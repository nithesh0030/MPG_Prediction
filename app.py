
import pandas as pd
import numpy as np
import streamlit as st
from prediction import predict



st.title('Predict Mileage per Galon')
st.markdown('Model to predict MPG of a car')

st.header('Car Features')
col1,col2,col3,col4=st.columns(4)
with col1:
    cylinders=st.slider('Cylinders',2,8,1)
    displacement=st.slider('Displacement',50,500,10)
with col2:
    horsepower=st.slider('Horsepower',50,500,10)
    weight=st.slider('Weight',1500,6000,250)
with col3:
    acceleration=st.slider('Acceleration',8,25,1)
    modelYear=st.slider('ModelYear',70,85,1)
with col4:
    origin=st.slider('Origin',1,3,1) 



if st.button('Predict MPG of Car'):
    result=predict(np.array([[cylinders,displacement,horsepower,weight,acceleration,modelYear,origin]]))
    st.text(result[0])

