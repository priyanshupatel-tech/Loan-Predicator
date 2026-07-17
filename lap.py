import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")

st.title("Loan Apporval Predicator!!!")
age=st.number_input("Enter your Age")
sal=st.number_input("Enter your monthly Income")
cs=st.number_input("Enter your credit Score")
exp=st.number_input("Enter your Ecperince year")
la=st.number_input("Enter your loan amount")

btn=st.button("Predict Loan Approval")
if btn:
    model=pickle.load(open("lap.pkl","rb"))
    result=model.predict([[age,sal,cs,exp,la]])[0]
    if result==1:
        st.success("Your Loan will be Approve")
    else:
        st.success("Your Loan Will be Reject")