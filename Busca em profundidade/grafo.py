from typing import List, Dict
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho, peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)

	def obtem_vertice(self, valor_vertice:str) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def e_um_dag_dfs(self, vertice:Vertice, visitados:Dict[Vertice,int]) -> bool:
		"""
		vertice: vertice a ser explorado
		visitados: Dicionário que mapeia, cada vertice explorado. 
				Se visitados[vertice]==1: o vértice ainda sendo explorado ou foi encontrado um ciclo neste vertice explorado
				Se visitados[vertice]==2: o vértice já foi explorado totalmente e não foi encontrado ciclo durante a exploração
		"""
		visitados[vertice] = 1
		for proxVertice in vertice.adjacencias.keys():
			#print(f"Valor: {proxVertice.valor} ")
			if proxVertice not in visitados:            
				if not self.e_um_dag_dfs(proxVertice, visitados):                    
					return False
			elif visitados[proxVertice] == 1:                
				return False       
		visitados[vertice] = 2  
		return True    

	def e_um_dag(self) -> bool:
		visitados = {}
		for vertice in self.vertices: 
			visitados[vertice] = 0  
		for vertice in self.vertices.values():          
			if not self.e_um_dag_dfs(vertice, visitados):
				print("Resultado : False") 
				return False   
		print("Resultado : True")             
		return True

	def visitarVertice(self, vertice, visita, lista):      
		visita[vertice.obtem_valor()] = True            
		for adjacente in vertice.adjacencias.keys():
			if not visita[adjacente.valor]:
				self.visitarVertice(adjacente, visita, lista)
		lista.append(vertice.obtem_valor())        

	def ordenacao_topologica(self) -> List:
		visita = {}
		lista = []      
		for vertice in self.vertices: 
			visita[vertice] = False              
		for vertice in self.vertices.values():           
			if not visita[vertice.valor]:
				self.visitarVertice(vertice, visita, lista)
		lista.reverse()
		print(f" Lista da ordenação topológica: {lista}")        
		return lista