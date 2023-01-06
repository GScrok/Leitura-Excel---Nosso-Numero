import pandas as pd
import os

def pega_excel():
    caminho_excel = 'excel'
    arquivo = []

    for file in os.listdir(caminho_excel):
        arquivo.append(file)

    return arquivo