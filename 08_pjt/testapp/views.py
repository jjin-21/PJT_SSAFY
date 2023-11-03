from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from rest_framework.response import Response
from django.http import JsonResponse


df = pd.read_csv('testapp/data/test_data.CSV', encoding='cp949')

# Create your views here.
def a(request):
    data = df.to_dict('records')
    return JsonResponse({'data': data})


def b(request):
    df.fillna('NULL', inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'data': data})

def c(request):
    avg_age = df['나이'].dropna().mean()
    df['차이'] = abs(df['나이']-avg_age)
    df_10 = df.sort_values(by='차이').head(10)
    data = df_10.to_dict('records')
    return JsonResponse({'data': data})
