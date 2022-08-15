# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 02:02:25 2022

@author: teladmin
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())