import streamlit as st

st.set_page_config(
    page_title="About | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("About the website")
st.write("""
         **:green[Welcome to Money Matters!]** Here, we hope to help you take charge of your financial destiny 
         by learning about personal finance. With the **ask** page, you can ask our Chat-GPT-based AI 
         any burning finance questions you have, with the **learn** page you can quiz yourself on personal 
         finance basics, and on the **analyze** page you can paste in any financial statement or company 
         press release and we will summarize it and assess whether or not the company would be a good 
         investment right now.
         
         We have augmented our AI using resources from Khan Academy, the Federal Reserve Bank of St. Louis, TED-Ed, DardenMBA, PBS, and moneyinstructor.com, and *greatly appreciate* being able to build on their great work.""")
