import requests
import pandas as pd
import datetime
import numpy as np
import pickle as pk
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from flask import Flask , render_template , current_app, url_for
from APPLE import APPL_STOCK


app = Flask(__name__)

def get_object():
    if not hasattr(current_app, 'APPL'):
        current_app.APPL = APPL_STOCK()
    return current_app.APPL

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/apple')
def hello():
    # APPL = get_object()
    # combine = list(zip(APPL.forecasted_dates,APPL.forecasted_data))
    a = [1,2,3,4,5]
    b = [2,3,5,6,7]
    combine = list(zip(a,b))
    Forecasting_DATA = url_for('static', filename='APPL_FORECASTING_DATA.png')
    DATASET = url_for('static', filename='Fetched_APPL_DATA.jpeg')
    WINDOWED_DATA = url_for('static', filename='Windowed_APPL_data.jpeg')
    TEST_TRAIN_SPLIT = url_for('static', filename='APPL_PLOTTED_DATA.png')
    PREDICTED_DATA = url_for('static', filename='APPL_PREDICTED_DATA.png')
    return render_template('second_page.html',combine=combine,Forecasting_DATA=Forecasting_DATA,DATASET=DATASET,WINDOWED_DATA=WINDOWED_DATA,TEST_TRAIN_DATA = TEST_TRAIN_SPLIT,PREDICTED_DATA=PREDICTED_DATA)

if __name__ == "__main__":
    app.run(debug=True)