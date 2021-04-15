from functools import total_ordering
import math
class MinHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
        
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2*i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        return 2*i+1

    def pai(self, i) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        return math.floor(i/2)
        
    def folha(self, pos):
        if pos >= (len(self.arr_heap)/2) and pos <= len(self.arr_heap):
            return True
        return False
    
    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):
        if not pos_raiz_sub_arvore >= len(self.arr_heap)/2 and pos_raiz_sub_arvore <= len(self.arr_heap):
            
            if self.arr_heap[pos_raiz_sub_arvore] > self.arr_heap[self.esquerda(pos_raiz_sub_arvore)] or self.arr_heap[pos_raiz_sub_arvore] > self.arr_heap[self.direita(pos_raiz_sub_arvore)]:
                
                if self.arr_heap[self.esquerda(pos_raiz_sub_arvore)] < self.arr_heap[self.direita(pos_raiz_sub_arvore)]:
                    aux = self.arr_heap[pos_raiz_sub_arvore]
                    self.arr_heap[pos_raiz_sub_arvore] = self.arr_heap[self.esquerda(pos_raiz_sub_arvore)]
                    self.arr_heap[self.esquerda(pos_raiz_sub_arvore)] = aux
                    self.refaz(self.esquerda(pos_raiz_sub_arvore))
                    
                else:
                    aux = self.arr_heap[pos_raiz_sub_arvore]
                    self.arr_heap[pos_raiz_sub_arvore] = self.arr_heap[self.direita(pos_raiz_sub_arvore)]
                    self.arr_heap[self.direita(pos_raiz_sub_arvore)] = aux
                    self.refaz(self.esquerda(pos_raiz_sub_arvore))
                    self.refaz(self.direita(pos_raiz_sub_arvore))           

    def insere(self,item):
        self.arr_heap.append(item)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)
        while pos_inserir > 1 and item < self.arr_heap[pai_pos_inserir]:
            self.arr_heap[pos_inserir] = self.arr_heap[pai_pos_inserir]
            pos_inserir = self.pai(pos_inserir)
            pai_pos_inserir = self.pai(pos_inserir)     
        self.arr_heap[pos_inserir] = item

    def retira_min(self):
        if len(self.arr_heap) <= 1:
            return None
        
        menorValor = self.arr_heap[1]
        pos_menorValor = 1
        
        for i in range(1,len(self.arr_heap)):
            if self.arr_heap[i] < menorValor:
                menorValor = self.arr_heap[i];
                pos_menorValor = i   
                    
        minimo = menorValor
        self.arr_heap.pop(pos_menorValor)
        
        ##Refazendo o heap     
        tamHeap = len(self.arr_heap)
        self.arr_heap.insert(1, self.arr_heap[tamHeap-1])
        self.arr_heap.pop(tamHeap)    
        for j in range(math.floor((tamHeap)/2)):
            for i in range(math.floor((tamHeap)/2) - 1, 0 , -1):
                array_final = self.arr_heap
                menorPos = self.menorDos2(i, tamHeap)
                if self.arr_heap[i] > self.arr_heap[menorPos]:
                    aux = self.arr_heap[i]
                    self.arr_heap[i] = self.arr_heap[menorPos]
                    self.arr_heap[menorPos] = aux                   
        return minimo
    
    def menorDos2(self, i, tamHeap):
        if (2*i + 1) <= tamHeap:
            if self.arr_heap[2*i] <= self.arr_heap[2*i + 1]: 
                return 2*i
            else:
                return 2*i + 1
        else:
            return 2*i

    def __str__(self):
        return str(self.arr_heap)

    def __repr__(self):
        return str(self)