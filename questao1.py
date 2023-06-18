class No:
    def __init__(self, n):
        self.valor = n
        self.prox = None


class Lista:
    def __init__(self):
        self.head = None

    def insert(self, n):
        if self.head is None:
            self.head = No(n)
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = No(n)

    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.valor)
            temp = temp.prox

    # def last(self):
    #     temp = self.head
    #     while temp.prox is not None:
    #         temp = temp.prox
    #     return temp

    def find(self, n):
        temp = self.head
        while temp is not None:
            if temp.valor == n:
                return temp
            temp = temp.prox
        return None

    def detect(self):
        if self.head is not None:
            temp1 = self.head
            temp2 = self.head.prox
            while temp1 != temp2:
                if temp2.prox is None:
                    print("Ciclo não Detectado")
                    return 0
                else:
                    temp2 = temp2.prox

                if temp2.prox is None:
                    print("Ciclo não Detectado")
                    return 0
                else:
                    temp2 = temp2.prox

                temp1 = temp1.prox
                if temp2 is None:
                    print("Ciclo não Detectado")
                    return 0
            print("Ciclo Detectado")
            return 1


def main():
    print("Digite o número de linhas a serem lidas: ")
    num_linhas = int(input())

    print("Digite os valores dos nós: ")
    valores = list(map(int, input().split()))
    print("Valores dos nós recebidos, em uma lista: ", valores)

    encadeamento_nos = []

    print("Digite o encadeamento dos nós: ")
    for i in range(num_linhas - 1):
        encadeamento_nos.append(list(map(int, input().split())))
    print("Encadeamento dos nós recebido, em uma lista: ", encadeamento_nos)

    qntd_nos = len(valores)
    print("Quantidade de nós: ", qntd_nos)

    lista = Lista()
    lista.insert(encadeamento_nos[0][0])

    for j in encadeamento_nos:
        no = lista.find(j[0])
        if lista.find(j[1]) is None:
            lista.insert(j[1])
            print("No inserido: ", j[1])
        else:
            no.prox = lista.find(j[1])


    lista.detect()

if __name__ == '__main__':
    main()
