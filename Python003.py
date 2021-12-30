"""(TUPLA) TUPLA DE 0 A 20. E A PARTIR DO NÚMERO EM QUE O USUÁRIO DIGITAR, O NOME DELE APARECERÁ POR EXTENSO (O = ZERO).
E DEVE HAVER CHECAGEM."""
listanumeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', \
               'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

checaescolha = True
while checaescolha == True:
    escolha = int(input('Digite um número: '))
    if escolha >= 0 and escolha <= 20:
        print('=' * 40)
        print(f'O N° que você digitou é {escolha}. Que escrito se escreve: {listanumeros[escolha]}')
        continuar = True
        while continuar == True:
            escolha = str(input('Deseja digitar outro número [S/N]: ')).upper().strip()
            if escolha == 'S':
                print('Ok, vamos continuar!')
                print('=' * 40)
                continuar = False
            elif escolha == 'N':
                print('Ok, obrigado!')
                checaescolha = False
                break
            else:
                print('Você digitou uma opção inválida!')
                print('=' * 40)
    else:
        print("""Você digitou um número inválido! 
Você deve digitar um número entre 0 e 20.""")
        print('=' * 40)

"""(TUPLA) CRIAR TUPLA COM OS 20 PRIMEIROS COLOCADOS NA TABELA DO BRASILEIRÃO E MOSTRAR: 
5 PRIMEIROS COLOCADOS, OS ÚLTIMOS 4 COLOCADOS, LISTA COM ORDEM ALFABÉTICA, EM QUE POSIÇÃO ESTÁ O TIME "CHAPECOENSE"""

times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense',
         'America-MG', 'Ceará', 'Internacional', 'Atlético Goianiense', 'Santos', 'Athletico-PR', 'São Paulo',
         'Juventude', 'Cuiába', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')

print(f"""Os cinco primeiros da tabela são: 
1°{times[0]}
2°{times[1]} 
3°{times[2]}
4°{times[3]}
5°{times[4]}. 
""")

print(f"""Os últimos 4 colocados são:
17°{times[-4]}
18°{times[-3]}
19°{times[-2]}
20°{times[-1]}
""")

print(f"""Os times mostrados em ordem alfabética fica: '
{sorted(times)}
""")

print(f"""Atualmente a posição da chapecoense é {times.index("Chapecoense") + 1}""")

"""(TUPLA) GERAR 5 NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA, MOSTRE OS NÚMEROS QUE FORAM GERADOS, QUAL O MAIOR E O 
MENOR. """
from random import choice

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
escolhidos = (choice(tupla), choice(tupla), choice(tupla), choice(tupla), choice(tupla))
print(f"""Os números escolhidos foram: {escolhidos}
""")
print(f"""Os maior número da lista é: {max(escolhidos)}, e o menor é: {min(escolhidos)}
""")
print(f"""Sendo que o {max(escolhidos)} aparece um total de: {escolhidos.count(max(escolhidos))} vezes 
e o {min(escolhidos)} aparece um total de {escolhidos.count(min(escolhidos))} vezes""")

"""(TUPLA) PROGRAMA QUE LÊ 4 VALORES E GUARDA EM UMA TUPLA. DEPOIS MOSTRE QUANTAS VEZES APARECEU O VALOR 9,
EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3 E QUAIS FORAM OS NÚMEROS PARES."""
n1 = 1
n2 = 1
n3 = 1
n4 = 1
v1 = int(input('Digite um valor: '))
if v1 % 2 == 0:
    n1 = v1
v2 = int(input('Digite um valor: '))
if v2 % 2 == 0:
    n2 = v2
v3 = int(input('Digite um valor: '))
if v3 % 2 == 0:
    n3 = v3
v4 = int(input('Digite um valor: '))
if v4 % 2 == 0:
    n4 = v4

valores = (v1, v2, v3, v4)
mostra9 = valores.count(9)
mostra3 = valores.count(3)
print(f'\nA quantidade de vezes que o N°9 aparece é de {mostra9} vezes.')

if mostra3 == 0:
    print('O N°3 não foi digitado nenhuma vez')
else:
    print(f'O N°3 foi o {valores.index(3) + 1}° número a ser digitado\n')

if n1 == v1 or n2 == v2 or n3 == v3 or n4 == v4:
    print(f'Os números pares digitados foram:')
    if n1 == v1:
        print(f'{n1}')
    if n2 == v2:
        print(f'{n2}')
    if n3 == v3:
        print(f'{n3}')
    if n4 == v4:
        print(f'{n4}')

elif n1 != v1 and n2 != v2 and n3 != v3 and n4 != v4:
    print('Não tivemos nenhum número par!')

"""(TUPLA) PROGRAMA QUE TENHA UMA ÚNICA TUPLA COM NOMES DE PRODUTOS E SEUS PREÇOS, NO FINAL MOSTRE SEUS
NOMES E PREÇOS DE FORMA TABULADA."""

listaprodutos = ('Pão', 2, 'Arroz', 25, 'Feijão', 10)
print('-' * 20)
print('LISTAGEM DE PREÇOS')
print('-' * 20)
print(f"""
{listaprodutos[0]}......................   R${listaprodutos[1]:.2f}
{listaprodutos[2]}......................   R${listaprodutos[3]:.2f}
{listaprodutos[4]}......................   R${listaprodutos[5]:.2f}
""")
print(f'A soma de todos os produtos comprados é de: R${listaprodutos[1] + listaprodutos[3] + listaprodutos[5]:.2f}')

"""(TUPLA) PROGRAMA QUE LÊ PRODUTOS, AUTOMATIZADO."""

qtdprodutos = contador = int(input('Quantos produtos deseja cadastrar: '))
listaprodutos = []
for c in range(0, qtdprodutos):
    produto = str(input('Digite o produto: '))
    listaprodutos.append(produto)
    valor = int(input('Digite o valor do produto: R$'))
    listaprodutos.append(valor)
    print('-' * 40)

for c in range(0, qtdprodutos):
    print(f'{listaprodutos[qtdprodutos - contador]:.<30} {listaprodutos[qtdprodutos - contador + 1]:>.2f}')
    contador += 2

"""(TUPLA) CRIAR UMA TUPLA COM VÁRIAS PALAVRAS (SEM ACENTOS), DEPOIS MOSTRAR QUAIS AS VOGAIS DE CADA PALAVRA."""

listapalavras = ('Aranha', 'Cagada', 'Perdizes', 'Amor', 'Carinho')

for c in listapalavras:
    print(f'\nA palavra {c} tem as seguintes vogais: ', end='')
    for l in c:
        if l in 'aeiou':
            print(f'{l}', end='')

"""(LISTAS)  # PROGRAMA QUE LEIA 5 VALORES EM UMA LISTA E NO FINAL MOSTRE O MAIOR E O MENOR VALOR DELAS E QUAIS E
QUANTAS POSIÇÕES ELES SE ENCONTRAM."""
qtd = contador = int(input('Digite a quantidade de valores que deseja digitar: '))
lista = []

for c in range(0, qtd):
    lista.append(int(input('Digite um número: ')))
print(f'\nOs valores digitados foram: ')
for c in range(0, qtd):
    print(f'{lista[qtd - contador]}', end=', ')
    contador -= 1
print('FIM')

qtdmaior = lista.count(max(lista))
qtdmenor = lista.count(min(lista))

print(f"""\nSendo: 
- {max(lista)} o maior N°, aparecendo {qtdmaior} vez(es).. 
- {min(lista)} o menor número, aparecendo {qtdmenor} vez(es).""")

"""(LISTAS) USUARIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E O CADASTRE NA LISTA, CASO O NÚMERO JÁ EXISTA, ELE
NÃO SERÁ ADICIONADO E NO FINAL OS VALORES ÚNICOS DEVEM SER MOSTRADOS E ORDEM CRESCENTE"""

qtd = contador = int(input('Quantos valores deseja digitar: '))
pausabruta = False
digitados = 0
valornegado = 0
lista = []

validadigitar = True
while validadigitar == True:
    for c in range(0, qtd):
        v1 = (int(input('Digite um valor: ')))
        digitados += 1
        if v1 in lista:
            print(f'O valor {v1} já foi digitado, não será adicionado! ')
            valornegado += 1
        else:
            lista.append(v1)
            print(f'O valor {v1} foi adicionado em nossa lista!')
        validapergunta = True
        while validapergunta == True:
            pergunta = str(input('\nDeseja digitar um novo valor [S/N]: ')).upper().strip()
            if pergunta == 'S':
                validapergunta = False
                print('=' * 20)
            elif pergunta == 'N':
                pausabruta = True
                validapergunta = False
            else:
                print('Você digitou valor inválido, vamos novamente!')
                print('=' * 20)
        if pausabruta == True:
            validadigitar = False
            break

print(f'Os valores digitados foram:')
for c in range(0, digitados):
    lista.sort()
    print(f'{lista[qtd - contador]}', end=', ')
    print('FIM')
    contador -= 1

print(f'\nCom um total de {valornegado} N°(s) REJEITADOS POR DUPLICIDADE.')

"""(LISTAS) USUARIO DIGITA 5 VALORES E CADASTRÁ-LOS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT).
NO FINAL MOSTRA A LISTA ORDENADA NA TELA."""

lista = []
for c in range(5):
    n1 = int(input('Digite um número: '))
    if c == 0:
        lista.append(n1)
        print('Esse foi o primeiro número!')
        print(lista)
    elif lista[-1] < n1:
        lista.append(n1)
        print('Esse é o maior número até agora, vai para o final!')
        print(lista)
    else:
        p = 0
        while p < len(lista):
            if n1 <= lista[p]:
                lista.insert(p, n1)
                print(f'Número inserido na posição {p}!')
                print(lista)
                break
            p += 1

print('=' * 20)
print(f'N°s da lista: {lista}')

"""(LISTAS) LER VARIOS NÚMEROS E COLOCÁ-LO EM UMA LISTA, AO FINAL MOSTRE: QUANTOS FORAM DIGITADOS, A LISTA ORDENADA
DE FORMA DECRESCENTE, SE O VALOR 5 FOI OU NÃO DIGITADO E ESTÁ OU NÃO NA LISTA E QUAL(IS) POSIÇÕES."""

lista = []
posi5 = []
for c in range(5):
    n1 = int(input('Digite um número: '))
    lista.append(n1)

print(f'Foram digitados {len(lista)} N°s')
lista.sort(reverse=True)
print(f'A lista final é: {lista}')
if 5 in lista:
    for p in range(len(lista)):
        if lista[p] == 5:
            posi5.append(p)
            p += 1
    print(f'O N° 5 aparece na lista!')
    print(f'O N° 5 aparece na(s) seguinte(s) posições: {posi5}')

"""(LISTAS) LER VARIOS NÚMEROS E COLOCÁ-LOS EM UMA LISTA, AO FINAL MOSTRE: A LISTA TOTAL, UMA LISTA SÓ DE N°s PARES E
OUTRA SÓ DE N°s ÍMPARES. SEM USAR O "IF" LOGO NA INSERÇÃO DO NÚMERO."""

lista = []
pares = []
impares = []
for c in range(5):
    n1 = int(input('Digite um número: '))
    lista.append(n1)
lista.sort()
print(f'\nA lista total é: {lista}')
for p in range(len(lista)):
    if lista[p] % 2 == 0:
        pares.append(lista[p])
    else:
        impares.append(lista[p])
    p += 1

print(f'Os números pares digitados são: {pares}')
print(f'Os números ímpares digitados são: {impares}')

"""(LISTAS) USUÁRIO DEVE DIGITAR UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES. SEU PROGRAMA DEVERÁ ANALISAR SE A
EXPRESSÃO ESTÁ COM O N° DE PARÊNTESES CORRETOS."""

par1 = 0
par2 = 0
posiaber = 0
posifech = 0
ex = str(input('Digite uma expressão: '))
for p in range(len(ex)):
    if ex[p] == '(':
        posiaber = p
        par1 += 1
    if ex[p] == ')':
        par2 += 1
        posifech = p

    p += 1

if par1 > par2:
    print('Função negada! Existem expressões sem conclusão.')
elif par2 > par1:
    print('Função negada! Existem fechamento excessivos de expressões.')
else:
    if posifech < posiaber:
        print('A expressão foi negada, as posições dos parênteses estão trocadas.')
    else:
        print('Sua expressão é válida!')


"""(LISTA COMPOSTA) LER NOME E PESO DE VÁRIAS PESSOAS. NO FINAL MOSTRA: QUANTAS PESSOAS FORAM CADASTRADAS, QUAIS 
PESSOAS MAIS PESADAS E AS PESSOAS MAIS LEVES (CASO TENHA MAIS DE UMA PESSOA COM O MESMO PESO)."""
pessoascadastradas = 0
dados = []
infocadastros = []
maiorpeso = 0
nomesmaiores = []
menorpeso = 0
nomesmenores = []

#cadastro
validacadastro = True
while validacadastro == True:
    nome = str(input('Digite seu nome: ')).upper().strip()
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    print('-'*40)
    dados.append(nome)
    dados.append(idade)
    dados.append(peso)
    pessoascadastradas += 1
    infocadastros.append(dados[:])
    dados.clear()
    validapergunta1 = True
    while validapergunta1 == True:
        pergunta1 = str(input('Deseja cadastrar uma nova pessoa?[S/N]: ')).upper().strip()
        if pergunta1 == 'S':
            validapergunta1 = False
        elif pergunta1 == 'N':
            validacadastro = False
            break
        else:
            print('Você digitou uma opção inváida!')
            print('='*40)

#analise de peso e armazenamento de nomes.
for p in infocadastros:
    if menorpeso == 0 and maiorpeso == 0:
        menorpeso = p[2]
        maiorpeso = p[2]

    if p[2] >= maiorpeso:
        maiorpeso = p[2]
        nomesmaiores.append(p[0])

    if p[2] <= menorpeso:
        menorpeso = p[2]
        nomesmenores.append(p[0])


print(f'As pessoas cadastradas foram: {infocadastros}')
print(f"""O maior peso registrado foi: {maiorpeso} através de {nomesmaiores} '
e o menor peso foi: {menorpeso} através de {nomesmenores} """)



"""(LISTA COMPOSTAS) USUÁRIO DIGITA 7 VALORES NÚMERICOS, E DENTRO DE UMA LISTA APENAS MOSTRE OS VALORES PARES E IMPARES
EM LISTAS SEPARADAS E DE FORMA CRESCENTE."""
dadosgerais = []
dadospares = []
dadosimpares = []
nlista = []

qtdn = int(input('Quantos números deseja digitar: '))
for c in range(qtdn):
    n = int(input('Digite um número: '))
    dadosgerais.append(n)
for p in dadosgerais:
    if p % 2 == 0:
        dadospares.append(p)
    if p % 2 != 0:
        dadosimpares.append(p)


nlista.append(dadosgerais[:])
nlista.append(dadospares[:])
nlista.append(dadosimpares[:])
nlista.sort()
print(nlista)


"""(LISTA COMPOSTAS) CRIAR UMA MATRIZ 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO, NO FINAL MOSTRAR A MATRIZ COM A
FORMATAÇÃO CORRETA
0 [] [] []
1 [] [] []
2 [] [] []
  0  1  2
"""

lista = []
lista1 = []
lista2 = []
listageral = []

for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {0, c}: '))
    lista.append(n)
for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {1, c}: '))
    lista1.append(n)
for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {2, c}: '))
    lista2.append(n)

listageral.append(lista)
listageral.append(lista1)
listageral.append(lista2)

print(f"""
0 [{listageral[0][0]}] [{listageral[0][1]}] [{listageral[0][2]}]
1 [{listageral[1][0]}] [{listageral[1][1]}] [{listageral[1][2]}]
2 [{listageral[2][0]}] [{listageral[2][1]}] [{listageral[2][2]}]
   0   1   2

""")


"""(LISTAS COMPOSTAS) APRIMORAR O DESAFIO ANTERIOR E MOSTRA A SOMA DE TODOS OS VALORES PARES DIGITADOS, A SOMA DOS 
VALORES DA TERCEIRA COLUNA E O MAIOR VALOR DA SEGUNDA LINHA."""

lista = []
lista1 = []
lista2 = []
listageral = []
listapares = []
somapares = 0
somacoluna3 = 0
maior2linha = 0

for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {0, c}: '))
    lista.append(n)
    if n % 2 == 0:
        listapares.append(n)
        somapares += n
    if c == 2:
        somacoluna3 += n

for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {1, c}: '))
    lista1.append(n)
    if n % 2 == 0:
        listapares.append(n)
        somapares += n
    if c == 2:
        somacoluna3 += n
    if maior2linha == 0:
        maior2linha = n
    if maior2linha < n:
        maior2linha = n

for c in range(0, 3):
    n = int(input(f'Digite o número para a posição {2, c}: '))
    lista2.append(n)
    if n % 2 == 0:
        listapares.append(n)
        somapares += n
    if c == 2:
        somacoluna3 += n

listageral.append(lista)
listageral.append(lista1)
listageral.append(lista2)

print(f"""
0 [{listageral[0][0]}] [{listageral[0][1]}] [{listageral[0][2]}]
1 [{listageral[1][0]}] [{listageral[1][1]}] [{listageral[1][2]}]
2 [{listageral[2][0]}] [{listageral[2][1]}] [{listageral[2][2]}]
   0   1   2

""")
print('='*40)
print(f'A soma de todos os valores pares ({listapares}) é {somapares}.')
print(f'A soma de todos os valores da terceira coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é: {maior2linha}')
print(f"""
E essa é a lista geral:'
{listageral}""")

"""(LISTAS COMPOSTAS) PROGRAMA QUE GERA PALPITES DE ACORDO COM A QUANTIDADE QUE O JOGADOR QUISER PARA A 
MEGA SENA (6 NUMEROS DIFERENTES ENTRE 1 E 60) CADASTRANDO ELES EM UMA LISTA COMPOSTA E EM ORDEM CRESCENTE."""
from random import randint


palpites = []
listafinal = []
qtdpalpites = int(input('Qual a quantidade de palpites que deseja? '))
for c in range(qtdpalpites):
    contador = 6
    for a in range(0, contador):
        n = randint(1, 60)
        if n not in palpites:
            palpites.append(n)
        if n in palpites:
            contador += 1
    contador -= 1
    palpites.sort()
    listafinal.append(palpites[:])
    palpites.clear()

print(listafinal)


"""(LISTAS COMPOSTAS) LER NOME E DUAS NOTAS DE ALUNOS EM LISTA COMPOSTAS. NO FINAL MOSTRA A MÉDIA DE CADA ALUNO E
PERMITA QUE O USUÁRIO POSSA MOSTRAS AS NOTAS DE CADA UM INDIVIDUALMENTE"""



'''(DICIONÁRIOS-90) LÊ NOME, NOTAS E MÉDIA DE UM ALUNO JUNTO COM SUA SITUAÇÃO FINAL. MOSTRAR AS SITUAÇÕES 
E A OPÇÃO DE CONSULTA'''
from time import sleep

aluno = {}
listafinal = []

qtdalunos = int(input('Digite a quantidade de alunos: '))
for c in range(0, qtdalunos):
    aluno['nome'] = str(input('Digite o nome do aluno: ')).upper().strip()
    aluno['nota1'] = int(input('Digite a primeira nota: '))
    aluno['nota2'] = int(input('Digite a segunda nota: '))
    aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    if aluno['media'] >= 7:
        aluno['situacaofinal'] = 'APROVADO'
    else:
        aluno['situacaofinal'] = 'REPROVADO'
    print('-' * 40)
    listafinal.append(aluno.copy())
    aluno.clear()

validamenu = True
while validamenu == True:
    pergunta = int(input("""
MENU: 
[1] - VISUALIZAR INDIVIDUALMENTE
[2] - VISUALIZAR RELATÓRIO GERAL
[3] - SAIR

OPÇÃO: """))
    if pergunta == 3:
        print('=' * 40)
        print('OBRIGADO POR UTILIZAR!')
        break

    elif pergunta == 2:
        print('=' * 40)
        print('SITUAÇÃO FINAL')
        print('=' * 40)
        for c in range(0, qtdalunos):
            print(f"""
NOME: {listafinal[c]['nome']}
NOTAS: {listafinal[c]['nota1']} e {listafinal[c]['nota2']}
MÉDIA: {listafinal[c]['media']}""")
            if listafinal[c]['situacaofinal'] == 'APROVADO':
                print(f'ALUNO {listafinal[c]["situacaofinal"]}')
            if listafinal[c]['situacaofinal'] == 'REPROVADO':
                print(f'ALUNO {listafinal[c]["situacaofinal"]}')
            print('-' * 20)

    elif pergunta == 1:
        for c in range(0, qtdalunos):
            print(f'{[c]} - {listafinal[c]["nome"]}')
        print('=' * 40)
        validapergunta2 = True
        while validapergunta2 == True:
            pergunta2 = int(input("""
Qual aluno deseja visualizar?
Digite aqui o número de referência: """))
            if pergunta2 >= qtdalunos:
                print('Você digitou um número errado de referência!')
            else:
                print(f"""
O aluno {listafinal[pergunta2]['nome']} obteve as seguintes notas e média: 
NOTA 1: {listafinal[pergunta2]['nota1']}
NOTA 2: {listafinal[pergunta2]['nota2']}

MÉDIA: {listafinal[pergunta2]['media']}
SITUAÇÃO FINAL: {listafinal[pergunta2]['situacaofinal']}
""")
            print('=' * 40)
            sleep(2)
            validapergunta2 = False

    else:
        print('Opção inválida!\n')
        print('=' * 30)
        sleep(2)

    validacontinua = True
    while validacontinua == True:
        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

        if continua == 'S':
            print('Ok, estamos voltando!')
            print('-' * 40)
            sleep(2)
            validacontinua = False
        elif continua == 'N':
            print('=' * 40)
            print('OBRIGADO POR UTILIZAR!')
            validamenu = False
            break
        else:
            print()
            print('Você digitou uma opção inválida!')
            print('=' * 40)


'''(DICIONÁRIOS-90) LÊ NOME, NOTAS E MÉDIA DE UM ALUNO JUNTO COM SUA SITUAÇÃO FINAL. MOSTRAR AS SITUAÇÕES 
E A OPÇÃO DE CONSULTA'''
from time import sleep

aluno = {}
listafinal = []

qtdalunos = int(input('Digite a quantidade de alunos: '))
for c in range(0, qtdalunos):
    aluno['nome'] = str(input('Digite o nome do aluno: ')).upper().strip()
    aluno['nota1'] = int(input('Digite a primeira nota: '))
    aluno['nota2'] = int(input('Digite a segunda nota: '))
    aluno['media'] = (aluno['nota1']+aluno['nota2'])/2
    if aluno['media'] >= 7:
        aluno['situacaofinal'] = 'APROVADO'
    else:
        aluno['situacaofinal'] = 'REPROVADO'
    print('-'*40)
    listafinal.append(aluno.copy())
    aluno.clear()

validamenu = True
while validamenu == True:
    pergunta = int(input("""
MENU: 
[1] - VISUALIZAR INDIVIDUALMENTE
[2] - VISUALIZAR RELATÓRIO GERAL
[3] - SAIR

OPÇÃO: """))
    if pergunta == 3:
        print('='*40)
        print('OBRIGADO POR UTILIZAR!')
        break

    elif pergunta == 2:
        print('=' * 40)
        print('SITUAÇÃO FINAL')
        print('=' * 40)
        for c in range(0, qtdalunos):
            print(f"""
NOME: {listafinal[c]['nome']}
NOTAS: {listafinal[c]['nota1']} e {listafinal[c]['nota2']}
MÉDIA: {listafinal[c]['media']}""")
            if listafinal[c]['situacaofinal'] == 'APROVADO':
                print(f'ALUNO {listafinal[c]["situacaofinal"]}')
            if listafinal[c]['situacaofinal'] == 'REPROVADO':
                print(f'ALUNO {listafinal[c]["situacaofinal"]}')
            print('-' * 20)

    elif pergunta == 1:
        for c in range(0, qtdalunos):
            print(f'{[c]} - {listafinal[c]["nome"]}')
        print('='*40)
        validapergunta2 = True
        while validapergunta2 == True:
            pergunta2 = int(input("""
Qual aluno deseja visualizar?
Digite aqui o número de referência: """))
            if pergunta2 >= qtdalunos:
                print('Você digitou um número errado de referência!')
            else:
                print(f"""
O aluno {listafinal[pergunta2]['nome']} obteve as seguintes notas e média: 
NOTA 1: {listafinal[pergunta2]['nota1']}
NOTA 2: {listafinal[pergunta2]['nota2']}

MÉDIA: {listafinal[pergunta2]['media']}
SITUAÇÃO FINAL: {listafinal[pergunta2]['situacaofinal']}
""")
            print('='*40)
            sleep(2)
            validapergunta2 = False

    else:
        print('Opção inválida!\n')
        print('='*30)
        sleep(2)

    validacontinua = True
    while validacontinua == True:
        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

        if continua == 'S':
            print('Ok, estamos voltando!')
            print('-'*40)
            sleep(2)
            validacontinua = False
        elif continua == 'N':
            print('='*40)
            print('OBRIGADO POR UTILIZAR!')
            validamenu = False
            break
        else:
            print()
            print('Você digitou uma opção inválida!')
            print('='*40)


'''(DICIONÁRIOS-91) JOGADORES TEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDAR O RESULTADO EM UM DICIONÁRIO
E NO FINAL COLOCAR O DICIONARIO EM ORDEM E MOSTRAR QUE FOI O GANHADOR (NÚMERO MAIOR).
MOSTRAR OS VALORES SORTEADOS E OS RANKINGS NO FINAL.'''
from random import randint

jogador = {}
listafinal = []

qtdjogadores = int(input('Quantos participarão: '))
for c in range(0, qtdjogadores):
    jogador['nome'] = str(input('Digite o nome do jogador{c}: ')).upper().strip()
    jogador['numero'] = randint(1, 6)
    listafinal.append(jogador.copy())
    jogador.clear()

print('-'*30)
print('LISTA FINAL')
print('-'*30)
listafinal = sorted(listafinal, key=lambda k: k['numero'])
for c in range(0, qtdjogadores):
    print(f"""NOME: {c+1:} - {listafinal[c]['nome']:<10} SORTEADO: {listafinal[c]['numero']:>1} """)

"""(DICIONÁRIOS-91) JOGADORES TEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDAR O RESULTADO EM UM DICIONÁRIO
E NO FINAL COLOCAR O DICIONARIO EM ORDEM E MOSTRAR QUE FOI O GANHADOR (NÚMERO MAIOR).
MOSTRAR OS VALORES SORTEADOS E OS RANKINGS NO FINAL."""
from random import randint

jogador = {}
listafinal = []

qtdjogadores = int(input('Quantos participarão: '))

for c in range(0, qtdjogadores):
    jogador['nome'] = str(input(f'Digite o nome do jogador {c+1}: ')).upper().strip()
    jogador['numero'] = randint(1, 6)
    listafinal.append(jogador.copy())
    jogador.clear()

print('-'*30)
print('LISTA FINAL')
print('-'*30)
listafinal = sorted(listafinal, key=lambda k: k['numero'], reverse=True)
for c in range(0, qtdjogadores):
    print(f"""NOME: {c+1:} - {listafinal[c]['nome']:<10} SORTEADO: {listafinal[c]['numero']:>1} """)


"""(DICIONÁRIOS-92) CADASTRAR NOME, ANO DE NASCIMENTO (QUE DEVE SER CONVERTIDO P/ IDADE) E N° DA CARTEIRA DE TRABALHO.
SE A CARTEIRA DE TRABALHO FOR VÁLIDA, O PROGRAMA ENTÃO RECEBERÁ O PRIMEIRO ANO DE CONTRATAÇÃO E O SALÁRIO.
NO FINAL, ALÉM DE SUA IDADE CALCULE COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR. (35 ANOS DE CONTRIBUIÇÃO)"""
from datetime import datetime
ano = datetime.today().year
cadastro = {}
listageral = []
print(ano)
qtdcadastros = int(input('Digite o N° de cadastros: '))
for c in range(0, qtdcadastros):
    cadastro['nome'] = str(input('Digite seu nome (Com nome e sobrenome): ')).upper().strip()
    cadastro['anonascimento'] = int(input('Digite seu ano de nascimento: '))
    cadastro['idade'] = (ano-cadastro['anonascimento'])
    cadastro['ctps'] = int(input('Digite o número da sua CTPS: '))
    if cadastro['ctps'] <= 0:
        print('O N° da sua carteira de trabalho é inválido!')
        break
    if cadastro['ctps'] > 0:
        cadastro['anocontrata'] = int(input('Qual o ano de sua primeira contratação: '))
        cadastro['salario'] = float(input('Qual seu salário atual: '))
        cadastro['anosrestantes'] = 35-(ano-cadastro['anocontrata'])
        listageral.append(cadastro.copy())
        cadastro.clear()
    print('='*20)
print('='*40)
print('NOME:               ANO NASCIMENTO:     IDADE:    CTPS:     ANO CONTRATAÇÃO:    APOSENTADORIA:   SALÁRIO:')
print('-'*40)
for c in range(0, qtdcadastros):
    print(f"{listageral[c]['nome']:<20}{listageral[c]['anonascimento']:<20}{listageral[c]['idade']:<10}"
          f"{listageral[c]['ctps']:<10}{listageral[c]['anocontrata']:<20}{listageral[c]['anosrestantes']:<17}"
          f"{listageral[c]['salario']:<1}")

print('')
print('='*40)
print('Obrigado por usar nosso software!')
print('='*40)


'''(DICIONÁRIOS-93) LER O NOME DO JOGADOR DE FUTEBOL, QUANTAS PARTIDAS ELE JOGOU, SUA QUANTIDADE DE GOLS POR PARTIDAS 
(QUE DEVE SER ARMAZENADO EM LISTA) E NO FINAL MOSTRAR O TOTAL DE GOLS NO CAMPEONATO. MOSTRAR EM UMA LISTA ORGANIZADA.'''
"""(DICIONÁRIOS-93) LER O NOME DO JOGADOR DE FUTEBOL, QUANTAS PARTIDAS ELE JOGOU, SUA QUANTIDADE DE GOLS POR PARTIDAS
(QUE DEVE SER ARMAZENADO EM LISTA) E NO FINAL MOSTRAR O TOTAL DE GOLS NO CAMPEONATO. MOSTRAR EM UMA LISTA ORGANIZADA."""
from time import sleep

cadastro = {}
gols = []
listageral = []

qtdjogadores = int(input('Quantos jogadores iremos cadastrar: '))
for c in range(0, qtdjogadores):
    nome = str(input('Nome do jogador: ')).upper().strip()
    cadastro['nome'] = nome
    qtdpartidas = int(input('Quantidade de partidas: '))
    for a in range(0, qtdpartidas):
        n = int(input(f'Quantos gols no {a + 1}° jogo: '))
        gols.append(n)
    cadastro['gols'] = gols[:]

    listageral.append(cadastro.copy())
    cadastro.clear()
    gols.clear()
print('')
print('='*40)
for b in range(0, qtdjogadores):
    print(f"NOME: {listageral[b]['nome']}  GOLS: {listageral[b]['gols']} TOTAL GOLS: {sum(listageral[b]['gols'])} "
          f"PARTIDAS: {len(listageral[b]['gols'])}")

print('-'*40)
for n in range(0, qtdjogadores):
    print(f'{n} - {listageral[n]["nome"]}')
print("-"*40)


print('='*40)
jogadorescolhido = int(input('Qual jogador deseja visualizar detalhadamente: '))
print('-'*40)
sleep(2)
contador = 1

print(f'O jogador {listageral[jogadorescolhido]["nome"]} fez:')
for c in listageral[jogadorescolhido]['gols']:
    print(f'{c} gols na partida {contador}')
    contador += 1
print(f"E média de {sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols'])} gols por jogo"
      f" em {len(listageral[jogadorescolhido]['gols'])} partidas!")



"""(DICIONÁRIOS-94) LER NOME, SEXO E IDADE DE VÁRIAS PESSOAS. GUARDANDO CADA UMA DAS PESSOAS EM UM DICIONÁRIO E
TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL MOSTRE: QUANTAS PESSOAS FORAM CADASTRADAS, A MÉDIA DE IDADE DO GRUPO,
UMA LISTA COM TODAS AS MULHERES E UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA. """
cadastro = {}
listageral = []
cadastradas = 0
idadegeral = 0
listamulheres = []
listamaiormedia = []

acadastrar = int(input("Quantas pessoas vamos cadastrar: "))

for c in range(0, acadastrar):
    nome = str(input('Digite o nome: ')).upper().strip()
    sexo = str(input('Digite o sexo: ')).upper().strip()
    idade = int(input('Digite a idade: '))

    cadastro['nome'] = nome
    cadastro['sexo'] = sexo
    cadastro['idade'] = idade

    if sexo == 'F':
        listamulheres.append(nome)
    idadegeral += idade
    cadastradas += 1

    listageral.append(cadastro.copy())
    cadastro.clear()
for d in range(0, acadastrar):
    if listageral[d]['idade'] > (idadegeral/cadastradas):
        listamaiormedia.append(listageral[d]['nome'][:])
print('='*40)
print('CADASTROS: ')
print('='*40)
for e in range(0, acadastrar):
    print(f"{e} - {listageral[e]['nome']} - {listageral[e]['idade']} anos")
print('')
print(f'Tivemos um total de: {cadastradas} pessoas cadastradas\n')
print(f'A média da idade do grupo é: {idadegeral/cadastradas} anos\n')

print('-'*40)
print('A lista de mulheres cadastradas:')
for c in listamulheres:
    print(c)

print('-'*40)
print(f'As pessoas que estão ACIMA da média de {idadegeral/cadastradas} anos são:')
for c in listamaiormedia:
    print(c)


"""(DICIONÁRIOS-95) APRIMORAR O DESAFIO 93 PARA QUE ELE CADASTRE VÁRIOS JOGADORES INCLUINDO UM SISTEMA DE DETALHES
DO APROVEITAMENTO DE CADA JOGADOR (TOTAL DOS GOLS, MÉDIA POR JOGO) E NO FINAL DÊ A OPÇÃO DE ESCOLHER UM JOGADOR APENAS
A SER MOSTRADO."""
from time import sleep

cadastro = {}
gols = []
listageral = []
qtdjogadores = 0

""""cadastro de jogador"""
validacadastro = True
while validacadastro == True:

    pergunta = str(input('Deseja cadastrar um jogador? [S/N]: ')).upper().strip()
    if pergunta == 'S':
        nome = str(input('Nome do jogador: ')).upper().strip()
        cadastro['nome'] = nome
        qtdpartidas = int(input('Quantidade de partidas: '))
        for a in range(0, qtdpartidas):
            n = int(input(f'Quantos gols no {a + 1}° jogo: '))
            gols.append(n)
        cadastro['gols'] = gols[:]

        listageral.append(cadastro.copy())
        cadastro.clear()
        gols.clear()
        qtdjogadores += 1

    elif pergunta == 'N':
        break
    else:
        print('Você digitou uma opção inválida! '
              'Tente novamente!')
        print('='*40)
        sleep(2)

"""definindo maior média"""
totalgolsmarcados = 0
totaljogosjogados = 0
for g in range(0, qtdjogadores):
    totalgolsmarcados += sum(listageral[g]['gols'])
    totaljogosjogados += len(listageral[g]['gols'])

mediageral = totalgolsmarcados/totaljogosjogados

"""iniciando um menu para escolhas gerais e individuais"""
validamenu = True
while validamenu == True:
    if qtdjogadores == 0:
        break
    elif qtdjogadores >= 1:
        print("""
[1] - VER LISTA GERAL 
[2] - ANALISAR INDIVIDUALMENTE
[3] - SAIR""")
        pergunta2 = int(input('OPÇÃO: '))

        """lista geral"""
        if pergunta2 == 1:
            print('')
            print('='*40)
            for b in range(0, qtdjogadores):
                print(f"NOME: {listageral[b]['nome']}  GOLS: {listageral[b]['gols']} TOTAL GOLS: "
                      f"{sum(listageral[b]['gols'])} PARTIDAS: {len(listageral[b]['gols'])}")

        """visão detalhada individual"""
        if pergunta2 == 2:
            print('-'*40)
            for n in range(0, qtdjogadores):
                print(f'{n} - {listageral[n]["nome"]}')

            print('='*40)
            jogadorescolhido = int(input('Qual jogador deseja visualizar detalhadamente: '))
            print('-'*40)
            sleep(2)
            contador = 1

            print(f'O jogador {listageral[jogadorescolhido]["nome"]} fez:')
            for c in listageral[jogadorescolhido]['gols']:
                print(f'{c} gols na partida {contador}')
                contador += 1
            print(f"-- E média de {sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols'])}"
                  f" gol(s) por jogo em {len(listageral[jogadorescolhido]['gols'])} partida(s)!")
            if sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols']) > mediageral:
                print(f'-- O que coloca ele acima da média geral de gols entre os jogadores avaliados: {mediageral:.2f}'
                      f' gol(s) por partida')
            elif sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols']) == mediageral:
                print(f'-- O que coloca ele exatamente na média geral de gols entre os jogadores avaliados: '
                      f'{mediageral:.2f} gol(s) por partida.')
            elif sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols']) < mediageral:
                print(f'-- O que coloca ele abaixo na média geral de gols entre os jogadores avaliados: '
                      f'{mediageral:.2f} gol(s) por partida.')
            print(f"-- Caso a média de "
                  f"{sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols'])} seja mantida,"
                  f" o jogador em 38 rodadas tem uma capacidade de "
                  f"{sum(listageral[jogadorescolhido]['gols'])/len(listageral[jogadorescolhido]['gols'])*38:.2f} gols.")

        """opção de sair"""
        if pergunta2 == 3:
            break

print('='*40)
print('OBRIGADO POR UTILIZAR NOSSO SOFTWARE!')


"""(FUNÇÕES-96) LER AS DIMENSÕES DE UM TERRENO (LARGURA E COMPRIMENTO) E MOSTRAR A ÁREA TOTAL DO TERRENO."""


def areatotal(a, b):
    areaterreno = a*b
    print(areaterreno)


frente = int(input('Metros de frente: '))
fundo = int(input('Metros de fundo: '))

areatotal(frente, fundo)


"""(FUNÇÕES-97) UMA FUNÇÃO "ESCREVA():" QUE RECEBE UM TEXTO QUALQUER E ADAPTA LINHAS DE CABEÇALHO AO SEU TAMANHO."""
def escreva (a):
    print(f'='*len(a))
    print(f'{a:>1}')
    print('='*len(a))


cabecalho = str(input('CABEÇALHO: ')).upper().strip()
escreva(cabecalho)


"""(FUNÇÕES-98) UMA FUNÇÃO CHAMADA "CONTADOR():" QUE RECEBA TRES PARÂMETROS: INICIO, FIM E PASSO. E REALIZAR
TRÊS CONTAGENS A PARTIR DA FUNÇÃO CRIADA: A) 1 até 10 de 1 em 1. B) 10 até 0, de 2 em 2. C) Contagem personalizada.
SE O PASSO FOR NEGATIVO "-1", O PRINT IGNORA O "-" E SE FOR "O" ele considera "1". """
from time import sleep


def ct1ate10():
    for n in range(0, 11, 1):
        print(n, end=" ")
        sleep(0.5)
    print('FIM.')


def ct10ate0():
    for n in range(10, -1, -2):
        print(n, end=" ")
        sleep(0.5)
    print('FIM.')


def ctescolhida(a, b, c):
    if c == 0 and b < 0:
        c = -1
    if c == 0 and b > 0:
        c = 1
    if b < 0:
        b -= 1
    if b > 0:
        b += 1
    if c > 0 and b < 0:
        c -= c*2
    for n in range(a, b, c):
        print(n, end=" ")
    print('FIM.')


ct1ate10()
ct10ate0()
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
ritmo = int(input('Digite o ritmo: '))

ctescolhida(inicio, fim, ritmo)



"""(FUNÇÕES-99) FUNÇÃO "MAIOR():" QUE RECEBA VÁRIOS PARÂMETROS E SEU PROGRAMA DEVE ANALISAR OS VALORES, DIZENDO QUAL
 O MAIOR ENTRE ELES."""


def maior(*num):
    maior = 0
    for c in num:
        if maior == 0:
            maior = c
        if c > maior:
            maior = c

    print(f'Entre os números: ', end='')
    for c in num:
        print(f'{c}', end=' ')

    print('.\n')
    print(f'O maior valor é: {maior}')


n = int(input('Digite o primeiro número: '))
n1 = int(input('Digite o segundo número: '))
n2 = int(input('Digite o terceiro número: '))

maior(n, n1, n2)



"""(FUNÇÕES-100) LISTA CHAMADA "NUMEROS" E DUAS FUNÇÕES: "SORTEIA():" E "SOMAPAR():". A PRIMEIRA SORTEIA 5 NÚMEROS
 E A SEGUNDA VAI MOSTRAR SOMENTE A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR."""
from random import choice


def finaliza(palavra):
    print('='*30)
    print(palavra)
    print('='*30)


def sorteia(numeros):
    while len(sorteados) < 5:
        escolhido = choice(numeros)
        if escolhido in sorteados:
            pass
        else:
            sorteados.append(escolhido)
    print('Os sorteados foram:', end=' ')
    for c in sorteados:
        print(c, end=' ')
    print(',FIM!')


def somapar(sorteados):
    for c in sorteados:
        if c % 2 == 0:
            sorteadopares.append(c)
    if len(sorteadopares) > 0:
        print(f'Os total somado dos valores pares sorteado é de: {sum(sorteadopares)}')
    elif len(sorteadopares) < 0:
        print(f'Nenhum dos números sorteados são pares.')


numeros = []
sorteados = []
sorteadopares = []

qtdnumeros = contador = int(input('Quantos números deseja digitar: '))
for c in range(0, qtdnumeros):
    n = int(input('Digite um número: '))
    numeros.append(n)

finaliza('RESULTADO FINAL:')
sorteia(numeros)
somapar(sorteados)


"""(FUNÇÕES-101) FUNÇÃO VOTO() QUE VAI RECEBER UM PARÂMETRO DO ANO DE NASCIMENTO. COM ISSO RETORNANDO VALOR LITERAL, 
INDICANDO SE ELA TEM O VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO."""
def voto(anonascimento):
    """
    :param anonascimento: parte principal do calculo para determinação de disponibilidade.
    :return: idade
    """
    from datetime import datetime
    hoje = datetime.today().year
    idade = hoje - anonascimento
    return idade


nascimento = int(input('Informe seu ano de nascimento: '))
idade = voto(nascimento)

if idade < 16:
    print(f'Pela sua idade de {idade} anos, você tem seu voto NEGADO!')
if idade >= 16 and idade <= 18 :
    print(f'Pela sua idade de {idade} você tem seu voto OPCIONAL')
if idade > 18 and idade < 65:
    print(f'Pela sua idade de {idade} você tem seu voto OBRIGATÓRIO')
if idade >= 65:
    print(f'Pela sua idade de {idade} você tem seu voto OPCIONAL')


"""(FUNÇÕES-102) FUNÇÃO FATORIAL() QUE CALCULA O FATORIAL DE UM NÚMERO E COMO OPCIONAL (NO PRÓPRIO PARÂMETRO) INDICA
SE A CONTA É OU NÃO MOSTRADA."""


def fatorial(n=0, contador=0, show=False):
    """
    :param n: numero a ser calculado
    :param contador: base definida automaticamente, validador da contagem
    :param show: (opcional) para mostrar ou não a resolução
    :return: o valor fatorial de um número N.
    """
    if show:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print('x', end='')
            else:
                print('= ', end='')

    while contador > 0:
        n *= contador
        contador -= 1
    return n


base = num = int(input('Digite um número: '))
while True:
    verconta = str(input('Gostaria de ver a resolução? [S/N]: ')).upper().strip()
    if verconta not in 'NS':
        print('Você digitou uma opção inválida!')
        print('-'*30)
    else:
        break

contador = num - 1
resultado = fatorial(num, contador, show=True if verconta == 'S' else False)
print(f'{resultado}')


"""(FUNÇÕES-103) FUNÇÃO FICHA() QUE RECEBA NOME E QUANTOS GOLS MARCADOS. DEVE SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR
MESMO SE QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE. TANTO NOME QUANDO GOLS."""


def ficha(nome='<desconhecido>', gols=''):
    if gols.isnumeric() == True:
        gols = gols
    else:
        gols = '<desconhecido>'

    if nome:
        nome = nome
    else:
        nome = '<desconhecido>'

    print(f'O jogador {nome} fez {gols} gol(s).')

nome = str(input('Digite o nome: ')).upper().strip()
gols = str(input('Quantidade de gols: '))


ficha(nome, gols)


"""(FUNÇÕES-104) FUNÇÃO LeiaInt() QUE SERÁ PARECIDO COM INPUT DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS
UM VALOR NUMÉRICO."""


def leiaint(checagem='A'):
    while True:
        checagem = str(input('Digite um número: '))
        if checagem.isnumeric():
            break
        else:
            print('ERRO, você não digitou um número!')

    return checagem


n = leiaint()
print(f'Você digitou o número {n}. ')


"""(FUNÇÕES-105) FUNÇÃO NOTAS() QUE RECEBE VÁRIAS NOTAS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
QUANTIDADE DE NOTAS, A MAIOR NOTA, A MENOR NOTA, A MÉDIA DAS NOTAS E A SITUAÇÃO. ADICIONANDO DOC STRINGS NA FUNÇÃO."""
from time import sleep


def notas(addsitu=False):
    """

    :param addsitu: opcional para que a situação de aprovação (ou não) seja mostrada.
    :return: dicionário com informações de alunos
    """
    notamaior = 0
    notamenor = 0
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    for c in range(0, qtdnotas):
        n = float(input('Digite um nota: '))
        todasnotas.append(n)

    for c in todasnotas:
        if notamaior == 0:
            notamaior = c
        if notamenor == 0:
            notamenor = c
        if c > notamaior:
            notamaior = c
        if c < notamenor:
            notamenor = c

    medianotas = sum(todasnotas)/qtdnotas
    if medianotas > 7:
        situ = 'APROVADO'
    elif medianotas > 5:
        situ = 'PROVA REC'
    else:
        situ = 'REPROVADO'

    cadastro['nome'] = nome
    cadastro['qtdnotas'] = qtdnotas
    cadastro['maiornota'] = notamaior
    cadastro['menornota'] = notamenor
    cadastro['media'] = medianotas
    if addsitu == True:
        cadastro['situacao'] = situ


cadastro = {}
todasnotas = []
qtdnotas = 3
todoscadastros = []

qrsitu = str(input('Deseja cadastrar situação[S/N]: ')).upper().strip()

while True:
    notas(addsitu=False if qrsitu == 'N' else True)
    todoscadastros.append(cadastro.copy())
    cadastro.clear()
    continuarcadastro = str(input('Deseja cadastrar mais uma pessoa [S/N]: ')).upper().strip()
    if continuarcadastro == 'S':
        sleep(2)
        print('Então vamos cadastrar novamente!')
        print('='*30)
    if continuarcadastro == 'N':
        print('OK!')
        print('='*30)
        sleep(2)
        break


print('ESCOLHA O ALUNO QUE DESEJA VISUALIZAR DE FORMA COMPLETA: ')
for c in range(0, len(todoscadastros)):
    print(f"{c} - {todoscadastros[c]['nome']}")
print('-'*30)
escolhaaluno = int(input('Digite o N° de referência do aluno: '))
print('='*30)
if escolhaaluno not in range(0, len(todoscadastros)):
    print('Você digitou um valor incompátivel!')
else:
    if qrsitu == 'S':
        print(f"""
    ALUNO: {todoscadastros[escolhaaluno]["nome"]} 
    MÉDIA: {todoscadastros[escolhaaluno]["media"]} 
    SITUAÇÃO: {todoscadastros[escolhaaluno]["situacao"]} 
    """)
    else:
        print(f"""
            ALUNO: {todoscadastros[escolhaaluno]["nome"]} 
            MÉDIA: {todoscadastros[escolhaaluno]["media"]} 
            """)


"""(FUNÇÕES-106) CRIAR UM SISTEMA QUE TENHA O "INTERACTIVE HELP" DO PYTHON. O USUÁRIO DIGITA O COMANDO QUE DESEJA SABER
E AUTOMATICAMENTE ELE MOSTRA SUA AJUDA. QUANDO DIGITAR "FIM" O PROGRAMA SE ENCERRARÁ. (USAR CORES)."""
from time import sleep


def interactivehelp(palavra):
    print('\033[1;34;40mEstamos acessando o manual...\033[m')
    sleep(3)
    print('\033[1;34;40m', end='')
    help(palavra)
    print('\033[m', end='')


def cabecalho(palavracab):
    print('\033[1;32;40m-\033[m'*len(palavracab))
    print(f'\033[1;32;40m{palavracab}\033[m')
    print('\033[1;32;40m-\033[m'*len(palavracab))


while True:
    cabecalho('SISTEMA DE AJUDA PyHelp')
    procura = str(input('Função ou Biblioteca > ')).upper().strip()

    if procura == 'FIM':
        cabecalho('ATÉ LOGO!')
        break
    else:
        interactivehelp(procura)
    print('='*30)
