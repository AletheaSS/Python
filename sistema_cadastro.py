# -*- coding: utf-8 -*-

informacao_paciente = {'nome' : [], 'data_nascimento' : [], 'pressao_arterial' : []}
numPacientes = 0
programa_principal = True
while programa_principal:

    # Menu Inicio
    print ('''\n====================
MENU
====================
0- Finaliza
1- Cadastro
2- Relatório Geral
3- Alteração de Dados
4- Exclusão
====================''')

    menuop = input("Digite o numero da opçao desejada: ")
    print('\n')
    
    #limpa tela
    import os
    os.system('clear') or None

    #Fecha programa 
    if menuop == '0':
        programa_principal = False

    #Cadastra paciente
    if menuop == '1':
                    
        nome = input ("Informe seu nome: ")
        data_nascimento = input ("Informe sua data de nascimento: ")
        pressao_arterial = input ("Informe sua pressão arterial: ")
        print('\nCadastrado com sucesso!')

        informacao_paciente['nome'].append(nome)
        informacao_paciente['data_nascimento'].append(data_nascimento)
        informacao_paciente['pressao_arterial'].append(pressao_arterial)
        
        numPacientes = numPacientes + 1
         

    #Relatorio geral
    if menuop == '2':
        
        print("Nome \t Data de Nascimento \t Pressão Arterial")
        print()
        
        for i in range(numPacientes):              
            
            print("{0} \t {1} \t {2}".format(informacao_paciente['nome'][i],informacao_paciente['data_nascimento'][i],informacao_paciente['pressao_arterial'][i]))    

    #Altera dados paciente  
    if menuop == '3':

        menu_altera_informacoes = True
        while menu_altera_informacoes:

            print('''
            [1] nome
            [2] ano de nascimento
            [3] pressão arterial
            [4] voltar ''')

            menuAlteracao = input ("\nDigite o numero da opçao desejada: ")

            #Altera nome paciente
            if menuAlteracao == '1':
                consulta_paciente = input ("\nInforme o nome do paciente: ")
                procura_paciente_nome = consulta_paciente in informacao_paciente['nome']
                
                if procura_paciente_nome == True:                   
                    newnome = input ("Informe o novo nome do paciente: ")
                    pos = informacao_paciente['nome'].index(consulta_paciente)
                    informacao_paciente['nome'][pos] = newnome
                    print("\nDados atualizados!!!\n")

            #Altera ano de nascimento
            if menuAlteracao == '2':
                consulta_paciente = input("\nInforme o nome do paciente: ")
                procura_paciente_nome = consulta_paciente in informacao_paciente['nome']
                
                if procura_paciente_nome == True:
                    newdata_nascimento = input ("Informe a nova data de nascimento do paciente: ")
                    informacao_paciente['data_nascimento'][pos] = newdata_nascimento
                    print("\nDados atualizados!!!\n")

            #Altera pressão arterial
            if menuAlteracao == '3':
                consulta_paciente = input("\nInforme o nome do paciente: ")
                procura_paciente_nome = consulta_paciente in informacao_paciente['nome']

                if procura_paciente_nome == True:
                    newpressao_arterial = input ("Informe o novo valor de pressão arterial: ")
                    informacao_paciente['pressao_arterial'][pos] = newpressao_arterial    
                    print("\nDados atualizados!!!\n")

            #Volta ao menu principal
            if menuAlteracao == '4':
                menu_altera_informacoes = False

    # Remover paciente
    if menuop == '4':
        
        consulta_paciente = input ("\nInforme o nome: ")
        procura_paciente_nome = consulta_paciente in informacao_paciente['nome']
        
        if procura_paciente_nome == True:
            
            pos = informacao_paciente['nome'].index(consulta_paciente)
            informacao_paciente['nome'].pop(pos)
            informacao_paciente['data_nascimento'].pop(pos)
            informacao_paciente['pressao_arterial'].pop(pos)
            numPacientes = numPacientes - 1
            print("Removido com sucesso")
        else:
            print("Nome invalido!!!")
                                
print ("Finalizando...")