import streamlit as st
import pandas as pd
import requests
import snowflake.connector
import numpy as np
from urllib.error import URLError
from PIL import Image
import re

import streamlit_modal as modal
import streamlit.components.v1 as components






def load_image(image_file):
	img = Image.open(image_file)
	return img
st.header("FeedMe")
st.subheader("Fridge Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"]) # check supported data for test

if image_file is not None:

			# To See details
	file_details = {"filename":image_file.name, "filetype":image_file.type,
                            "filesize":image_file.size};
	st.write(file_details);


              # To View Uploaded Image
	st.image(load_image(image_file),width=250);



if st.button('Get my recipe') :
    if image_file is  None:
        st.write('Can you shome me your fridge please :smile:  :smiling_imp:')
    else:
        # print is visible in the server output, not in the page
        print('button clicked!')
        st.write('Your Fridg contains :')
        st.write('Wow! You can prepare one of those recipes: ')

        import time

        'We are looking for the perfect recepies for you...'

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(10):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)


        '...and now we\'re done! Choose your recipe'


def load_data(nrows):
    data = pd.read_csv('data/data.csv', nrows=nrows)

    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data = data.drop(columns=['Unnamed: 0', 'Ingredients'])

    return data

data = load_data(4)

for row in range(data.shape[0]):
        one_image=data.Image_Name[row]
        recipe=data.Instructions[row]
<<<<<<< Updated upstream


        st.image(load_image(f"data/Food Images/{one_image}.jpg"),width=500);
=======
        ingredient=data.Cleaned_Ingredients[row]
        st.image(load_image(f"data/Food Images/{one_image}.jpg"),width=500);
        #st.write(data.Title[row])
>>>>>>> Stashed changes


        open_modal = st.button("Recipe of " + data.Title[row])

        if open_modal:
            modal.open()

        if modal.is_open():
            with modal.container():

                html_string_0 = '''
                <h2> Ingredients : </h2>

                <script language="javascript">
                document.querySelector("h1").style.color = "red";
                </script>
                '''
                components.html(html_string_0)
                ingredient= ingredient.split(',')

                for index, line in enumerate( ingredient):
                    line = re.sub("[['!@#$]", '', line)
                    st.write((index +1) ,"-" ,line )

<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
                html_string = '''
                <h2> Steps : </h2>

                <script language="javascript">
                document.querySelector("h1").style.color = "red";
                </script>
                '''
                components.html(html_string)

                recipe1=recipe.split('\n')
                for index, line in enumerate( recipe1):
                    st.write((index +1) ,"-" ,line )

                st.write("Bon appetit")
