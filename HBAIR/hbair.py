from time import sleep

def terminal_texto():
    arquivo = open('HBAIR/terminal.txt','r')
    lista = []
    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close()
    return lista

terminal = terminal_texto()

p1 = terminal[0]
p2 = terminal[1]
p3 = terminal[2]
p4 = terminal[3]
p5 = terminal[4]
p6 = terminal[5]
p7 = terminal[6]
p8 = terminal[7]

numero_viagem = 0
fortwo = []
aviao = []

def viagem_fortwo():
    global numero_viagem
    numero_viagem += 1
    print(f'\n========== Viagem {numero_viagem} ==========')
    sleep(1)
    print(f'Estão no terminal: {terminal}')
    sleep(1)

def embarque_fortwo(mot,passageiro):
    fortwo.append(mot)
    fortwo.append(passageiro)
    print(f'Embarcaram no fortwo {mot} e {passageiro}')
    print(f'{mot} e {passageiro} vão até o avião')

def remov_terminal(passageiro1,passageiro2):
    terminal.remove(passageiro1)
    terminal.remove(passageiro2)
    if terminal == []:
        print('Terminal de embarque esta vazio')
    else:
        print(f'Ficaram no terminal: {terminal}')

def embarque_avião(pessoa):
    aviao.append(pessoa)
    fortwo.remove(pessoa)
    print(f'Estão no avião: {aviao}')
    print(f'{fortwo} ficou no fortwo e retornou para o terminal')
    terminal.append(fortwo[0])
    fortwo.clear()

def embarque_v6(pessoa1,pessoa2):
    aviao.append(pessoa1)  
    aviao.append(pessoa2)
    print(f'Estão no avião: {aviao}')
    fortwo.clear()
    fortwo.append(p1)
    print(f'O {p1} embarcou no fortwo e retornou para o terminal')
    terminal.append(p1)

def embarque_v7(pessoa1,pessoa2):
    aviao.append(pessoa1)  
    aviao.append(pessoa2)
    print(f'Estão no avião: {aviao}')
    fortwo.clear()
    print('Todos os passageiros já estão no avião')

for viagem in range(1,8):
    if viagem == 1:
        viagem_fortwo()
        embarque_fortwo(p1,p2)
        remov_terminal(p1,p2)
        embarque_avião(p2)
    elif viagem == 2:
        viagem_fortwo()
        embarque_fortwo(p1,p3)
        remov_terminal(p1,p3)
        embarque_avião(p3)
    elif viagem == 3:
        viagem_fortwo()
        embarque_fortwo(p4,p5)
        remov_terminal(p4,p5)
        embarque_avião(p5)
    elif viagem == 4:
        viagem_fortwo()
        embarque_fortwo(p4,p6)
        remov_terminal(p4,p6)
        embarque_avião(p6)
    elif viagem == 5:
        viagem_fortwo()
        embarque_fortwo(p4,p1)    
        remov_terminal(p4,p1)
        embarque_avião(p1)
    elif viagem == 6:
        viagem_fortwo()
        embarque_fortwo(p7,p8)
        remov_terminal(p7,p8)
        embarque_v6(p7,p8)
    elif viagem == 7:
        viagem_fortwo()
        embarque_fortwo(p1,p4)
        remov_terminal(p1,p4)
        embarque_v7(p1,p4)

def salvar_aviao():
    arquivo = open('HBAIR/aviao.txt','w')
    lista_passageiros = []
    lista_passageiros.append(aviao)
    arquivo.writelines(lista_passageiros)
    arquivo.close










       



