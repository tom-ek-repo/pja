import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime

st.set_page_config(
    page_title="Ankieta",
    page_icon="👋",
)

st.header('Ankieta')

# st.subheader('pod nagłówek')

st.text('Uzupełnij dane:')

# st.markdown('# this is markdown 1A')
# st.markdown('## this is markdown 2')
# st.markdown('### this is markdown 3')  #więcej has mniejszy tekst
# st.markdown('# this is markdown 1B')

# st.success('dane ok')
# st.info('information')
# st.error('wprowadż nazwisko bez cyfr')

# st.exception('exception occured')

# st.help(range)

# st.write('some text')

# st.write("Wprowadź imię:")
# if st.checkbox("Masz drugie imię"):
#     st.write("Wprowadź drugię imię:")

# st.write("Wprowadź nazwisko:")

# img = Image.open('testImg.png')
# st.image(img, width=300, caption='simple image')

# dodawanie audio i video
# with open('Richmond.mov', 'rb') as vid_file:
#     vid = vid_file.read()
# st.video(vid)

# with open('Armin van Buuren  Tomorrowland Belgium 2018 W2.mp3', 'rb') as audio_file:
#     audio = audio_file.read()
# st.audio(audio)

# # widgets

# # checkbox:
# if st.checkbox("pokaz/hide"):
#     st.text("showing or hiding widget")

# # radio
# status = st.radio("What is your status", ("Active", "Inactive"))

# st.success('You are active') if status == 'Active' else st.warning("Inactive. Please activate")

 # # select box
# occupation = st.selectbox("Your Occupation", ("Programmer", "Data Analyst", "Teacher"))
# st.write("You selected this occupation: ", occupation)



# location = st.multiselect("Where are you based?", ("London", "Warsaw", "Sydney", "San Francisco"))
# st.write("You selected: ", len(location), " locations")

# slider
# level = st.slider("What is your level", 1, 100)

# # buttons
# st.button("Simple button")
# if st.button("About"):
#     st.text("This is a very cool demo")


# text input
firstname = st.text_input("Please, enter your 1st name", "Type here...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# text area
if st.checkbox("Do you have second name?"):
    secondname = st.text_input("Please enter your second name","Type here..")
    if st.button("Submit 2nd name"):
        result2 = secondname.title()
        st.success(result2)

# text area
surname = st.text_input("Please enter your surname","Type here..")
if st.button("Submit surname"):
    result3 = surname.title()
    st.success( result3)


# # date input
# today = st.date_input("Today is ", datetime.datetime.now())

# # time
# the_time = st.time_input("the time is ", datetime.time())

# displaying json
# st.text("Display JSON")
# st.json({'name': 'Dominika',
#         'gender': 'female'})

# # # displaying raw code
# st.text("Display raw code")
# st.code("import pandas as pd")

# # displaying raw code
# with st.echo():
#     # this will be shown as a comment
#     import pandas as pd
#     import numpy as np
#     df = pd.DataFrame({'name': ['Dominika', 'Grzegorz'],
#         'gender': ['female', 'male']})
#     df.head()

# # progress bar
# import time
# my_bar = st.progress(0)

# for p in range(100):
#     time.sleep(0.1)
#     my_bar.progress(p + 1)

# # spinner
# with st.spinner("Waiting..."):
#     time.sleep(3)
# st.success("Finished!")

# # SIDEBARS
# st.sidebar.header("About")
# st.sidebar.text("This is a Streamlit Demo")


# # function
# @st.cache
# def run_fxn():
#     return range(50)

# st.write(run_fxn())


