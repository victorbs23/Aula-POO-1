class AnimalEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, novo_nome):
        self.nome = novo_nome


if __name__ == '__main__':
    animal1 = AnimalEstimacao('Toddy', 'cachorro', 5)
    animal2 = AnimalEstimacao ('Dex', 'gato', 7)
    retorno = animal1.get_nome()
    #print('Nome:', retorno)
    #print('Mensagem:', nome_objeto.nome_metodo())
    print('Nome:', animal1.get_nome())
    print('Nome:', animal2.get_nome())
    #nome_objeto.nome_metodo(novo_valor)
    animal1.set_nome('Rex')
    print('Nome alterado:', animal1.get_nome())
    print('Idade:', animal2.get_idade())