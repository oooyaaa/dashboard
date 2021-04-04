'''
Created on 2021. 3. 31.

@author: user
'''
import requests
from bs4 import BeautifulSoup
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os
from dashboard01.settings import STATIC_DIR, TEMPLATE_DIR
import pandas as pd
from folium import folium, plugins

from konlpy.tag._okt import Okt
from collections import Counter
import pytagcloud

def cctv_map():
    popup=[]
    data_lat_log=[]
    a_path='c:/hj/data/'
    df=pd.read_csv(os.path.join(a_path,'cctv.csv'),encoding='utf-8')
    print(df)
    for data in df.values: #필드빼고 값만 가져온다.
        if data[4]>0:
            popup.append(data[1])
            data_lat_log.append([data[10],data[11]])
            
    m=folium.Map([35.1803305,129.0516257],zoom_start=11)
    plugins.MarkerCluster(data_lat_log, popups=popup).add_to(m)
    m.save(os.path.join(TEMPLATE_DIR, 'map/map01.html'))

