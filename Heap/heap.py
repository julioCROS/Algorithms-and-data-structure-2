from functools import total_ordering
import math
class MaxHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
    
    #Os metodos esquerda, direita e pai serão usados nos demais metodos do heap
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        pos_esquerda = 2*i
        return pos_esquerda


    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        pos_direita = (2*i) + 1
        return pos_direita

        

    def pai(self, i:int) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        pos_pai = math.floor(i/2)
        return pos_pai



    @property
    def pos_ultimo_item(self) -> int:
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):

        #maior_filho é inicializado com o da esqueda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_maior_filho = self.esquerda(pos_pai)      

        #obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]
                
        while pos_maior_filho <= self.pos_ultimo_item:
            
            #se a posição do filho a esquerda não for a ultima do vetor,
            #atualize, se necessario, o pos_maior_filho considerando o filho a direita
            if pos_maior_filho < self.pos_ultimo_item:
                pos_maior_filho = self.encontrarMaiorFilho(pos_pai)
                pass
                     
            #caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            #possua um valor maior que o de seus filhos, 
            # finaliza o while 
            #### SEU CODIGO AQUI ############
            if val_raiz_sub_arvore > self.arr_heap[self.esquerda(pos_pai)] and val_raiz_sub_arvore > self.arr_heap[self.direita(pos_pai)]:
                break
            #realize a troca conforme especificação
            #### SEU CODIGO AQUI ############
            self.arr_heap[pos_pai] = self.arr_heap[self.encontrarMaiorFilho(pos_pai)]

            #prepare as variáveis pos_pai e pos_maior_filho para a proxima iteração
            #substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = pos_maior_filho
            pos_maior_filho = self.encontrarMaiorFilho(pos_pai)

        #atualize a posição pos_pai apropriadamente
        self.arr_heap[self.pai(pos_maior_filho)] = val_raiz_sub_arvore
        
    def encontrarMaiorFilho(self,pos_pai):
        if 2*pos_pai + 1 < len(self.arr_heap):
            if self.arr_heap[self.esquerda(pos_pai)] >= self.arr_heap[self.direita(pos_pai)]:
                return self.esquerda(pos_pai)
            else :
                return self.direita(pos_pai)
        else:
            return self.esquerda(pos_pai)
    
    def retira_max(self):
        if len(self.arr_heap)<=1:
            return None

        maiorValor = self.arr_heap[1]
        pos_maiorValor = 1
        
        ## Faça a retirada do máximo conforme especificação/slides da aula teórica
        for i in range(1,len(self.arr_heap)):
            if self.arr_heap[i] > maiorValor:
                maiorValor = self.arr_heap[i];
                pos_maiorValor = i   
                    
        maximo = maiorValor
        self.arr_heap.pop(pos_maiorValor)
        
        ##Refazendo o heap     
        tamHeap = len(self.arr_heap)
        self.arr_heap.insert(1, self.arr_heap[tamHeap-1])
        self.arr_heap.pop(tamHeap)    
        for j in range(math.floor((tamHeap)/2)):
            for i in range(math.floor((tamHeap)/2) - 1, 0 , -1):
                array_final = self.arr_heap
                maiorPos = self.maiorDos2(i, tamHeap)
                if self.arr_heap[i] < self.arr_heap[maiorPos]:
                    aux = self.arr_heap[i]
                    self.arr_heap[i] = self.arr_heap[maiorPos]
                    self.arr_heap[maiorPos] = aux                   
        return maximo
 

    def maiorDos2(self, i, tamHeap):
        if (2*i + 1) < tamHeap:
            if self.arr_heap[2*i] >= self.arr_heap[2*i + 1]: 
                return 2*i
            else:
                return 2*i + 1
        else:
            return 2*i
        
    
    def insere(self, item):
        self.arr_heap.append(item)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)
        
        #substitua o "None" apropriadamente
        while pos_inserir > 1 and item > self.arr_heap[pai_pos_inserir]:
            
            #realiza a atualização (substitua os "None")
            self.arr_heap[pos_inserir] = self.arr_heap[pai_pos_inserir]

            #ajusta para a proxima iteração (substitua os None apropriadamente)
            pos_inserir = self.pai(pos_inserir)
            pai_pos_inserir = self.pai(pos_inserir)     
            
        #finalize o insere apropriadamente
        self.arr_heap[pos_inserir] = item
