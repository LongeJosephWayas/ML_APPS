import streamlit as st


#Set title

st.title('Our First Streamlit App')

from PIL import Image

st.subheader('This is a subheader')

image=Image.open("C:\\Users\\Hp\\OneDrive\\Pictures\\logo-color.png") 
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write("Put something here")

st.markdown("This is a markdown cell")

st.success("Congrats you run the App successfully")

st.info("This is an information for you")

st.warning('Be cautious')

st.error("Oops you run into an error,you need to rerun the app again or uninstall and install the app again")

st.help(range)

import numpy as np
import pandas as pd

dataframe=np.random.rand(10,20)

st.dataframe(dataframe)


st.text("-----"*100)

df=pd.DataFrame(np.random.rand(10,20),columns=('col %d'% i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=1))

st.text("-----"*100)

#DDisplay chart

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(chart_data)

st.text("-----"*100)

st.area_chart(chart_data)


chart_data=pd.DataFrame(np.random.randn(50,3),columns=['a','b','c'])

st.bar_chart(chart_data)

import matplotlib.pyplot as plt

arr=np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
st.pyplot() 

st.text("-----"*100)



import plotly
import plotly.figure_factory as ff

#Adding distplot

x1=np.random.randn(200)-2
x2=np.random.randn(200)
x3=np.random.randn(200)-2

hist_data=[x1,x2,x3] 
group_labels=['Group1','Group2','Group3']

fig=ff.create_distplot(hist_data,group_labels,bin_size=[.2,.25,.5])

st.plotly_chart(fig,use_container_width=True)

st.text("-----"*100)


df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])

st.map(df)


st.text("-----"*100)



#Creating buttons

if st.button("say hello"):
	st.write("hello is here")
else:
    st.write("why are you here")

st.text("-----"*100)


genre=st.radio("what is your favourite genre?",('comedy','Drama','Documentary'))

if genre=='comedy':
	st.write("oh you like comedy")
elif genre=='Drama':
	st.write('Yeah Drama is cool')
else:warning
st.write('I see!!')


st.text("-----"*100)

#Select button
option=st.selectbox("How was your night?",('Fantastic','Awesome','So-so'))

st.write("Your said was:",option)

st.text("-----"*100)
option=st.multiselect("How was your night,you can select multiple choice?",('Fantastic','Awesome','So-so'))

st.write("Your said was:",option)

st.text("-----"*100)


age=st.slider('How old are you?',0,150,10)
st.write("You age is : ",age)

values=st.slider('selecta range of values',0,200,(15,80))

st.write('You selected range between:',values)

number=st.number_input('Input number')
st.write('The number you inputed is:',number)


st.text("-----"*100)
st.text("-----"*100)


#File uploader

upload_file=st.file_uploader("Choose a csv file",type='csv')

if upload_file is not None:
	data=read_csv(upload_file)
	st.write(data)
	st.success("successfully uploaded")
else:
    st.markdown("Please upload a csv file")	

#Color picker

color=st.sidebar.color_picker("Pick your preferred color:",'#00f900')
st.write("This is your color:",color)

#Side bar

st.text("-----"*100)
st.text("-----"*100)


add_sidebar=st.sidebar.selectbox('what is your favourite course?',('A course from TDS on building Data web APP','others','Am not sure'))


import time

my_bar=st.progress(0)
for percent_complete in range(100):
	time.sleep(0.1)
	my_bar.progress(percent_complete+1)

with st.spinner('wait for it.....'):
	time.sleep(5)
st.success('successful')

	
st.balloons()


