# Como avaliação final da disciplina, desenvolva um sistema para controlar o estoque de uma empresa. Deve-se utilizar a linguagem de programação Python e contemplar as seguintes funcionalidades:

# a) Exibir menu para o usuário selecionar as funcionalidades do sistema;

# b) Cadastrar produtos (nome produto, quantidade em estoque, preço de custo e preço de venda);

# c) Permitir alteração dos dados cadastrais do produto (nome, preço de custo e preço de venda);

# d) Permitir exclusão de um produto cadastrado;

# e) Registrar entrada (compra) de produtos no estoque (adicionar quantidade em estoque);

# f) Registar saída (venda) de produtos no estoque (reduzir quantidade em estoque);

# g) Consultar a quantidade de produtos em estoque (pesquisa de um único produto ou todos);

# h) Consultar o valor total (em R$) do preço de custo e preço de venda de todo o estoque (soma total dos valores);

# i) Persistir os dados. Os dados devem ser salvos e carregados a partir de um arquivo texto.

from module_function import * #importando pacotes de funções do sistema (pacote módulos)

import json #importando pacote json (preferi trabalhar com ele, pois possui estruturas de dados 
#similares às de python, auxiliando na formatação do arquivo.)

import os #importando pacote os (verifica a existencia do meu arquivo.json e cria ele, caso não o encontre em nenhum diretório  do meu computador.)

from module_menu import * #importando pacotes de funções do menu (pacote modeulos_do_menu)

'''
Declaração de variável que vai receber uma f'strings, com o método os.getcwd. Esse método é o 
responsável por vasculhar em cada diretório do meu computador a existência do paramêtro que é passado 
pra ele, qual seja, o \arquivo.json.
'''
file = f'{os.getcwd()}/arquivo.json' 

'''
Método if para comparar uma negação, utilizando o método os.path.isfile(), que vai verificar se o paramêtro 
(caminho da variável file) passado é um arquivo existente. No caso, nós estamos negando a condição, 
assim, se o caminho não corresponder a um arquivo existente, executa-se o bloco abaixo, que vai ser 
responsável por abrir o arquivo em módo write(escrita), e dar um dumps de um array vázio (passa um dado
em json para o arquivo). O array vázio é necessário, em virtude da estrutura de dados do json. Depois,
o arquivo é fechado.  
'''
if not os.path.isfile(file): 
    with open('arquivo.json', 'w') as f: 
        
        f.write(json.dumps([]))

        f.close() 


estoque = open('arquivo.json') 
'''Abre o arquivo.json criado. é um arquivo IO (in and out). Ao abrir um, a variável atrelada a ele não
recebe, de cara, seus dados, mas sim um conjunto de bytes indicando a sua localização na memória. Isso
porque um arquivo é, naturalmente, uma estrutura I/O, que recebe e exporta dados.
Após a abertura do arquiv, é necessário ler os dados existentes no caminho apontado por ele, para ter 
um retorno dos dados que estão registrados lá. Para isso, atribui=se nova var, que vai receber a leitura
do arquivo. Mais tarde, é preciso converter os dados lidos do arquivo em um objeto python, usando jsonloads,
pois até o momento esses dados estão em formato json, em virtude do dumps feito anteriormente. Ao final, 
fecha-se o arquivo.'''

estoque_como_string = estoque.read()

estoque_atual = json.loads(estoque_como_string) 

estoque.close() 

while True:
    '''
    Estrutura de repetição que ficará em loop infinito enquanto o usuário não digitar o comando de saída.
    opcao: recebe def menu(), que é a função responsável por listar as opções do nosso menu.
    '''
    opcao = menu(['Cadastrar produtos no estoque.', 'Alterar informações dos produtos cadastrados no estoque.',
     'Excluir um produto do estoque.', 'Registrar entrada de produtos no estoque.', 'Registrar saídas de produtos no estoque.',
     'Consultar informações dos produtos em estoque.', 'Inserir aumento de preço','Consultar o estoque', 
     'Sair do sistema'])

    '''
    Além de a var opcao receber a função, ela vai exigir um input, que deve contar um número inteiro 
    entre 1 e 9, para acessar uma funcionalidade do nosso sistema. Para cada uma das funcionalidades
    é passada a função modularizada correspondente à ela. Após executada a função, é necessário fazer
    um dumps no parâmetro que passamos para a função referente à opção, atribuindo seu resultado à outra
    variável, que vai ser responsável por conter os dados como objeto json, permitindo a escrita no nosso
    arquivo de estoque.
    Por fim, basta utilizar a def escreve_arquivo(aux,aux1): para escrever os dados alterados e 
    incluídos no nosso controle de estoque. Os parâmetros necessários são o nome do arquivo, e a variável
    que contem os dados em formato json.
    Com exceção da opcao 1, todas as demais receberam a def cabeçalho(), para formatar o seu cabeçalho.
    '''

    if opcao == 1:
        cabeçalho('CADASTRO DE PRODUTOS')
        cadastrar_produto(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    
    elif opcao == 2:
        cabeçalho('ALTERAÇÃO DE DADOS CADASTRAIS')
        alterar_dados(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)    
    
    elif opcao == 3:
        cabeçalho('EXCLUIR PRODUTO')
        excluir_produto(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    
    elif opcao == 4:
        cabeçalho('REGISTRAR ENTRADA DE ESTOQUE')
        registro_entrada(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    
    elif opcao == 5:
        cabeçalho('REGISTRAR SAÍDA DE ESTOQUE')
        registro_saida(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    
    elif opcao == 6:
        cabeçalho('INFORMAÇÕES DE ESTOQUE')
        somar_estoque(estoque_atual)
    
    elif opcao == 7:
        cabeçalho('AUMETAR PREÇO DE PRODUTOS CADASTRADOS')
        aumenta_preco(estoque_atual)
        estoque_str = json.dumps(estoque_atual)
        escreve_arquivo('arquivo.json', estoque_str)
    
    elif opcao == 8:
        cabeçalho('CONSULTAR DE ESTOQUE')
        consulta_estoque(estoque_atual)
    
    elif opcao == 9:
        cabeçalho('SAINDO DO SISTEMA....')
        break
    
    else:
        print('Opção inválida! Favor digite um número correspondente à uma função do sistema.')