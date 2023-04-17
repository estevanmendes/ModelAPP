import streamlit as st
import pandas as pd
from ast import literal_eval
import numpy as np
import random

def load_metrics(path):
    with open(path,'r') as f:
        data=f.read()
    metrics=literal_eval(data)
    return metrics

def format_metrics(data):
    metrics_config=[]
    for k,v in data.items():
        metrics_config.append({'label':k,'value':v['mean'],'delta':'+/- '+str(v['std']),'delta_color':'normal'})
    return metrics_config

def display_metrics(metrics_config):
    cols=st.columns(len(metrics_config))
    for index,col in enumerate(cols):
        col.metric(**metrics_config[index])


def upload_files_parallel(filenames):
    cols=st.columns(len(filenames))
    for index,col in enumerate(cols):
        col.file_uploader(filenames[index])

def upload_files(filenames):
    for file in filenames:
        st.file_uploader(file)

def input_values(variables,sequence_size,random_value=False):
    cols=st.columns(len(variables))
    for index,col in enumerate(cols):
        col.write(f'{variables[index]}')

        for row in range(sequence_size):
            value=None
            if random_value:
                value=str(random.uniform(-2,2))
            col.text_input(label=variables[index]+str(row+1),label_visibility='hidden',value=value)


def load_model(path):
    with open(path,'rb') as f:
        model=f.read()

    return model
    

def download_model(path):
    st.markdown("# Download the Model")
    cols=st.columns(3)
    cols[1].download_button('Model.h5',load_model(path))

def get_classification():
    _,col,_=st.columns(3)
    col.button('Get Classification')

st.set_page_config(
    page_title="Driver Behaviour Classification",
    page_icon="",
)


st.markdown("# Model Metrics")
metrics=load_metrics('metrics.txt')
metrics_formated=format_metrics(metrics)
display_metrics(metrics_formated)


download_model('metrics.txt')



st.write("# Tryout the model ")

variables_to_upload=['AccX','AccY','AccZ','GyroX','GyroY','GyroZ']

if st.button('Random Inputs'):

    input_values(variables_to_upload,10,random_value=True)
    get_classification()

if st.button('InputManually'):

    input_values(variables_to_upload,10)
    get_classification()

if st.button('Input File'):

    upload_files(variables_to_upload)
    get_classification()

st.sidebar.success("Model usage")

st.markdown(
    """

"""
)