from typing import List

class Node:
    def __init__(self, key, left:"Node"=None, right:"Node"=None):
        self.key = key
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        """
        if self.left:
            self.left.print_tree()
        print(self.key, end=" ")
        if self.right:
            self.right.print_tree()


    def insert(self, key) -> bool:
        """
        Insere um nodo na árvore que a chave "key"
        """
        if key < self.key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = Node(key)
                return True
        elif key > self.key:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = Node(key)
                return True
        else:
            return False


    def search(self, key) -> bool:
        """
        Retorna verdadeiro caso a chave `key` exista na árvore
        """
        if key < self.key:
            if self.left:
                return self.left.search(key)
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        else:
            return True
        return False


    def to_sorted_array(self, arr_result:List =None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.
        """
        if(arr_result == None):
            arr_result = []

        if self.left:
            self.left.to_sorted_array(arr_result)

        arr_result.append(self.key)

        if self.right:
            self.right.to_sorted_array(arr_result)
        return arr_result

    def max_depth(self,current_max_depth:int=0) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        current_max_depth = current_max_depth +1
        val_left,val_right = current_max_depth,current_max_depth

        if self.left:
            val_left = self.left.max_depth(current_max_depth)
        if self.right:
            val_right = self.right.max_depth(current_max_depth)

        if(val_left>val_right):
            return val_left
        else:
            return val_right

    def position_node(self, key, current_position:int = 1) -> int:
        """
            Retorna a posição do nodo desejado na árvore
            current_position: representa a posição da árvore naquele momento
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        return 0
    def is_balanced(self) -> bool:
        """
            Retorna true caso a árvore seja balanceada, false caso não seja
        """
        d1 = 0
        d2 = 0
        if self.left:
            retorno = self.left.is_balanced()
            if not retorno:
                return False
   
        if self.right:
            retorno = self.right.is_balanced()
            if not retorno:
                return False
            
        if self.left:
            d1 = self.left.max_depth()
        if self.right:
            d2 = self.right.max_depth() 
        
        if abs(d1 - d2) > 1:
            return False
        return True

    def sorted_array_to_balanced_tree(self, array:List, start:int, end:int) -> "Node":
        if (start > end):
            return None
        
        pos_raiz_sub_arvore = int(len(array)/2)        
        raiz_sub_arvore = Node(array[int(pos_raiz_sub_arvore)])
        
        if raiz_sub_arvore.left:
            raiz_sub_arvore.left = self.sorted_array_to_balanced_tree(array[:int(len(array)/2)], start, int(pos_raiz_sub_arvore))
        if raiz_sub_arvore.right:
            raiz_sub_arvore.right = self.sorted_array_to_balanced_tree(array[int(len(array)/2)+1:], int(pos_raiz_sub_arvore) + 1, end)

        return raiz_sub_arvore

    def to_balanced_tree(self):

        array = self.to_sorted_array()

        return self.sorted_array_to_balanced_tree(array, 0, len(array)-1)
