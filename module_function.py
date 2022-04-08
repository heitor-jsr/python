from textwrap import indent


def escreve_arquivo(nome, dados):
    '''
    Função responsável por escrever os dados passados pelo usuário ao nosso arquivo. Recebe dois parâmetros,
    o nome do arquivo e a variável com os dados.
    arquivo: variável para abrir o arquivo passado no parâmetro, realizar a escrita dos dados do parâmetro
    e fechar o arquivo.
    '''
    arquivo = open(nome, 'w+')
    arquivo.write(dados)
    arquivo.close()

def cadastrar_produto(estoque_atual):
    '''
    Função para implementar a inserção de dados no nosso arquivo de estoque. 
    produtos: dicionário criado para receber a chave 'Nome', e o valor que é o input do usuário informando
    o nome do produto que deseja inserir no estoque. São usadas as funções capitalize e strip para padronizar
    os dados inseridos, evitando conflitos, inconsistências e redundâncias. 
    loop for: verifica se o valor passado pelo usuário à chave 'Nome' já se encontra em algum dos itens do 
    parâmetro que passamos para a função (é o nosso estoque). Se já estiver, o programa retorna um print
    informando que o produto já está no nosso estoque, e retorna para o início da execução da função.
    try e except: foram usados os trys e excepts para conter os inputs do usuário dos dados referentes 
    às chaves 'Quantidade', 'Custo' e 'Venda da variável produtos, a fim de avaliar se os dados passados pelos 
    usuários são válidos para nosso sistema. No caso de o dado ser inválido, é informado o erro, e o 
    usuário tem mais uma oportunidade de inserir o dado corretamente.
    Ao final, o nosso parâmetro recebe o append da variável produtos, contendo os dados dos produtos que
    o usuário está inserindo no nosso sistema. 
    OBS: preferi usar como padrão para o sistema valores floats, pois permitem a manipulação de valores
    quebrados, o que é essencial para se trabalhar com quantidades de estoque e valores de produtos. 
    '''
    count = ()
    produtos = {} 
    produtos['Nome'] = input('Digite o nome do produto:').capitalize().strip()
    for i in estoque_atual:
        if i['Nome'] == produtos['Nome']:
            print('Este produto já está no estoque. Selecione uma opção adequada!')
            return 
    try: 
        produtos['Quantidade'] = float(input('Digite a quantidade do produto a ser inserida no estoque:'))
    except ValueError:
        print('Você digitou um dado inválido!')
        produtos['Quantidade'] = float(input('Digite a quantidade do produto a ser inserida no estoque:'))
    try:
        produtos['Custo'] = float(input('Digite o preço de custo do produto:'))
    except ValueError:
        print('Você digitou um dado inválido!')
        produtos['Custo'] = float(input('Digite o preço de custo do produto:'))
    try:
        produtos['Venda'] = float(input('Digite o preço de venda do produto:'))
    except ValueError:
        print('Você digitou um dado inválido!')
        produtos['Venda'] = float(input('Digite o preço de venda do produto:'))
    estoque_atual.append(produtos)


def alterar_dados(estoque_atual):
    '''
    Função responsável por alterar os dados dos produtos cadastrados em nosso estoque. Uma observação é 
    que o usuário deve digitar o nome do produto corretamente (tive bug com o else para o caso de digitar
    algo que não está cadastrado - isso em todas as funções -, pois retornava o else para todos os produtos cadastrados - debuguei o 
    código até não conseguir mais, e não consegui resolver o problema. Se o Sr. puder me ajudar a resolver, 
    agradeço :D.)
    nome_produto: recebe o input do usuário para informar o nome do produto que o usuário deseja alterar 
    algum dado. 
    informacao_alterar: recebe o input do usuário informando a informação a ser alterada pelo usuário.
    valor_novo: recebe o input do usuário informando o novo dado.
    OBS: usados capitalizes e strips quando convenientes, para possibilitar a padronização dos dados, evitando
    inconsistências, redundâncias e erros. 
    loop for: é usado para avaliar se o valor da chave 'Nome' de algum item no nosso parâmetro (estoque)
    é igual ao valor que passamos para o nome_produto. Se for, primeiro verificamos se a informação que
    queremos alterar é o nome do produto (pois não permite o float que precisamos para os outros dados),
    e se for, o item i do nosso parâmetro, representado pelo valor da variável informacao_alterar capitalizado
    recebe o valor_nome (nome novo), capitalizado e sem espaços.
    Se não for, o nosso i (item no nosso array de dicionários - cada um representa um produto) vai receber
    para a chave representada pelo input em informacao_alterar o valor_novo com ponto flutuante. 
    '''
    print('Tenha certeza de digitar o nome do produto corretamente!')    
    nome_produto = input('Digite o nome do produto que deseja alterar um dado cadastrado: ').capitalize().strip()
    informacao_alterar = input('Digite a informação do item que deseja alterar: ').strip()  
    valor_novo = input('Insira o novo dado: ').strip()
    for i in estoque_atual:  
        if i['Nome'] == nome_produto:
            if informacao_alterar == 'nome':
                i[informacao_alterar.capitalize()] = valor_novo.capitalize().strip()
            else:
                i[informacao_alterar.capitalize()] = float(valor_novo)


def registro_entrada(estoque_atual):
    '''
    Função responsável por registrar entradas no estoque. Recebe como parâmetro o nosso estoque (um array
    de dicionários - cada dict contém um produto).
    produto_entrada: input do usuário informando o nome do produto que deseja registrar uma entrada.
    qtd_entrada: quantidade de produtos que vai ser adicionada no nosso diciário.
    1º loop for:vai percorrer sobre o array de dicts e verificar se ele contém a chave 'Entradas'. Se
    não conter, ela é adicionada ao dict do produto, com um valor inicial de 0.
    2º loop for: uma vez existente a chave 'Entradas', cria-se a variavél cont, que vai ser atualizada 
    com 1 para cada loop, e depois o valor dela vai ser incrementado no valor da chave 'Entradas', para informar
    quantas entradas o determinado produto recebeu desde o seu cadastro. Além disso, é atualizada o valor
    da chave 'Quantidade' do dict do produto, incrementando no valor da chave a quantidade de produtos
    que estão entrando no estoque. OBS: criada uma variável auxiliar a para receber o valor de 'Entradas'
    acao: opção adicional para o usuário verificar o número de entradas que o produto recebeu desde o seu 
    cadastro no estoque. Caso o usuário queira fazer a consulta, o programa retorna o valor armazenado na
    variável a declarada anteriormente. 
    '''
    print('Tenha certeza de digitar o nome do produto corretamente!')    
    produto_entrada = input('Digite o produto para o qual deseja registrar uma entrada: ').capitalize().strip()
    qtd_entrada = input('Digite a quantidade de itens para a entrada atual: ').strip()
    for i in estoque_atual:
        if 'Entradas' not in i.keys():
            i['Entradas'] = 0
    for i in estoque_atual:
        cont = 0
        if produto_entrada == i['Nome']:
            cont +=1
            i['Entradas'] += cont
            a = i['Entradas']
            i['Quantidade'] += float(qtd_entrada)    
    acao = input('Você deseja verificar a quantidade de entradas registradas para um produto? S/N: ').strip()
    if acao == 'S' or acao == 's':
        prod = input('Digite o nome do produto que desena obter informação: ').capitalize().strip()
        for i in estoque_atual:
            if prod == i['Nome']:
                print(f'A quantidade de entradas registradas para o produto desde o seu registro em nosso estoque é {a}.')
    
def registro_saida(estoque_atual):
    '''
    Função responsável por registrar saídas no estoque. Recebe como parâmetro o nosso estoque (um array
    de dicionários - cada dict contém um produto). Para evitarmos repetições desnecessárias, a função
    faz a mesma coisa que a def registro_entrada(). A única diferença é que agora a chave criada é 'Saidas',
    e a quantidade é atualizada reduzindo o número de produtos cadastrados. 
    '''
    print('Tenha certeza de digitar o nome do produto corretamente!')
    produto_saída = input('Digite o produto para o qual deseja registrar uma saída: ').capitalize().strip()
    qtd_saida = input('Digite a quantidade de itens para a saída atual: ').strip()
    for i in estoque_atual:
        if 'Saidas' not in i.keys():
            i['Saidas'] = 0
    for i in estoque_atual:
        cont = 0
        if produto_saída == i['Nome']:
            cont +=1
            i['Saidas'] += cont
            a = i['Saidas']
            i['Quantidade'] -= float(qtd_saida)    
    acao = input('Você deseja verificar a quantidade de saídas registradas para um produto? S/N: ').strip()
    if acao == 'S' or acao == 's':
        prod = input('Digite o nome do produto que desena obter informação: ').capitalize().strip()
        for i in estoque_atual:
            if prod == i['Nome']:
                print(f'A quantidade de saídas registradas para o produto desde o seu registro em nosso estoque é {a}.')
    
def excluir_produto(dic):
    '''
    Função responsável por realizar a exclusão de um produto de nosso estoque.
    prints: achei interessante dar um print nos produtos do estoque antes e depois para o usuário ter
    a certeza de que o produto excluído foi desejado. 
    loop for: para cada item (dicionário) no nosso array (estoque) que é o parâmetro da função, nós
    verificamos se a chave (input do usuário informando o nome do produto que deseja excluir) é igual
    a algum valor de i['Nome'] de algum item em nosso array de dicionários. Se for, o item em questão
    (dicionário) é removido.
    '''
    print('Tenha certeza de digitar o nome do produto corretamente!')
    print(dic)
    chave = input('Digite o nome do item que deseja excluir: ').capitalize().strip()
    for i in dic:  
        if chave == i['Nome']:
            dic.remove(i)
    print(dic)

def somar_estoque(estoque):
    '''
    Função responsável por somar os preços de custo, de venda, e a quantidade dos itens no nosso estoque.
    Recebe como parâmetro o nosso estoque.
    venda: variável responsável por armazenar os dados de venda dos produtos
    custo: variável responsável por armazenar os dados de custo dos produtos
    total: variável responsável por armazenar a quantidade de itens do nosso estoque
    1º loop for: responsável por iterar sobre todos os itens registrados no nosso estoque (array de dicionários),
    e incrementar em cada variável descrita acima o valor das chaves 'Custo', 'Venda' e 'Quantidade' de
    cada item do array de dicionários. 
    Depois disso, uso de fstrings para printar os valores ao usuário.
    Além disso, foi criada funcionalidade para informar os valores de venda, custo e a quantidade de um
    item apenas. 
    Para isso, perguntamos ao usuário se ele quer acessar a informação, e se a resposta for s ou S, a função
    é executada. Primeiro, o usuário informa o produto para o qual deseja obter a informação, e se ele for encontrado
    em nosso estoque, as variáveis auxiliares declaradas recebem os seus valores de quantidade * custo e
    quantidade * venda.
    Finalmente, é usado fstrings para printar os valores de custo e venda do produto desejado.

    '''
    venda = 0
    custo = 0
    total = 0
    for i in estoque:
        custo += i['Custo']
        venda += i['Venda']
        total += i['Quantidade']
    print(f'A soma do preço de custo dos itens em R$ no estoque é: {custo}')
    print(f'A soma do preço de venda dos itens em R$ no estoque é: {venda}')
    print(f'O número total (unidades) de itens em estoque é: {total}')
    individual = input('Você deseja consultar um item individual? [S/N]: ')
    if individual == 'S' or individual == 's':
        print(estoque)
        produto = input('Digite o nome do produto que deseja obter a informação: ').capitalize().strip()
        custo_individual = 0.0
        venda_individual = 0.0
        for k in estoque:
            if k['Nome'] == produto:
                custo_individual = k['Quantidade'] * k['Custo']
                venda_individual = k['Quantidade'] * k['Venda']
        print(f'O valor de custo total do item {produto} é R$ {custo_individual}')
        print(f'O valor de venda total do item {produto} é R$ {venda_individual}')


def aumenta_preco(estoque_atual):
    '''
    Função que decidi implementar para o caso de o usuário querer incrementar em algum dos valores 
    um aumento com base em porcentagem. 
    produto: usuário informa o produto sobre o qual quer aplicar o aumento.
    onde_aumentar: usuário informa se quer aumentar em preço de custo ou de venda.
    percentual: percentual de aumento que o usuário deseja aplciar.
    Uso de try e except para averiguar se o valor passado para percentual é válido.
    Se for, acessa-se o loop for, que vai iterar sobre o array de dicionários (nosso estoque), e vai
    avaliar se o valor de i['Nome'] é igual a produto, e se onde_aumentar é igual a 'Venda', para
    aplicar o percentual de aumento sobre o valor de venda, alterando o valor de i['Venda'], para o
    valor antigo * o percentual, arredondado para duas casas decimais. 
    Para alterar o preço de custo é feita a mesma coisa.
    '''
    produto = input('Digite o nome do produto que deseja aplicar um percentual de aumentos em um de seus registros: ').capitalize().strip()
    onde_aumentar = input('Informe sobre qual dos preços (de custo ou de venda) o aumento será aplicado: ').capitalize().strip()
    percentual = 0
    try:
        percentual = float(input('Informe o percentual de aumento (incluir o percentual sobre os 100 por cento decimal do produto - por exemplo: para o aumento de 10 por cento, use o decimal 1.10.): '))
    except ValueError:
        print('Você não digitou um valor válido! Tente novamente.')
    for i in estoque_atual:
        if i['Nome'] == produto and onde_aumentar == 'Venda':
            i['Venda'] = round(i['Venda'] * percentual, 2)
        elif i['Nome'] == produto and onde_aumentar == 'Custo':
            i['Custo'] = round(i['Custo'] * percentual, 2)

def consulta_estoque(est):
    '''
    Função para realizar a consulta do nosso estoque, como um todo. É necessário o import de json aqui.
    Vai receber uma variável com um array vázio, para que ele receba cada item do nosso parâmetro (estoque)
    , por meio do loop for, que vai iterar sobre o estoque e apensar na nossa variável cada item 
    encontrado no estoque(dict). Decidi fazer isso (dar o estoque para uma variável que só vai ser 
    usada aqui) para evitar algum erro com a variável de estoque principal, que é responsável 
    por conter os dados usados em todas as funções e armaenados no arquivo.
    Depois, é dado dois prints, um com a informação para apresentar os dados, e outros para fazer um print
    mais legível para o usuário, usando o dumps na variável consultando_est, com os métodos de json sort_keys
    e indent.
    '''
    import json
    consultando_est = []
    for i in est:
        consultando_est.append(i)
    print('Olá! Atualmente o seu estoque está compostos pelos seguintes itens:')
    print(json.dumps(consultando_est, sort_keys=False, indent=True))