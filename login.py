import streamlit as st
from users import USERS

def login_page(authenticate_user):
    st.markdown(
        """
        <style>
            .image-container {
                text-align: center;
                margin-bottom: 20px;
            }
            .image-container img {
                border-radius: 50%;
                width: 300px;
                height: 300px;
                object-fit: cover;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
        <div class="image-container">
        </div>
        """,
        unsafe_allow_html=True
    )

    try:
        with st.container():
            st.image("images/nice.png", use_container_width=False)
    except FileNotFoundError:
        st.error("Image file 'images/nice.png' not found.")
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        from users import USERS  
        department = authenticate_user(username, password, USERS)
        if department:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['department'] = department
            st.success(f"Welcome {username}!")
            st.rerun()
        else:
            st.error("Incorrect username or password")