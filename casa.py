class Casa:

    def limpar(self, nome, comodo, produto_limpeza):
        self.comodo = comodo
        self.produto_limpeza = produto_limpeza
        self.nome = nome
        print(f"""Hoje {self.nome} vai limpar a casa e vai começar pela {self.comodo}
        e vai usar o produto {self.produto_limpeza}""")

    def enxugar(self,):
        print(f"{self.nome} enxugou a {self.comodo} com o pano")
