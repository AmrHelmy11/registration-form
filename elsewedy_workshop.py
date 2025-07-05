import streamlit as st
import pandas as pd
import os

# Create a title for the app
st.title("El Sewedy Workshop (Factory Model)")

# Create a form with input fields
with st.form("user_data_form"):
    name = st.text_input("Name")
    phone_number = st.number_input("Phone Number", min_value=0 , step=1)
    Faculty = st.text_input("Faculty")
    submit_button = st.form_submit_button("Submit")

# Create a CSV file to store the user data
csv_file = "elsewedy_workshop.csv"

# Check if the form has been submitted
if submit_button:
    # Create a dictionary to store the user data
    user_data = {"Name": name, "Phone Number": phone_number,"Faculty":Faculty}

    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        # Create a new CSV file with the header row
        pd.DataFrame(columns=["Name", "Phone Number" ,"Faculty"]).to_csv(csv_file, index=False)

    # Append the new user data to the CSV file
    pd.DataFrame([user_data]).to_csv(csv_file, mode="a", header=False, index=False)

    # Display a success message
    st.success("Data submitted successfully!")

# Display a table with the collected user data
if os.path.exists(csv_file):
    user_data_df = pd.read_csv(csv_file)
    
else:
    st.write("No data collected yet!")
