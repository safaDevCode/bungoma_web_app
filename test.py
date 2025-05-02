import streamlit as st
import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Streamlit app title
st.title("MSSQL Table Selector")

# Retrieve database credentials from .env
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
driver = os.getenv("DRIVER")

# Function to get table names
def get_table_names(conn):
    query = """
    SELECT TABLE_NAME 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_TYPE = 'BASE TABLE'
    """
    return pd.read_sql(query, conn)['TABLE_NAME'].tolist()

# Connect to the database and display tables
if st.button("Connect"):
    try:
        # Establish connection
        conn_str = (
            f"DRIVER={driver};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        conn = pyodbc.connect(conn_str)
        
        # Get table names
        tables = get_table_names(conn)
        
        # Display dropdown
        if tables:
            selected_table = st.selectbox("Select a table", tables)
            st.write(f"Selected table: {selected_table}")
        else:
            st.write("No tables found in the database.")
        
        # Close connection
        conn.close()
        
    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")