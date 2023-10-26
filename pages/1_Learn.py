import streamlit as st

st.set_page_config(
    page_title="Learn | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Learn basic definitions")
#st.subheader("Learn basic personal finance terms and gain a jumping-off point for the ask page")

st.write("""Savings: Money set away, perhaps to compound over time, in order to be retrieved later. Some examples of usage include retirement savings, an emergency fund in case of a sudden financial need, and saving up for a big purchase.
    Investing:To put money into an asset (such as stocks, bonds, real estate, or gold) with the expectation that it will grow in the future.
    Credit: The ability to make a purchase and pay for it later.
    Debt: Money which is owed to someone.
    Loans: Money which is given, typically by a bank, with the expectation of later repayment.
    Interest: Additional money which you pay to borrow money.
    Budgeting: Creating a plan to allot money.
""")