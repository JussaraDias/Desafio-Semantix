
import networkx as nx
import matplotlib.pyplot as plt
import PIL as gui



ref_arquivo = open("edges.dat","r")
g = nx.Graph()
for linha in ref_arquivo:
    valores = linha.split()
    g.add_node(valores[0])
    g.add_node(valores[1])
    g.add_edge(valores[0],valores[1])
 
    print(valores[0], valores[1])
    
print("Nodes of graph: ")
print(g.nodes())
print("Edges of graph: ")
print(g.edges())


hartford = nx.read_edgelist("edges.dat", create_using=nx.DiGraph(),nodetype=int)
N,K = hartford.order(), hartford.size()
avg_deg = float(K)/N
print ("Nodes: ", N)
print ("Edges: ", K)
print ("Average degree: ", avg_deg)

for p in nx.all_shortest_paths(g,source="63",target="59"):
    print (p)
print ("Densidade: ", nx.density(g))
print ("lenght: ", nx.shortest_path_length(g,source="63",target="59"))

print ("centrality: ", nx.closeness_centrality(g,"63"))

list_closeness_centrality=list(range(len(g)))
list_labels=list(range(len(g)))
labeldict = {}
for i in range(len(g)):
    print (i,": ",str(g.nodes()[i]) +"  -  "+ str(nx.closeness_centrality(g,g.nodes()[i])))
    list_closeness_centrality[i]=(round(nx.closeness_centrality(g,g.nodes()[i]),3),g.nodes()[i])
    
    list_labels[i]=str(g.nodes()[i])+"["+str(list_closeness_centrality[i])+"]"
    labeldict[g.nodes()[i]] = str(g.nodes()[i])+"["+str(list_closeness_centrality[i])+"]"
    
#for j in range(len(g)):
primeira_lista = list_closeness_centrality


# print(tuplas)
list_closeness_centrality.sort(key=lambda x: x[0])
print(list_closeness_centrality)

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, str(list_closeness_centrality), "Centralidade", 1)
    
nx.draw_random(g,labels=labeldict,node_size=1400,with_labels = True,width=0.2, font_size=10, alpha=0.4)
plt.savefig("simple_path.png") # save as png
plt.show() # displa


#"A distancia entre quaisquer dois vrrtices e o seu caminho mais curto"
#"O distanciamento de um dado vértice (V) é a soma de todas as distâncias de cada vértice até V"
#"Finalmente, a Proximidade de um vértice (V) é o inverso do distanciamento."
#"A primeira parte do desafio é classificar os vértices em um determinado gráfico pela sua proximidade (O gráfico é fornecido no arquivo anexado)"
#"Cada linha do arquivo consiste em dois nomes de vértice separados por um único espaço, o que representa uma vantagem entre esses dois nomes. A segunda parte do desafio é criar um servidor web RESTful com extremos de registrar bordas e exibir a centralidade do gráfico"
#"http://www.cl.cam.ac.uk/~cm542/teaching/2011/stna-pdfs/stna-lecture11.pdf"
#"http://www.python-course.eu/networkx.php"

ref_arquivo.close()
 
 
 