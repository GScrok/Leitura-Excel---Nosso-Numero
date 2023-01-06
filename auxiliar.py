import pandas as pd
import os


def definir_tables(excel):
    
    i=1
    pasta = 'excel'

    tables_certas = []

    tabela = pd.read_excel(os.path.join(pasta,excel),  sheet_name= 'Table 1')
    
    while(tabela.iloc[0,0] != 'Código de Histórico'):

        tables_certas.append(f"Table {i}")
        i += 1
        table_test = f'Table {i}'
        tabela = pd.read_excel(os.path.join(pasta,excel),  sheet_name= table_test)



    return tables_certas
