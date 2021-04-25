class Variavel:

    def __init__(self, posicao_inicial, tamanho, codigo, descricao):
        # Modificacao
        self.posicao_inicial = int(posicao_inicial) - 1
        self.tamanho = int(tamanho)
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = {}

    def add_categoria(self, categoria):
        # categoria = dict {'categoria_tipo': tipo, 'categoria_descricao_tipo': descricao}
        self.categoria[categoria.get('categoria_tipo')] = categoria.get('categoria_descricao_tipo')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
