from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
import pandas as pd

ing_list = ["apple",
        "banana",
        "beef",
        "blueberry",
        "bread",
        "butter",
        "carrot",
        "cheese",
        "chicken",
        "chocolate",
        "corn",
        "egg",
        "flour",
        "bean",
        "ham",
        "cream",
        "lime",
        "milk",
        "mushroom",
        "onion",
        "potato",
        "shrimp",
        "spinach",
        "strawberry",
        "sugar",
        "tomato"]

# Dictionary that maps class names to IDs
# class_name_to_id_mapping = {

# }
# class_id_to_name_mapping = dict(zip(class_name_to_id_mapping.values(), class_name_to_id_mapping.keys()))

# def plot_bounding_box(image, annotation_list):
#     annotations = np.array(annotation_list)
#     w, h = image.size

#     plotted_image = ImageDraw.Draw(image)

#     transformed_annotations = np.copy(annotations)
#     transformed_annotations[:,[1,3]] = annotations[:,[1,3]] * w
#     transformed_annotations[:,[2,4]] = annotations[:,[2,4]] * h

#     transformed_annotations[:,1] = transformed_annotations[:,1] - (transformed_annotations[:,3] / 2)
#     transformed_annotations[:,2] = transformed_annotations[:,2] - (transformed_annotations[:,4] / 2)
#     transformed_annotations[:,3] = transformed_annotations[:,1] + transformed_annotations[:,3]
#     transformed_annotations[:,4] = transformed_annotations[:,2] + transformed_annotations[:,4]

#     for ann in transformed_annotations:
#         obj_cls, x0, y0, x1, y1 = ann
#         plotted_image.rectangle(((x0,y0), (x1,y1)))

#         plotted_image.text((x0, y0 - 10), class_id_to_name_mapping[(int(obj_cls))])

#     plt.imshow(np.array(image))
#     plt.show()

# # Read images and annotations
# images = [os.path.join('images', x) for x in os.listdir('images')]
# annotations = [os.path.join('annotations', x) for x in os.listdir('annotations') if x[-3:] == "txt"]

# images.sort()
# annotations.sort()

# # Split the dataset into train-valid-test splits
# train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 1)
# val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)

# def convert_labels(labels):
#     df = pd.read_csv(labels)
#     file_names = df["filename"].values
#     for file in file_names:
#         file_save_name = file[:-3] + "txt"
#         df_test = df[df["filename"] == file]
#         df_test["x_center"] = (df_test["xmax"] - df_test["xmin"])/2
#         df_test["y_center"] = (df_test["ymax"] - df_test["ymin"])/2
#         df_test["width"] = (df_test["xmax"] - df_test["xmin"])
#         df_test["height"] = (df_test["ymax"] - df_test["ymin"])
#         X = df_test[["x_center", "y_center", "width", "height"]].to_numpy()
#         np.savetxt(file_save_name, X)

def vector_output(list_1):
    ing_list = ["apple",
                "banana",
                "beef",
                "blueberry",
                "bread",
                "butter",
                "carrot",
                "cheese",
                "chicken",
                "chocolate",
                "corn",
                "egg",
                "flour",
                "bean",
                "ham",
                "cream",
                "lime",
                "milk",
                "mushroom",
                "onion",
                "potato",
                "shrimp",
                "spinach",
                "strawberry",
                "sugar",
                "tomato"]
    V = ing_list.copy()
    for i, ing in enumerate(V):
        if ing in list_1:
            V[i] = 1
        else:
            V[i] = 0
    return V

def score(row, vector):
    #computes dot product
    A = row.to_numpy()
    row["score"] = np.matmul(A, vector)
    return row

def load_data(nrows):
    data = pd.read_csv("raw_data/3006_receipe_final.csv", nrows=nrows)

    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data = data.drop(columns=['Unnamed: 0', 'Ingredients'])

    return data


def vegfilter(df, vegetarian=False, vegan=False):
    if vegan == True:
        df_filtered = df[df['vegan']==1]
    elif vegetarian == True:
        df_filtered = df[df['vegetarian']==1]
    else:
        df_filtered = df
    return df_filtered


def difficulty(df, max_prep_time=10000, max_complexity=0):
    df_filtered = df[df['Prep Time']<=max_prep_time]
    df_filtered = df_filtered[df_filtered['complexity']<=max_complexity]
    return df_filtered

def allergencheck(df, milk = False, egg = False, mustard=False, peanut=False, soy=False, walnut=False, almond=False, hazelnut=False, pecan=False,
cashew=False, pistachio=False, wheat=False):
    df_f = df
    if milk == True:
        df_f = df_f[df_f['milk']==0]
    if egg == True:
        df_f = df_f[df_f['egg']==0]
    if mustard == True:
        df_f = df_f[df_f['mustard']==0]
    if peanut == True:
        df_f = df_f[df_f['peanut']==0]
    if soy == True:
        df_f = df_f[df_f['soy']==0]
    if walnut == True:
        df_f = df_f[df_f['walnut']==0]
    if almond == True:
        df_f = df_f[df_f['almond']==0]
    if cashew == True:
        df_f = df_f[df_f['cashew']==0]
    if pistachio == True:
        df_f = df_f[df_f['pistachio']==0]
    if wheat == True:
        df_f = df_f[df_f['wheat']==0]
    return df_f

def load_image(image_file):
	img = Image.open(image_file)
	return img

