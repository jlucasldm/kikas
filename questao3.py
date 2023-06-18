class No:
    def __init__(self, n, up):
        self.id = n
        self.up = up
        self.prox = None


class Lista:
    def __init__(self):
        self.head = None

    def insert(self, n):
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.prox is not None:
                temp = temp.prox
            temp.prox = n

    def remove(self, n):
        if self.head is not None:
            temp = self.head
            if temp.id == n:
                self.head = temp.prox
                return 1
            while temp.prox is not None:
                if temp.prox.id == n:
                    temp.prox = temp.prox.prox
                    return 1
                temp = temp.prox
        return 0

    def show(self):
        temp = self.head

        outputid = ""
        outputUp = ""

        while temp is not None:
            outputid += f'{temp.id} '
            outputUp += f'{temp.up} '
            temp = temp.prox
        print(outputid[:-1])
        print(outputUp[:-1])

    def find(self, n):
        temp = self.head
        while temp is not None:
            if temp.id == n:
                return temp
            temp = temp.prox
        return None

def main():
    print("Digite o número de linhas a serem lidas: ")
    numLinhas = int(input())

    print("Digite o quantum e máximo de UP da CPU: ")
    quantum, maxUP = map(int, input().split())

    print("Digite os identificadores dos processos: ")
    identificadores = list(map(int, input().split()))

    print("Digite os UP's necessários para cada processo: ")
    UPs = list(map(int, input().split()))

    lista = Lista()
    processado = 0

    for i in range(len(identificadores)):
        lista.insert(No(identificadores[i], UPs[i]))

    while processado < maxUP:
        no = lista.head

        if maxUP - processado <= quantum:
            quantum = maxUP - processado

        if no.up >= quantum:
            no.up -= quantum
            processado += quantum
            if no.up == 0:
                lista.remove(no.id)
            else:
                lista.remove(no.id)
                noInsert = No(no.id, no.up)
                lista.insert(noInsert)
        else:
            processado += no.up
            lista.remove(no.id)

    lista.show()

if __name__ == '__main__':
    main()
