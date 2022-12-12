import pandas as pd
import streamlit as st
import pickle
from xgboost import XGBRegressor

st.title('To Predict The Ingersoll Rand Air Compressor's Actual Delivery Air Flow')

st.sidebar.header('PLEASE INPUT THE REQUIRED DETAILS')


def user_input_features():
	global controller
	model= st.sidebar.text_input("Enter Model Number here")
	power = st.sidebar.number_input("Enter power here")
	pressure = st.sidebar.number_input("Enter pressure here")
	weight = st.sidebar.number_input("Enter weight here")
	controller = st.sidebar.selectbox("Enter controller type here", ('microprocessor','relay control panel','xe-90m','xe-70m'))
		
	data = {"model name": model,
       "power": power,
        "pressure": pressure,
        "weight": weight,
		"controller": controller}
	feature = pd.DataFrame(data,index=[0])
	return feature
	
df = user_input_features()
st.subheader('USER INPUT PARAMETERS')
st.write(df)


if controller == "microprocessor":
	df["relay_control"] = 0
	df["microprocessor"]=1
	df["xe_70"]=0
	df["xe_90"]=0	

if controller == "relay control panel":
	df["relay_control"] = 1
	df["microprocessor"]=0
	df["xe_70"]=0
	df["xe_90"]=0		

if controller == "xe-90m":
	df["relay_control"] = 0
	df["microprocessor"]=0
	df["xe_70"]=0
	df["xe_90"]=1	

if controller == "xe-70m":
	df["relay_control"] = 0
	df["microprocessor"]=0
	df["xe_70"]=1
	df["xe_90"]=0	

df.drop(['model name','controller'],axis = 1,inplace = True)

pipe_lr=pickle.load(open('Compressor.pkl', 'rb'))

prediction = pipe_lr.predict(df)
flow = prediction[0]

st.subheader("PREDICTED RESULT")
st.write("THE FLOW IN CFM IS : ", flow)
