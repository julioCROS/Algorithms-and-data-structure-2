from typing import List
class NoTrie:
	def __init__(self, letra:str="", fim_palavra:bool=False):
		self.filhos = dict()
		self.fim_palavra = fim_palavra
		self.letra = letra

        
	def insere(self, letra:str, fim_palavra:bool):
		self.filhos[letra] = NoTrie(letra, fim_palavra)

	def existe_letra(self, letra:str) -> bool:
		return letra in self.filhos

	def obtem_no_filho(self,letra:str) -> "NoTrie":
		return self.filhos[letra]

	def nos_filhos(self) -> List[str]:
		return self.filhos.keys()

class Trie:
	def __init__(self, raiz:NoTrie=None):
		if not raiz:
			raiz = NoTrie()
		self.raiz = raiz

	def insere(self, palavra:str):
		no_atual = self.raiz
		for i,letra in enumerate(palavra):
			if not no_atual.existe_letra(letra):
				no_atual.insere(letra, i == len(palavra)-1)
			no_atual = no_atual.obtem_no_filho(letra)
		no_atual.fim_palavra = True

	def pesquisa(self, palavra:str) -> bool:
		self.raiz_inicial = NoTrie()
		self.raiz_inicial = self.raiz
		listaPalavra = list(palavra)
		tamPalavra = len(palavra)
		i = 0
        
		resultado = self.raiz.existe_letra(listaPalavra[i])
		while resultado == True:
			if tamPalavra == 1 and resultado == True:
				return True
			self.raiz = self.raiz.obtem_no_filho(listaPalavra[i])
			if i == (tamPalavra-1) and self.raiz.fim_palavra: 
				self.raiz = self.raiz_inicial
				return True
			if i + 1 >= tamPalavra:
				self.raiz = self.raiz_inicial
				return False
			resultado = listaPalavra[i + 1] in self.raiz.filhos
			i = i + 1
		if resultado == False:
			self.raiz = self.raiz_inicial
			return False


	def preditor(self, prefixo_palavra:str) -> List[str]:		
		#obtem a ultima letra do prefixo
		no_ult_letra_prefixo = self.raiz
		for letra in prefixo_palavra:
			if not no_ult_letra_prefixo.existe_letra(letra):
				return []

			no_ult_letra_prefixo = no_ult_letra_prefixo.obtem_no_filho(letra)
			prefixo_palavra = prefixo_palavra + letra

		#por meio da ultima letra do prefixo, faz a predição das possiveis palavras
		#Para isso, você poderá precisar de fazer um método recursivo
		### SEU Código aqui

		return []

