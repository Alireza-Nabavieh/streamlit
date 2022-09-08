import streamlit as st
import pandas


data={
  'Series 1':[1,3,4,5,7],
  'Series 2':[10,30,40,100,250]
}

df=pandas.DataFrame(data)


st.title('Our first steam application')
st.subheader('Introduction Streamlit')

st.write('''
This is the first web App
''')

#local run= streamlit run main.py


st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider=st.slider('Celsius')

st.write(myslider, 'In Farenheit is', 9.5*myslider + 32)