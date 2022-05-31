
from unittest import result
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
import requests
import numpy as np
from urllib.error import URLError
from PIL import Image
import re
import time
import streamlit_modal as modal
import streamlit.components.v1 as components
import torch
from FeedMe.utils import vector_output, score, load_data, load_image, ing_list
from ast import literal_eval


# Model for object detection
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

#col1, col2, col3 = st.columns([3, 1])


st.sidebar.title("FeedMe")
st.sidebar.header("Snap a picture of your fridge!")
image_file = st.sidebar.file_uploader(label='Upload it here below', type=["png","jpg","jpeg"])
imageLocation = st.sidebar.empty()
 # check supported data for test

if image_file is not None:
	# To See details
	file_details = {"filename":image_file.name, "filetype":image_file.type,
                            "filesize":image_file.size};
    # To View Uploaded Image
	imageLocation.image(load_image(image_file),width=300);

if st.sidebar.button('Inspect my fridge'):
    if image_file is  None:
        st.write('Can you show me your fridge please :smile:  :smiling_imp:')
    else:
        # print is visible in the server output, not in the page
        print('button clicked!')
        # Object detection
        results = model(load_image(image_file))
        results.save()
        imageLocation.image(load_image(f"runs/detect/exp/image0.jpg"), width=300)
        shutil. rmtree("runs/detect/exp/")
        # Output ingredients
        output_list = results.pandas().xyxy[0]["name"].unique()
        output_vector = vector_output(output_list)
        st.session_state.vector = output_vector


if st.sidebar.button('FeedMe'):
    st.header("Chef's Choice:")
    data = load_data(1000)
    df = data[ing_list].apply(lambda x: score(x, st.session_state.vector), axis=1)
    data["score"] = df["score"]
    data = data.sort_values(by="score", ascending=False)
    # Dataframe for troubleshooting
    # st.dataframe(data)

if 'data' in locals():
    row = data.head(1)
    one_image = row.Image_Name.iloc[0]
    recipe = row.Instructions.iloc[0]
    ingredient = row['Ingredients'].apply(literal_eval).iloc[0]
    st.session_state.recipe = recipe
    st.session_state.ingredient = ingredient
    st.image(load_image(f"raw_data/Recipes/Food Images/{one_image}.jpg"),width=500)
    st.subheader('Ingredients:')
    for i in ingredient:
        st.write(i)
    st.subheader('Instructions:')
    st.write(recipe)




#     open_modal = st.button("Recipe of " + row.Title.iloc[0])
# else:
#     open_modal = None

# if open_modal:
#     modal.open()

# if modal.is_open():
#     with modal.container():
#         html_string_0 = '''
#         <h2> Ingredients : </h2>

#         <script language="javascript">
#         document.querySelector("h1").style.color = "red";
#         </script>
#         '''
#         components.html(html_string_0)
#         ingredient= st.session_state.ingredient.split(',')

#         for index, line in enumerate( ingredient):
#             line = re.sub("[['!@#$]", '', line)
#             st.write((index +1) ,"-" ,line )

#         html_string = '''
#         <h2> Steps : </h2>

#         <script language="javascript">
#         document.querySelector("h1").style.color = "red";
#         </script>
#         '''
#         components.html(html_string)

#         recipe1=st.session_state.recipe.split('\n')
#         for index, line in enumerate( recipe1):
#             st.write((index +1) ,"-" ,line )









# if st.sidebar.button('FeedMe'):
#     data["score"] = data[ing_list].apply(lambda x: score(x, output_vector), axis=1)
#     data = data.sort_values(by="score")
#     for row in range(3):
#             one_image=data.Image_Name[row]
#             recipe=data.Instructions[row]

#             ingredient=data.Cleaned_Ingredients[row]
#             st.image(load_image(f"raw_data/Recipes/Food Images/{one_image}.jpg"),width=500);
#             #st.write(data.Title[row])


#             open_modal = st.button("Recipe of " + data.Title[row])

#             if open_modal:
#                 modal.open()

#             if modal.is_open():
#                 with modal.container():
#                     html_string_0 = '''
#                     <h2> Ingredients : </h2>

#                     <script language="javascript">
#                     document.querySelector("h1").style.color = "red";
#                     </script>
#                     '''
#                     components.html(html_string_0)
#                     ingredient= ingredient.split(',')

#                     for index, line in enumerate( ingredient):
#                         line = re.sub("[['!@#$]", '', line)
#                         st.write((index +1) ,"-" ,line )

#                     html_string = '''
#                     <h2> Steps : </h2>

#                     <script language="javascript">
#                     document.querySelector("h1").style.color = "red";
#                     </script>
#                     '''
#                     components.html(html_string)

#                     recipe1=recipe.split('\n')
#                     for index, line in enumerate( recipe1):
#                         st.write((index +1) ,"-" ,line )

#                     st.write("Bon appetit")
