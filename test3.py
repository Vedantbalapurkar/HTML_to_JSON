# from fastapi import FastAPI, UploadFile, File
# from unstructured.partition.auto import partition
# import uvicorn
# import os
# import json
# import streamlit as st

# import streamlit as st
# import os
# import json

# # def partition(filename):
# #     # Implement your partitioning logic here or call the appropriate function
# #     # from the unstructured.partition.auto module
# #     return ["element1", "element2", "element3"]

# def main():
#     st.title("File Upload and Partitioning")

#     uploaded_file = st.file_uploader("Upload a file", type=["html", "txt", "pdf"])

#     if uploaded_file is not None:
#         # Read the content of the uploaded file
#         content = uploaded_file.read()

#         # Save the content to a temporary file
#         temp_filename = "temp_file.html"  # Change the extension based on the actual file type
#         with open(temp_filename, "wb") as temp_file:
#             temp_file.write(content)

#         # Call the partition function using the saved file path
#         elements = partition(filename=temp_filename)

#         # Clean up: remove the temporary file
#         os.remove(temp_filename)

#         elements_json = json.dumps(elements)
        
#         # Display the extracted elements
#         st.write("Extracted elements:")
#         for element in elements_json:
#             st.write(element)

# if __name__ == "__main__":
#     main()




import streamlit as st
import os
import json
from unstructured.partition.auto import partition  

def main():
    st.title("File Upload and Partitioning")

    uploaded_file = st.file_uploader("Upload a file", type=["html", "txt", "pdf"])

    if uploaded_file is not None:
        # Read the content of the uploaded file
        content = uploaded_file.read()

        # Save the content to a temporary file
        temp_filename = "temp_file.html"  # Change the extension based on the actual file type
        with open(temp_filename, "wb") as temp_file:
            temp_file.write(content)

        # Call the partition function using the saved file path
        elements = partition(filename=temp_filename)  # Make sure the partition function is defined or imported

        # Clean up: remove the temporary file
        os.remove(temp_filename)

        # Display the extracted elements
        # st.write("Extracted elements:")
        # for element in elements:
        #     element_json = json.dumps(element)  # Convert the element to JSON format
        #     st.json(element_json)  # Display the JSON content


        for element in elements:
            # Convert the element to a serializable format (e.g., extract relevant attributes)
            #serializable_element = {"elements": element.elements}
            element_json = json.dumps([str(element) for element in elements[::]])  # Convert the serializable element to JSON format
            st.json(element_json)  # Display the JSON content

if __name__ == "__main__":
    main()
