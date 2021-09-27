# -*- coding: utf-8 -*-
"""Tratamento de dados Mortalidade

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VdOmBuUm1B4rAiTwdwN8davO6FTi7Kf3
"""

import pandas as pd
from datetime import date
import numpy as np

df = pd.read_csv("DOMAT20.csv", dtype=str, usecols=["DTOBITO", "NATURAL", "DTNASC"])

df.head()

df.dtypes

df[["DTOBITO", "DTNASC"]] = df[["DTOBITO", "DTNASC"]].apply(pd.to_datetime, errors='coerce', format='%d%m%Y')

print('Analise de Qualidade DTOBITO: ' + str((df['DTOBITO'].isnull().sum() / df.shape[0]) * 100))

print('Analise de Qualidade DTNASC: ' + str((df['DTNASC'].isnull().sum() / df.shape[0]) * 100))

print('Analise de Qualidade NATURAL: ' + str((((df['NATURAL'] == '999').sum() + df['NATURAL'].isnull().sum()) / df.shape[0]) * 100))

arr_brasil = []
arr_estrang = []
aux = ''

for i in range(len(df['NATURAL'])):
  if (str(df['NATURAL'][0]) == '8'):
    arr_brasil.append(str(df['NATURAL'][0]))
  else:
    aux = str(df['NATURAL'][0])
    if (aux != 'nan'):
      arr_estrang.append(str(df['NATURAL'][0]))

arr_estados = []

for i in range(len(arr_brasil)):
  arr_estados.append(arr_brasil[i][1:3])


df['PAIS'] = '';
df['ESTADO'] = '';


dic_est = {'11':'RO', '12':'AC', '13':'AM', '14':'RR', '15':'PA', '16':'AP', 'TO':'17',
           '21':'MA', '22':'PI', '23':'CE', '24':'RN', '25':'PB', '26':'PE', '27':'AL', '28':'SE','29':'BA',
           '31':'MG', '32':'ES', '33':'RJ', '35':'SP',
           '41':'PR', '42':'SC', '43':'RS',
           '50':'MS', '51':'MT', '52':'GO', '53':'DF'}


for i in range(len(df['PAIS'])):
  if (str(df['NATURAL'][i])[0] == '8'):
    df['PAIS'][i] = 'Brasil'    
    for elem in dic_est.keys():
      if (elem == str(df['NATURAL'][i])[1:3]):
        df['ESTADO'][i] = dic_est[elem]
  elif (str(df['NATURAL'][i]) == '33.0'):
    df['PAIS'][i] = 'Aruba'
  elif (str(df['NATURAL'][i]) == '109.0'):
    df['PAIS'][i] = 'Ilhas do Canal'
  elif (str(df['NATURAL'][i]) == '33.0'):
    df['PAIS'][i] = 'Hong-Kong'
  if (str(df['NATURAL'][i]) == 'nan'):
    df['PAIS'][i] = 'Não informado'

print(df.head())