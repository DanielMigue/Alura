import os

restaurantes = [{'nome': 'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana',
                 'ativo':True},
                {'nome': 'Cantina','categoria':'Italiano','ativo':False}                  
                ]
def exibir_nome_do_programa():
    ''''Essa função é responsável por mostrar o nome do programa estilizado'''
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
''')
    


def exibir_opcoes():
    '''Mostra as opções que usuário devera escolher no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Encerra o aplicativo com uma mensagem de finalização'''
    exibir_subtitulo('Finalizando o app\n')

def opcao_invalida():
    ''''Exibe a mensagem inválida
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Pede ao usuário uma tecla para voltar ao menu principal
    Outputs:
    -Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    '''Estiliza e exibe o subtítulo na tela
    Inputs:
    -texto: str - O texto do subtítulo
    '''
    os.system('cls') #limpa o programa
    linha = '*' * (len(texto)) #len = tamanho
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    #antes do código, é feita uma breve "docstrings"
    '''
    Essa função é responsável por cadastrar um restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    -Adiciona um novo restaurante a lista de restaurantes
    
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi  cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''''
    Lista os restaurantes presentes na lista

    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') #ljust deixa x caracteres para direita

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Desativa ou ativa o restaurante alterando o estado

    Outputs:
    -Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')    
            
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Socilita ao usuário a escolha de umas das opções e executa as funções'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__': #Se esse aqruivo faça com que o o main execute...
    main()    