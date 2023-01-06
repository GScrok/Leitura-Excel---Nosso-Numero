import pandas as pd
import auxiliar
import chamada_excel
import os
import math



pago = []
n_pago = []

pasta = 'excel'
arquivos = chamada_excel.pega_excel()


for excel in arquivos:
    nomes_planilhas = auxiliar.definir_tables(excel)


    for i in nomes_planilhas:
        
        if i == 'Table 1':
            tabela = pd.read_excel(os.path.join(pasta,excel), usecols=[0,1,7,8], skiprows= 6,header=0)

            tabela = tabela.dropna(axis=0)  
        
            for i,j in tabela.iterrows():
                if i == len(tabela):
                    continue
                
                
                if tabela.iloc[i, 2] != 'L':
                    cart = tabela.iloc[i, 0]
                    cart = "{:.0f}".format(cart)

                    nosso_numero = tabela.iloc[i, 1]
                    nosso_numero = "{:09.0f}".format(nosso_numero)
                    
                    #data_paga = tabela.iloc[i, 2]
                    #data_paga = data_paga.strftime("%Y-%m-%d")
                    
                    n_pago.append({
                        'nosso numero':f"{cart}/{nosso_numero}",
                        'movimentacao':tabela.iloc[i, 1],
                        #'data_paga': data_paga
                    })
                    continue

                cart = tabela.iloc[i, 0]
                cart = "{:.0f}".format(cart)
                
                nosso_numero = tabela.iloc[i, 1]
                resto_nosso_numero = nosso_numero % 10
                nosso_numero = nosso_numero / 10

                nosso_numero = math.trunc(nosso_numero)
                nosso_numero_str = "{:08}".format(nosso_numero)


                resto_nosso_numero_str = "{:.0f}".format(resto_nosso_numero)
                

                data_paga = tabela.iloc[i, 3]
                data_paga = data_paga.strftime("%Y-%m-%d")
                
                pago.append({
                    'nosso numero':f"{cart}/{nosso_numero_str}-{resto_nosso_numero_str}",
                    'movimentacao':tabela.iloc[i, 2],
                    'data_paga': data_paga
            })
            continue 

        tabela = pd.read_excel(os.path.join(pasta,excel), sheet_name= i,usecols=[0,1,7,8])

        tabela = tabela.dropna(axis=0)  
    
        for i,j in tabela.iterrows():
                if i == len(tabela):
                    continue
                
                if tabela.iloc[i, 2] != 'L':
                    
                    cart = tabela.iloc[i, 0]
                    cart = "{:.0f}".format(cart)
                    
                    nosso_numero = tabela.iloc[i, 1]
                    nosso_numero = "{:09.0f}".format(nosso_numero)
                    
                    #data_paga = tabela.iloc[i, 2]
                    #data_paga = data_paga.strftime("%Y-%m-%d")
                    
                    n_pago.append({
                        'nosso numero':f"{cart}/{nosso_numero}",
                        'movimentacao':tabela.iloc[i, 1],
                        #'data_paga': data_paga
                    })
                    continue

                cart = tabela.iloc[i, 0]
                cart = "{:.0f}".format(cart)
                
                nosso_numero = tabela.iloc[i, 1]
                resto_nosso_numero = nosso_numero % 10
                nosso_numero = nosso_numero / 10

                nosso_numero = math.trunc(nosso_numero)
                nosso_numero_str = "{:08}".format(nosso_numero)


                resto_nosso_numero_str = "{:.0f}".format(resto_nosso_numero)
                

                data_paga = tabela.iloc[i, 3]
                data_paga = data_paga.strftime("%Y-%m-%d")
                
                pago.append({
                    'nosso numero':f"{cart}/{nosso_numero_str}-{resto_nosso_numero_str}",
                    'movimentacao':tabela.iloc[i, 2],
                    'data_paga': data_paga
            })

    print(pago)

