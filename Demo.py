import streamlit as st


name = st.text_input("enter your name")
fname = st.text_input("enter your father name")
area = st.text_area("enter the text")
drop = st.selectbox("enter your class : " , (1,2,3,4,5,6,7,8,9,10,11,12) )

button = st.button("submit")

if button :
    st.markdown(
        f"""Name :{name}
            Father Name :{fname}
            Addresh :{area}
            Your Class : {drop} 
             """)
