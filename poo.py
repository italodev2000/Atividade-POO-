class Atividade:
    '''Classe que contenha dois atributos e 
    dois métodos'''

    def informar(self, nome, idade):
        self.nome = nome
        self.idade = idade

        print(f"meu nome é {nome} e tenho {idade} de idade")

    def estudar(self, materia):
        self.materia = materia

        print(
            f"O aluno {self.nome} irá estudar o conteúdo de {self.materia}com {self.idade}")
