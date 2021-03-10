from functools import total_ordering
from datetime import datetime
from heap import MaxHeap

class Cliente:
    def __init__(self,nome:str, idade:int, necessidades_especiais:bool):
        self.nome = nome
        self.idade = idade
        self.necessidades_especiais = necessidades_especiais

    def __str__(self):
        return self.nome
    def __repr__(self):
        return str(self)

@total_ordering
class PrioridadeCliente:
    ultima_ordem_chegada = 0
    def __init__(self, cliente:Cliente, prioridade:str):
        self.cliente = cliente
        self.prioridade = prioridade
        PrioridadeCliente.ultima_ordem_chegada += 1
        self.ordem_chegada = PrioridadeCliente.ultima_ordem_chegada

    def __eq__(self, outro:"PrioridadeCliente") ->bool:
        return (self.prioridade == outro.prioridade)

    def __lt__(self,  outro:"PrioridadeCliente") -> bool:
        if self.prioridade != outro.prioridade : 
            return (self.prioridade < outro.prioridade)
        else:
            return (self.ordem_chegada > outro.ordem_chegada)

    def __str__(self):
        return f"Cliente: {self.cliente} Prioridade: {self.prioridade}"

    def __repr__(self):
        return str(self)

class CaixaBanco:
    def __init__(self,nome_banco:str):
        self.fila_prioridade = MaxHeap()
        self.nome_banco = nome_banco
        
    def adiciona_cliente(self, cliente:Cliente):
        if cliente.idade > 80:
            prioridade = 3
            p_cliente = PrioridadeCliente(cliente, prioridade)
        elif (cliente.idade > 60 and cliente.idade <= 80) or cliente.necessidades_especiais == True:
            prioridade = 2
            p_cliente = PrioridadeCliente(cliente, prioridade)
        else:
            prioridade = 1
            p_cliente = PrioridadeCliente(cliente, prioridade)
            
        self.fila_prioridade.insere(p_cliente)
        pass

    def proximo_cliente(self) -> Cliente:
        return print(f"Retirado: {self.fila_prioridade.retira_max()}")

    def __str__(self):
        return f"Banco: {self.nome_banco} Fila: {self.fila_prioridade}"

    def __repr__(self):
        return str(self)
