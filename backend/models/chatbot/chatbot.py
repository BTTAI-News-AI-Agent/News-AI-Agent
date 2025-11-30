from openai import OpenAI
from dotenv import load_dotenv
import os
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


