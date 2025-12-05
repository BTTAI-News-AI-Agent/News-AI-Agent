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

import os
from openai import OpenAI
from dotenv import load_dotenv
from models.summarization.summarization import generate_summary
from models.categorization.categorize import predict_category

def setup():
    # Load the .env file
    load_dotenv()

    # Get your API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the client
    client = OpenAI(api_key=api_key)

    return client


def askQuestion(client: OpenAI, article, question="Summarize the article."):
    '''
    Answers given question about article using GPT

    Args:
        client: OpenAI object with API key 
        question: question about the article from user
        article: article in text format 

    Returns:
        Answer to question based on article.
    '''
    model_type = "gpt-4o-mini"
    messages = [
        {
            "role": "system",
            "content": (
                "You are given an article as context. Read and analyze the article carefully, "
                "then use its information to provide a specific, well-supported, and concise answer to the following question. "
                f"Answer the question: {question}\n\n"
            ),
        },
        {
            "role": "user",
            "content": f"Here is the article:{article}"
        }
    ]
    response = client.chat.completions.create(
        model=model_type,
        messages=messages
    )
    
    return response.choices[0].message.content


################# AGENT #####################

def run_agent(client: OpenAI, headline, description, question):
    print("agent")

    # The latest user input
    user_message = question

    # === Step 1: Ask GPT to decide which tool to use ===
    system_prompt = """You are an autonomous news analysis agent.
Your only goal is to choose the correct tool.

TOOLS:
- summarize → used when the user asks for summary, main points, TLDR, overview
- categorize → used when the user asks for topic, category, section
- ask → used when the user asks a question that requires analyzing the article

FORMAT:
Return ONLY ONE WORD:
summarize
categorize
ask
none

Never return sentences.
Never return anything else.

EXAMPLES:
User: "give me a summary"
Assistant: summarize

User: "what category is this?"
Assistant: categorize

User: "what topic or genre?"
Assistant: categorize

User: "categorize"
Assistant: categorize

User: "why is this important?"
Assistant: ask
"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "summarize_article",
                "description": "Summarizes the content of an article",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "headline": {
                            "type": "string",
                            "description": "The headline of the article"
                        },
                        "description": {
                            "type": "string",
                            "description": "The description/content of the article"
                        }
                    },
                    "required": ["headline", "description"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "categorize_article",
                "description": "Categorizes an article into business, entertainment, politics, sports, or tech",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "headline": {
                            "type": "string",
                            "description": "The headline of the article"
                        },
                        "description": {
                            "type": "string",
                            "description": "The description/content of the article"
                        }
                    },
                    "required": ["headline", "description"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "askQuestion",
                "description": "Answer a custom question about the article using GPT analysis",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article": {
                            "type": "string",
                            "description": "The full article text (headline + description)"
                        },
                        "question": {
                            "type": "string",
                            "description": "The question to answer about the article"
                        }
                    },
                    "required": ["article", "question"]
                }
            }
        }
    ]

    # Ask GPT to choose a tool
    choice = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    ).choices[0].message.content.strip().lower()

    print(f"Tool selected: {choice}")
    print(choice)
    # === If GPT chooses a tool ===
    if  "summarize" in choice:
        print("========== Summarization T5 Model Used ============")
        return generate_summary(description)

    elif "categorize" in choice:
        print("========== Categorization Classification Model Used ============")
        return predict_category(headline, description)
    
    elif "ask" in choice:
        print("========== General GPT Model Used ============")
        article = f"{headline}\n\n{description}"
        return askQuestion(client, article, question)
    
    # === If GPT answers directly ===
    else:
        print("========== No Tool Used, GPT Direct Answer ============")
        # get GPT to check if its article related
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Is this an article related question like asking to summarize, categorize, or about the article? Return ONLY one of the following: yes, no"},
                {"role": "user", "content": f"{user_message}"},
            ],
        )
        print(response.choices[0].message.content)
        #article related
        if response.choices[0].message.content == "yes":
            print("========== Article Related Question ============")
            # GPT provides a direct answer
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"{user_message}\n\nHeadline: {headline}\nDescription: {description}"},
                ],
            )
            return response.choices[0].message.content
    
        #article not related or failed attempt
        else:
            print("========== General Question ============")
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"{user_message}"},
                ],
            )
            return response.choices[0].message.content
       
        
def run_agent_draft(client: OpenAI, headline, description, question):
    print("agent")

    # The latest user input
    user_message = question

    # === Step 1: Ask GPT to decide which tool to use ===
    system_prompt = """
    You are an autonomous news analysis agent.
    You have the following tools:
    1. summarize_article - summarize the article content
    2. categorize_article - categorize the article into one of the following: business, entertainment, politics, sports, tech
    3. askQuestion - answer a custom question about the article using GPT

    Choose the tool that answers the user's request. Return ONLY one word: summarize, categorize, ask, or none.
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "summarize_article",
                "description": "Summarizes the content of an article",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "headline": {
                            "type": "string",
                            "description": "The headline of the article"
                        },
                        "description": {
                            "type": "string",
                            "description": "The description/content of the article"
                        }
                    },
                    "required": ["headline", "description"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "categorize_article",
                "description": "Categorizes an article into business, entertainment, politics, sports, or tech",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "headline": {
                            "type": "string",
                            "description": "The headline of the article"
                        },
                        "description": {
                            "type": "string",
                            "description": "The description/content of the article"
                        }
                    },
                    "required": ["headline", "description"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "askQuestion",
                "description": "Answer a custom question about the article using GPT analysis",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article": {
                            "type": "string",
                            "description": "The full article text (headline + description)"
                        },
                        "question": {
                            "type": "string",
                            "description": "The question to answer about the article"
                        }
                    },
                    "required": ["article", "question"]
                }
            }
        }
    ]

    # Ask GPT to choose a tool
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        tools=tools,
        tool_choice="auto"
    )

    msg = response.choices[0].message
    
    # === If GPT chooses a tool ===
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        tool_name = tool_call.function.name
        
        print(f"Tool selected: {tool_name}")

        if tool_name == "summarize_article":
            print("========== Summarization T5 Model Used ============")
            return generate_summary(description)

        elif tool_name == "categorize_article":
            print("========== Categorization Classification Model Used ============")
            return predict_category(headline, description)
        
        elif tool_name == "askQuestion":
            print("========== General GPT Model Used ============")
            article = f"{headline}\n\n{description}"
            return askQuestion(client, article, question)
    
    # === If GPT answers directly ===
    else:
        print("========== No Tool Used, GPT Direct Answer ============")
        # GPT provides a direct answer
        if msg.content:
            return msg.content
        else:
            # Fallback: make another call with article context
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"{user_message}\n\nHeadline: {headline}\nDescription: {description}"},
                ],
            )
            return response.choices[0].message.content