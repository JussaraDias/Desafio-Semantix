
import networkx as nx
import matplotlib.pyplot as plt
import ctypes

#Leitura do arquivo com os vértices

ref_arquivo = open("edges.dat","r")
g = nx.Graph()

# Inserção dos vertices em um grafo

for linha in ref_arquivo:
    valores = linha.split()
    g.add_node(valores[0])
    g.add_node(valores[1])
    g.add_edge(valores[0],valores[1])

# Função centralidade
    
def Centralidade(g,nx):
    list_closeness_centrality=list(range(len(g)))
    list_labels=list(range(len(g)))
    labeldict = {}
    for i in range(len(g)):
        list_closeness_centrality[i]=(round(nx.closeness_centrality(g,g.nodes()[i]),3),g.nodes()[i])
        list_labels[i]=str(g.nodes()[i])+"["+str(list_closeness_centrality[i])+"]"
        labeldict[g.nodes()[i]] = str(g.nodes()[i])+"["+str(list_closeness_centrality[i])+"]"
    return list_closeness_centrality,labeldict

# chamada da função centralidade

list_closeness_centrality,labeldict=Centralidade(g,nx)

# Criação da imagem do grafo gerado

list_closeness_centrality.sort(key=lambda x: x[0])
print(list_closeness_centrality)
nx.draw_random(g,labels=labeldict,node_size=1400,with_labels = True,width=0.2, font_size=10, alpha=0.4)
plt.savefig("centralidade.png") # salavar como as png
plt.show() 

# Criando de um panel para exibição do resultado da centralidade, em ordem crescente
ctypes.windll.user32.MessageBoxW(0, str(list_closeness_centrality), "Apresentação da centralidade em ordem crescente [(valor centralidade), (vértice)]", 1)

ref_arquivo.close()
 
 
 