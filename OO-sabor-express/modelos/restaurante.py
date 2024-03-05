from modelos.avaliacao import Avaliacao

class Restaurante():
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria): 
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title() #title() - deixa a primeira letra maiúscula
        self._categoria = categoria.upper() #upper() - deixa todas as letras maiúsculas
        self._ativo = False 
        self._avaliacao=[]
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #Indica que estamos mexendo com um método especifico da classe
    def listar_restaurantes(cls): #cls é a classe
        '''Exibe uma lista formatada de todos os restaurantes.  "'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property #serve para alterar o modo de exibir determinada instância
    def ativo(self):
        ''''Retorna um símbolo indicando o estado de atividade do restaurante.'''
        return '✅' if self._ativo else '❌' #_ativo tem anderline pra fazer com que a instância não seja alterado pelo usuário
        
    def alternar_estado(self):
        ''''Alterna o estado de atividade do restaurante.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente,nota):
        ''''"""
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        '''
        if 0 <= 5:
            avaliacao=Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        ''''Calcula e retorna a média das avaliações do restaurante.'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)#soma todas as avaliações
        quantidade_notas = len(self._avaliacao)#pega todo o tamanho da lista
        media= round(soma_das_notas/quantidade_notas,1)#divide o total de avaliação pela pelo tamanho da lista, dando a média em uma casa decimal
        return media
    

    

