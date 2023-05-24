import streamlit as st
import pandas as pd
import ast
import io
from utils import *


import streamlit as st

st.set_page_config(
    page_title="BrainNerd Model App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/DrKimLab/BrainNERD/issues',
        'Report a bug': "https://github.com/DrKimLab/BrainNERD/issues",
        'About': "### BrainNerd Model.https://github.com/DrKimLab/BrainNERD "
    }
)



st.write("# Welcome to BrainNerd Model App")


st.sidebar.success("Select a function from above to work on your data.")


st.markdown(
    """
    Brainnerd is an open-source Deep Learning app framework built specifically for
    extracting text categories from CT , MRIs and MRA Radiology reports.

    **👈 Select a function from the sidebar** to see some examples
    of what BrainNerd can do!

    ### Want to learn more?
    - Check out [BrainNerd page](https://github.com/DrKimLab/BrainNERD)
    - Jump into our [documentation](https://github.com/DrKimLab/BrainNERD)
    - Ask a question in our [community
        forums](https://github.com/DrKimLab/BrainNERD/issues)
    - Want to learn more about our lab? Check out [Dr.Kim Lab](https://www.drlabkim.com/)
    - Want to read or cite our paper? Check out [BrainNerd paper](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2795179)
    - Need to use a colab tutorial for low level functions? Check out [BrainNerdColab](https://colab.research.google.com/drive/1x7Kul4J4rYuIdlEuR8QRgtxzN6IXXHjg?usp=sharing)

    ### See more examples

"""

)


from PIL import Image


st.write("#### Example of model output on a CT report, looking only for hemorrage and size of hemorrage")

# Load image from file in the same folder as the .py file
#image = Image.open("Filter.png")

#make the image smaller
#image = image.resize((128, 128))

# Display image
#st.image(image, caption="Visualization of BrainNerd output on a CT report", use_column_width=True)





# Load image from file in the same folder as the .py file
image = Image.open("B_spacy.png")

# Display image
st.image(image, caption="Visualization of BrainNerd output on a CT report", use_column_width=True)






