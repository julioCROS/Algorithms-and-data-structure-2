from typing import List, Dict
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho:"Vertice", peso:int):
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

	def obtem_vertice(self, valor_vertice) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def grau_separacao(self, valor_vertice_origem) -> Dict[Vertice,int]:
		distancia = {}
		visitou = {}
		queue = []
        
		vertice_inicial = self.obtem_vertice(valor_vertice_origem)
        
		if not vertice_inicial:
			return None
        
		for vertice in self.vertices.values():       
			distancia[vertice] = float("inf")
			visitou[vertice] = False
            
		queue.append(vertice_inicial)
		distancia[vertice_inicial] = 0

		while queue:           
			vertice_atual = queue.pop(0)
			for adjacente in vertice_atual.adjacencias.keys():
				if visitou[adjacente] == False:
					visitou[adjacente] = True
				if distancia[adjacente] == float("inf"):
					distancia[adjacente] = distancia[vertice_atual] + 1
					queue.append(adjacente)


		#print(distancia)
		return distancia