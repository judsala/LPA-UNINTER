#VARIÁVEIS GLOBAIS
employee_list = [] 
employee_id = 0 

#FUNÇÕES
def employee_registration(id): #função para cadastrar funcionário
    print('\n' + '-' * 15 + ' MENU CADASTRAR FUNCIONÁRIO ' + '-' * 15)
    print('Id do funcionário: {}' .format(id)) 
    name = input('Entre com o nome do funcionário: ') 
    department = input('Entre com o departmento do funcionário: ') 
    salary = int(input('Entre com o SALÁRIO do funcionário (R$): ')) 
    employee_dictionary =     {'id'            : id,
                               'nome'          : name,
                               'departamento'  : department,
                               'salário'       : salary}
    employee_list.append(employee_dictionary.copy()) 

def employee_check(): #função para consultar os funcionários cadastrados
    print('\n' + '-' * 15 + ' MENU CONSULTAR FUNCIONÁRIO ' + '-' * 15)
    while True: 
        check_option = input('Escolha a opção desejada:\n' +
                                '1 - Consultar Todos os Funcionários\n' +
                                '2 - Consultar Funcionários por ID\n' +
                                '3 - Consultar Funcionários por department\n' +
                                '4 - Retornar\n' +
                                '>>> ')
        if check_option == '1':
            for employees in employee_list: 
                print('-' * 15)
                for key, value in employees.items(): 
                    print('{}: {}' .format(key, value))
                print('-' * 15)
        elif check_option == '2':
            id_option = int(input('Digite o ID do funcionário: '))
            for employees in employee_list:
                if employees['id'] == id_option: 
                    print('-' * 15)
                    for key, value in employees.items():  
                        print('{}: {}'.format(key, value))
                    print('-' * 15)
        elif check_option == '3':
            department_option = input('Digite o department do(s) funcionário(s): ')
            for employees in employee_list:
                if employees['department'] == department_option:  
                    print('-' * 15)
                    for key, value in employees.items():  
                        print('{}: {}'.format(key, value))
                    print('-' * 15)
        elif check_option == '4':
            return 
        else:
            print('Opção inválida! Tente novamente...')
            continue  

def delete_employee(): #função para remover funcionário
    print('\n' + '-' * 15 + ' MENU REMOVER FUNCIONÁRIO ' + '-' * 15)
    id_option = int(input('Digite o ID do funcionário a ser removido: ')) 
    for employees in employee_list:
        if employees['id'] == id_option:  
            print('-' * 15)
            employee_list.remove(employees) 
            print('Funcionário removido com sucesso.')
            print('-' * 15)

#PROGRAMA PRINCIPAL
print('Welcome to my Company!')
print('*' * 60 + '\n')
while True:
    print('\n' + '-' * 20 + ' MENU PRINCIPAL ' + '-' * 20)
    main_option = input('Escolha a opção desejada:\n' +
                                '1 - Cadastrar Funcionário\n' +
                                '2 - Consultar Funcionário(s)\n' +
                                '3 - Remover Funcionário\n' +
                                '4 - Sair\n' +
                                '>>> ')
    if main_option == '1':
        employee_id += 1 
        employee_registration(employee_id) 
    elif main_option == '2':
        employee_check()
    elif main_option == '3':
        delete_employee() 
    elif main_option == '4':
        break 
    else:
        print('Opção inválida! Tente novamente...')
        continue