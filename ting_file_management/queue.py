class Queue:
    def __init__(self):
        """Construtor da Classe Queue - definindo a estrutura como lista"""
        self._data = []

    def __len__(self):
        """Retornando o tamanho da lista"""
        return len(self._data)

    def enqueue(self, value):
        """Adicionando elementos a lista"""
        return self._data.append(value)

    def dequeue(self):
        """Removendo o primeiro elemento da lista"""
        return self._data.pop(0)

    def search(self, index):
        """Buscando o elemento pelo index"""
        if 0 <= index < len(self._data):
            return self._data[index]
        raise IndexError
