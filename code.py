import streamlit as st

def find_largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("This is your Largest Number. new version")


a = st.number_input("First number:")
b = st.number_input("Second number:")
c = st.number_input("Third number:")

if st.button("Largest Number : "):
    largest_num = find_largest(a,b,c)
    st.write(f"The largest number : {largest_num}")
