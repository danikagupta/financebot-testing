import streamlit as st

st.set_page_config(
    page_title="Learn | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Learn key definitions")

st.write("""**Savings:** Money set away, perhaps to compound over time, in order to be retrieved later. Some examples of usage include retirement savings, an emergency fund in case of a sudden financial need, and saving up for a big purchase. Typically low-risk.
    \n **Budgeting:** Creating a detailed plan to allot money. Two popular strategies are the 50-30-20 and 75-15-10 rules. While 50-30-20 (of income, 50% to essentials, 30% non-essentials, and 20% to savings) is more well known, it can be hard for people who aren't as financially secure, so 75-15-10 (75% to spending, 15% to investing, and 10% to savings) may be better.
    \n **Credit:** The ability to make a purchase and pay for it later. For example, using a credit card and making the minimum monthly payments.
    \n **Interest:** An additional amount of money which is the cost of borrowing money, which is calculated as a percent of the total loan amount. Compounding interest is like interest on interest, as it grows over both the loan amount and previous interest rates. Non-compounding interest is called simple interest.
    \n **Debt:** Money which is owed to someone. Common examples are student loans and credit cards.
    \n **Loans:** A type of debt where a lender like a bank provides money upfront that you agree to repay in installments plus interest by a maturity date. For example, taking out a $15,000 personal loan from a bank for home renovations that you will pay back over 5 years with an interest rate at 7%.
    \n **Risk:** The potential for an investment or other such financial decision to result in an unexpected or not preferred outcome. Oftentimes correlated with volatility. Typically, high risk correlates to high returns and vice versa.
    \n **Investing:** To put money into an asset (such as stocks, bonds, real estate, or gold) with the expectation that it will grow in the future. For example, you might invest in a mutual fund. Stocks are highly risky, and bonds are typically safe.
""")