import streamlit as st
import os
import json
from unstructured.partition.auto import partition  # Make sure this import is correct
import requests  # Import the requests library to fetch content from URL
from unstructured.partition.html import partition_html
import urllib.parse


def fetch_content_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Failed to fetch content from the provided URL")
        return None

def main():
    st.title("Content Partitioning")

    option = st.radio("Select an option:", ["Upload a File", "Enter a URL"])

    if option == "Upload a File":
        uploaded_file = st.file_uploader("Upload a file", type=["html", "txt", "pdf"])
        if uploaded_file is not None:
            content = uploaded_file.read()
            upload_content(content)

    elif option == "Enter a URL":
        url = st.text_input("Enter a URL to fetch content from")
        if url:
            content = fetch_content_from_url(url)
            if content is not None:
                url_content(url)

def url_content(url):

    elements = partition_html(url=url, ssl_verify=False)  # Make sure the partition function is defined or imported

            # Display the extracted elements
    st.write("Extracted elements:")
    for element in elements:
                # Convert the element to a serializable format (e.g., extract relevant attributes)
                # serializable_element = {"elements": element.elements}
                # You need to modify this part based on the structure of the elements

                # Convert the serializable element to JSON format
        element_json = json.dumps(element.__dict__, default=str, indent=2)
        st.json(element_json)  # Display the JSON content

                # Add a download button
    extracted_content = "\n\n".join([json.dumps(element.__dict__, default=str, indent=2) for element in elements])
    extracted_filename = "extracted_content.json"
    #st.download_button("Download Extracted Content", data=extracted_content, file_name=extracted_filename)
    download_link = f'<a href="data:application/json;charset=utf-8,{urllib.parse.quote(extracted_content)}" download="{extracted_filename}">Download Extracted Content</a>'
    st.markdown(download_link, unsafe_allow_html=True)



def upload_content(content):
        # Save the content to a temporary file
    temp_filename = "temp_file.html"  # Change the extension based on the actual file type
    with open(temp_filename, "wb") as temp_file:
        temp_file.write(content)

        # Call the partition function using the saved file path
    elements = partition(filename=temp_filename)  # Make sure the partition function is defined or imported

        # Clean up: remove the temporary file
    os.remove(temp_filename)

        


    for content in elements:
            
        element_json = json.dumps([str(content) for content in elements[::]])  # Convert the serializable element to JSON format
        st.json(element_json)

    # Add a download button
    extracted_content = "\n\n".join([json.dumps(content.__dict__, default=str, indent=2) for content in elements])
    extracted_filename = "extracted_content.json"
    #st.download_button("Download Extracted Content", data=extracted_content, file_name=extracted_filename)
    download_link = f'<a href="data:application/json;charset=utf-8,{urllib.parse.quote(extracted_content)}" download="{extracted_filename}">Download Extracted Content</a>'
    st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



