import streamlit as st
import requests

# Set the API endpoint
api_url = "https://cloudsol-finetune01-nxjjon2snq-uc.a.run.app/get_icd_codes_and_description"

# Streamlit app layout
st.title("ICD Code Chat Interface")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Text input for user
user_input = st.text_input("Enter ICD code or text:", key="user_input")

# Send button
if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state["messages"].append({"role": "user", "text": user_input})
        
        # Call the API
        try:
            response = requests.get(api_url, params={"input": user_input})
            response_json = response.json()
            icd_message = response_json.get("message", "No response received.")
            
            # Append API response to chat history
            st.session_state["messages"].append({"role": "api", "text": icd_message})
        except Exception as e:
            st.error(f"Error calling API: {e}")


# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**You:** {message['text']}")
    else:
        st.write(f"**API:** {message['text']}")

