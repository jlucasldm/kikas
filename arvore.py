class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None


class Tree:
    def __init__(self):
        self.raiz = None

    def add(self, n, count, depth):
        if self.raiz is None:
            self.raiz = n
            return n
        elif self.raiz.esq is None:
            self.raiz.esq = n
            return n
        elif self.raiz.dir is None:
            self.raiz.dir = n
            return n
        else:
            if self.add_aux(self.raiz.esq, count, depth + 2, n):
                return n
            if self.add_aux(self.raiz.dir, count, depth + 2, n):
                return n
            # if self.raiz.esq is None:
            #     self.raiz.esq = n
            # elif self.raiz.dir is None:
            #     self.raiz.dir = n
            # else:
            #     self.add(r.esq, n)

    def add_aux(self, r, count, depth, n):
        if r.esq is None:
            r.esq = n
            return n
        elif r.dir is None:
            r.dir = n
            return n
        else:
            if self.level(count + 1) > depth + 1:
                if self.add_aux(r.esq, count, depth + 1, n):
                    return n
                elif self.add_aux(r.dir, count, depth + 1, n):
                    return n
            else:
                depth -= 1
                return 0


    def find(self, r, i, value):
        if self.raiz == value:
            return i
        else:
            if r.esq == value:
                print("Nó:", r.valor, "Esquerda:", r.esq.valor, "Direita:", r.dir.valor, "\n")
                return i + 1
            elif r.dir == value:
                print("Nó:", r.valor, "Esquerda:", r.esq.valor, "Direita:", r.dir.valor, "\n")
                return i + 1
            else:
                self.find(r.esq, i + 1, value)

    def level(self, n):
        for i in range(0, n+1):
            if n <= (2 ** i) - 1:
                return i


def main():
    print("Digite o número de linhas a serem lidas: ")
    num_linhas = int(input())

    print("Digite os valores dos da árvore: ")
    valores = list(map(int, input().split()))
    print("Valores dos nós recebidos, em uma lista: ", valores)
    t = Tree()

    print(t.level(11))
    print(t.level(12))

    depth = 0
    count = 0
    for i in valores:
        t.add(No(i), count, depth)
        count += 1

    encadeamento_nos = []

    for i in range(num_linhas - 1):
        encadeamento_nos.append(list(map(int, input().split())))
    print("Encadeamento1 dos nós recebido, em uma lista: ", encadeamento_nos)

    # [t.find(t.raiz, 0, i) for i in range(1, 8)]

    # lista = Lista()
    # lista.insert(encadeamento_nos[0][0])


if __name__ == '__main__':
    main()
