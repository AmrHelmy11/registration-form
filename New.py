import streamlit as st
import sqlite3
import pandas as pd
import os

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('elsewedy_workshop.db')  # Create or connect to the database
    return conn

# Function to create the table if it doesn't exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            phone INTEGER NOT NULL,
            faculty TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, phone_number, faculty):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, phone, faculty) VALUES (?, ?, ?)', (name, phone, faculty))
    conn.commit()
    conn.close()

# Function to save data to a CSV file
def save_to_csv(data):
    # Check if the CSV file exists
    if os.path.exists('elsewedy_workshop.csv'):
        # If it exists, append the new data
        existing_data = pd.read_csv('elsewedy_workshop.csv')
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        updated_data.to_csv('elsewedy_workshop.csv', index=False)
    else:
        # If it doesn't exist, create a new one
        data.to_csv('elsewedy_workshop.csv', index=False)

# Create the table
create_table()

# Streamlit form
st.title("El Sewedy Workshop (Factory Model)")

with st.form(key='data_form'):
    name = st.text_input("Name")
    phone = st.number_input("phone number", min_value=0)
    faculty = st.text_input("faculty")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Insert the data into the database
        insert_data(name, phone, faculty)

        # Create a DataFrame from the input data
        data = pd.DataFrame({
            'Name': [name],
            'Phone Number': [phone],
            'Faculty': [faculty]
        })

        # Save the data to CSV
        save_to_csv(data)

        st.success("Data saved successfully!")


# Button to display data from the database
#if st.button("Show Data"):
 #   conn = create_connection()
  #  df = pd.read_sql_query("SELECT * FROM users", conn)
   # conn.close()
    #st.dataframe(df)
