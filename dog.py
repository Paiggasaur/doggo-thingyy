import streamlit as st
from PIL import Image
import numpy as np

def simulate_dog_vision(image):
    img_array = np.array(image)
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    gray = (r + g + b) // 3
    dog_b = b
    dog_y = (r + g) // 2
    
    simulated_image = np.stack([gray, dog_y, dog_b], axis=-1)
    return Image.fromarray(simulated_image.astype('uint8'))

def generate_human_colors_for_dog(image):
    img_array = np.array(image)
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    grayish_brown = ((r + g + b) // 3 + r) // 2
    muted_yellow = (r + g) // 2
    pale_blue = (b + 128) // 2 
    
    dog_human_mapped_image = np.stack([grayish_brown, muted_yellow, pale_blue], axis=-1)
    return Image.fromarray(dog_human_mapped_image.astype('uint8'))
    
st.title("Doggo Thing")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="OG image.", use_column_width=True)
    
    dog_vision_image = simulate_dog_vision(image)
    st.image(dog_vision_image, caption="Image as seen by a dog.", use_column_width=True)
    
    dog_vision_image = generate_human_colors_for_dog(image)
    st.image(dog_vision_image, caption="Image redefined so that a dog can percieve it the way a human would.", use_column_width=True)

