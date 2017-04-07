# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import networkx as nx


ref_arquivo = open("edges.dat","r")
g = nx.Graph()
for linha in ref_arquivo:
    valores = linha.split()
    g.add_node(valores[0])
    g.add_node(valores[1])
    g.add_edge(valores[0],valores[1])
    g.add_weighted_edges_from(1)
    print(valores[0], valores[1])
    
print("Nodes of graph: ")
print(g.nodes())
print("Edges of graph: ")
print(g.edges())

"A distância entre quaisquer dois vértices é o seu caminho mais curto;"

"O distanciamento de um dado vértice (V) é a soma de todas as distâncias de cada vértice até “V”."
"Finalmente, a Proximidade de um vértice (V) é o inverso do distanciamento."
"A primeira parte do desafio é classificar os vértices em um determinado gráfico pela sua proximidade (O gráfico é fornecido no arquivo anexado). "
"Cada linha do arquivo consiste em dois nomes de vértice separados por um único espaço, o que representa uma vantagem entre esses dois nomes. A segunda parte do desafio é criar um servidor web RESTful com extremos de registrar bordas e exibir a centralidade do gráfico."
"http://www.cl.cam.ac.uk/~cm542/teaching/2011/stna-pdfs/stna-lecture11.pdf
"http://www.python-course.eu/networkx.php

ref_arquivo.close()
 
 
 