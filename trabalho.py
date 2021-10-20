# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:20:07 2021
@author: Diones Francisco Rossetto

Trabalho da disciplina de Análise de Dados com Python
"""

import pandas as pd
import numpy as np

dados = pd.read_table('breast-cancer-wisconsin.data', sep=',',
                      names=['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
                             'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size',
                             'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
                             'Mitoses', 'Class'], engine='python')
# mostra o dataframe gerado pela leitura
# print(type(dados))

# gera csv com os dados originais
dados.to_csv('breast-cancer-wisconsin-unprocessed.csv')

dados.info()
# conta quantidade de linhas iniciais
qtd_linhas_inicial = dados[dados.columns[0]].count()
print(f"Quantidade de linhas no inicio do processamento: {qtd_linhas_inicial}")

print('#### tratamento de dados ausentes ####')
# no exemplo de dados a serem processados nao ha dados ausentes, todavia, caso houver dados ausentes preenche com o valor undefined
dados_f = dados.fillna('undefined')

# verifica a soma de dados ausentes
soma_f = np.sum(dados_f.isnull())
print(f"\nSoma de dados ausentes por coluna:\n{soma_f}")

print("")
print('#### tratamento de dados duplicados ####')
tem_duplicados = dados.duplicated()
# print(tem_duplicados) # imprime as linhas informando se ha duplicacoes

# remove dados duplicados
dados_final = dados_f.drop_duplicates()
# imprime os dados finais, apos o tratamento
# print(dados_final)

# gera novo arquivo csv com os dados processados
dados_final.to_csv('breast-cancer-wisconsin-processed.csv')

# conta quantidade de linhas iniciais
qtd_linhas_final = dados_final[dados_final.columns[0]].count()
print(f"Quantidade de linhas no final do processamento: {qtd_linhas_final}")
