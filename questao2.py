class No:
    def __init__(self, n):
        self.valor = n
        self.prox = None

    def show(self):
        return f'{self.valor}'


class Pilha:
    def __init__(self):
        self.head = None

    def push(self, n):
        if self.head is None:
            self.head = n
        else:
            n.prox = self.head
            self.head = n

    def pop(self):
        if self.head is None:
            print("Pilha vazia")
        else:
            temp = self.head
            self.head = self.head.prox
            del temp

    def retirar(self):
        self.head = self.head.prox

    def apagar(self):
        self.head = None

    def show(self):
        print('Pilha:')
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(f'{temp.show()}')
                temp = temp.prox

    def tam(self):
        if self.head is None:
            print('Pilha Vazia')
            return 0

        i = 0
        temp = self.head
        while temp is not None:
            i += 1
            temp = temp.prox

        print(f'O tamanho da pilha é {i}')

    def topo(self):
        return f'{self.head.valor}'

    def inserev(self, n):
        if self.head is None:
            self.head = n
        elif n.valor == ")" and self.head.valor == "(":
            return f'{self.retirar()}'
        elif n.valor == "]" and self.head.valor == "[":
            return f'{self.retirar()}'
        elif n.valor == "}" and self.head.valor == "{":
            return f'{self.retirar()}'
        else:
            n.prox = self.head
            self.head = n

    def verifica(self):
        if self.head is None:
            print("Válida")
        else:
            print("Inválida")


def main():
    print("Digite a expressão a ser validada: ")
    expressao = input()

    pilha = Pilha()

    for i in expressao:
        if i == "(" or i == "[" or i == "{" or \
                i == ")" or i == "]" or i == "}":
            pilha.inserev(No(i))

    pilha.verifica()

if __name__ == '__main__':
    main()
