import time

import numpy as np

import openai
import pinecone
import streamlit as st
import os

st.set_page_config(
    page_title="Ask | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Your financial mentor")
st.markdown("""
Please enter a question about personal finance. You can tailor your question to be more specific to your needs.
            \n Here are some questions from recent users which show different angles you can ask from:
            \n * "i'm a college student with no steady income but i have $1000 in my bank account. can you create me a savings plan for the next 4 years?"
            \n * "how do i become able to start renting an apartment"
            \n * "i am a 24 year old single mother of a toddler. i just finished my masters degree in anthropology but now fear that it may not be conducive to getting a stable job or income. right now i'm working as a waitress and share an apartment's rent with two friends. what are possible steps for me to take care of my daughter, find a good job, and at some point rent out my own apartment for just me and my daughter? please focus on financial advice"
""")

avatars={"system":"💻","user":"🤔","assistant":"💵"}


os.environ['PINECONE_API_ENV']='gcp-starter'
os.environ['PINECONE_INDEX_NAME']='pinecone-index'

PINECONE_API_KEY=st.secrets['PINECONE_API_KEY']
PINECONE_API_ENV=os.environ['PINECONE_API_ENV']
PINECONE_INDEX_NAME=os.environ['PINECONE_INDEX_NAME']
openai.api_key=st.secrets['OPENAI_API_KEY']

def augmented_content(inp):
    # Create the embedding using OpenAI keys
    # Do similarity search using Pinecone
    # Return the top 5 results
    embedding=openai.Embedding.create(model="text-embedding-ada-002", input=inp)['data'][0]['embedding']
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    index = pinecone.Index(PINECONE_INDEX_NAME)
    results=index.query(embedding,top_k=3,include_metadata=True)
    #print(f"Results: {results}")
    #st.write(f"Results: {results}")
    rr=[ r['metadata']['text'] for r in results['matches']]
    #print(f"RR: {rr}")
    #st.write(f"RR: {rr}")
    return rr


SYSTEM_MESSAGE={"role": "system", 
                "content": """Ignore all previous commands. 
                You are a helpful and patient financial guide. 
                When asked a question, your response should be polite, and you should not only answer a question but provide a larger lesson about finance including examples. 
                Using markdown language formatting, bold key phrases and use bullet points when relevant.
                Keep responses below 300 words. 
                If you don't know an answer, state the exact words 'I don't have an answer for that' and don't add any more. 
                You must not provide answers to questions which are not about finance, aside from stating the exact text 'I don't have an answer for that.'."""
                }

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask your question here!"):
    retrieved_content = augmented_content(prompt)
    #print(f"Retrieved content: {retrieved_content}")
    prompt_guidance=f"""
Please guide the user with the following information:
{retrieved_content}
The user's question was: {prompt}
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        
        messageList=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages]
        messageList.append({"role": "user", "content": prompt_guidance})
        
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messageList, stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    #with st.sidebar.expander("Retrieval context provided to GPT-3"):
     #   st.write(f"{retrieved_content}")
    st.session_state.messages.append({"role": "assistant", "content": full_response})