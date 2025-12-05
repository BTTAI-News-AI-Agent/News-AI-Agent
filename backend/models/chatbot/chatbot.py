import os
from openai import OpenAI
from dotenv import load_dotenv
from models.summarization.summarization import generate_summary
from models.categorization.categorize import predict_category
#chatbot functionality

def setup():
    # Load the .env file
    load_dotenv()

    # Get your API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the client
    client = OpenAI(api_key=api_key)

    return client

#def processArticle():

def askQuestion(client: OpenAI, article, question= "Summarize the article."):
    '''
    Answers given question about article using GPT

    Args:
        client: OpenAI object with API key 
        question: question about the article from user
        article: article in text format 


    Returns:
        Answer to question based on article.
    '''
    #specifications of model type and general prompt
    model_type="gpt-4o-mini"
    messages=[
            #general prompt
            {   "role": "system",
                "content": ("You are given an article as context. Read and analyze the article carefully, "
                    "then use its information to provide a specific, well-supported, and concise answer to the following question. "
                    #"Be sure to cite or refer to specific parts of the article in your reasoning when relevant."
                    f"Answer the question: {question}\n\n"
                ),
            },

            { "role": "user",
               "content": f"Here is the article:{article}"}
    ]
    response = client.chat.completions.create(
        model=model_type,
        messages = messages
    )
    
    return response.choices[0].message.content


################# AGENT #####################

def run_agent(client: OpenAI, headline, description, question):
    print("agent")

    # The latest user input
    user_message = question

    # === Step 1: Ask GPT to decide which tool to use ===
    system_prompt = """
    You are an autonomous news analysis agent.
    You have the following tools:
    1. summarize_article(headline, description) - summarize the article content
    2. categorize_article(headline, description) - categorize the article into one of the following: business, entertainment, politics, sports, tech
    
    Choose ONLY the tool that best answers the user's request.
    """

    
    tools = [
    {
        "name": "summarize_article",
        "type": "function",
        "description": "Summarizes the content of an article",
        "function": {
            "name": "summarize_article",
            "parameters": {
                "type": "object",
                "properties": {
                    "headline": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["headline", "description"]
            }
        }
    },
    {
        "name": "categorize_article",
        "type": "function",
        "description": "Categorizes an article into business, entertainment, politics, sports, or tech",
        "function": {
            "name": "categorize_article", 
            "parameters": {
                "type": "object",
                "properties": {
                    "headline": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["headline", "description"]
            }
        }
    }
    ]


    # ask GPT to choose a tool
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        tools=tools
    )

    msg = response.choices[0].message
    print(msg.tool_calls, msg.content)
    # === If GPT chooses a tool ===
    if msg.tool_calls:
        tool = msg.tool_calls[0]
        tool_name = tool.function.name


        if tool_name == "summarize_article":
            print("========== Summarization T5 Model Used ============")
            return generate_summary( description)

        if tool_name == "categorize_article":
            print("========== Categorization Classification Model Used ============")
            return predict_category(headline, description)
    else:
        print("========== No Tool Used ============")
        #add article to prompt
        user_message += f"\nHeadline: {headline}\nDescription: {description}"
          # ask GPT to choose a tool
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_message},
            ],
        )
        msg = response.choices[0].message
    # === If GPT answers directly ===
    return msg.content