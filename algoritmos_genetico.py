from random import random

class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        
class Individuo():
    def __init__(self,  espacos, valores, limit_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limit_espacos = limit_espacos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else :
                self.cromossomo.append("1")
    #fitness    
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
            if soma_espacos > self.limit_espacos:
                nota = 1
            self.nota_avaliacao = nota
            self.espaco_usado = soma_espacos
            
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        
        #cromossomos dos filhos
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filhos = [Individuo(self.espacos, self.valores, self.limit_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limit_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
    def mutacao(self, taxa_mutacao):
        print("Antes  %s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == "1":
                    self.cromossomo[i] = "0"
                else:
                    self.cromossomo[i] = "1"
        print ("Depois %s " % self.cromossomo)
        return self
    
class AlgoritmoGenetico():
    
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_populacao = 0
        
    def inicializa_populacao(self, espacos, valores, limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))
        self.melhor_populacao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse=True)

#função inicial
if __name__ == '__main__':
    #lista de produto 
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))

    espacos = []
    valores = []
    nomes = []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3
    
    #populacao inicial
    tamanho_populacao = 20
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.inicializa_populacao(espacos, valores, limite)
    for Individuo in ag.populacao:
        Individuo.avaliacao()
        print(Individuo.nota_avaliacao)
    ag.ordena_populacao()
    for i in range(ag.tamanho_populacao):
        print("*** Individuo %s ***\n" % i,
              "Espaços = %s \n" % str(ag.populacao[i].espacos),
              "Valores = %s \n" % str(ag.populacao[i].valores),
              "Cromossomo = %s \n" %  str(ag.populacao[i].cromossomo),
              "Nota = %s " %  ag.populacao[i].nota_avaliacao)
    