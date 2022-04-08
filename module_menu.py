def linha(len=90):
    '''
Função responsável por criar as linhas do nosso cabeçalho, que são utilizadas para formatar nossos menus
e submenus. A função recebe um parâmetro nomeado, que é correspondente ao número de traços a serem 
exibidos ao usuário, e retorna o número de traços multiplicado pelo parâmetro. 
    '''
    return ('-') * len


def cabeçalho(texto):
    '''
Função reponsável por criar os cabeçalhos exibidos nos menus e submenus do nosso sistema. Recebe um texto
como parâmetro. Depois, printa os resultados das funções linhas, assim como o parâmetro que passamos,
alinhado ao centro de 90 caracteres (parâmetro da função .center) e entre as duas linhas.
    '''
    print(linha())
    print(texto.center(90))
    print(linha())


def leiaInt(aux):
    '''
Função responsável para avaliar se os valores passados no input do usuário para selecionar uma função 
são válidos. Recebe um parâmetro auxiliar que é chamado no bloco abaixo, e é exatamente o input do usuário.
Se o dado passado por ele for algo que não equivale às opções desejadas, o programa levanta as exceções abaixo. 
    '''
    try:
        i = int(input(aux))
    except (ValueError, TypeError):
        print('Ocorreu um erro! Por favor, digite o número de uma opção válida do menu.')
        pass
    except (KeyboardInterrupt):
        print('O usuario não digitou nenhum número do menu.')
        return 0
    else:
        return i

def menu(aux1):
    '''
    Função responsável por criar o menu e submenus do nosso sistema. Ela chama outra função (cabeçalho())
    e cria uma variável c responsável por ter os números das opções do nosso sistema. Passamos um loop
    for para iterar sobre cada item dos nossos parâmetros, e printar a variável c, e o item, sendo atualizado
    a cada loop for o valor de c.
    Ao final, é chamado um input para o usuário informar a função que deseja, retornando-se o seu input ao sistema.
    '''
    cabeçalho('CONTROLE DE ESTOQUE')
    c = 1
    for item in aux1:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    option = leiaInt('Escolha uma das funcionalidades do nosso sistema: ')
    return option