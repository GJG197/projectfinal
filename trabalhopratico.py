'''-------------------------Librarias Necessárias------------------------------------'''

import mysql.connector
from enum import Enum
from datetime import datetime

'''-------------------------Criação de Classes---------------------------------------'''
# Definindo enumerações para os estados do ticket e do atendimento


class TicketState(Enum):
    POR_ATENDER = 1
    EM_ATENDIMENTO = 2
    ATENDIDO = 3


class AtendimentoState(Enum):
    ABERTO = 1
    RESOLVIDO = 2
    NAO_RESOLVIDO = 3

# Classe base para os tickets


class Ticket:
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado):
        self.numero_sequencial = numero_sequencial
        self.data_hora = data_hora
        self.codigo_colaborador = codigo_colaborador
        self.estado = estado

# Classe para tickets de serviços de hardware


class HardwareTicket(Ticket):
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 equipamento, avaria, descricao_reparacao, estado_hardware):
        super().__init__(numero_sequencial, data_hora, codigo_colaborador, estado)
        self.equipamento = equipamento
        self.avaria = avaria
        self.descricao_reparacao = descricao_reparacao
        self.estado_hardware = estado_hardware


# Classe para tickets de serviços de software
class SoftwareTicket(Ticket):
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 software, descricao_necessidade, estado_software):
        super().__init__(numero_sequencial, data_hora, codigo_colaborador, estado)
        self.software = software
        self.descricao_necessidade = descricao_necessidade
        self.estado_software = estado_software

# Classe para gerenciar a base de dados de tickets


class TicketDatabase:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def criar_ticket(self, ticket):
        if isinstance(ticket, HardwareTicket):
            query = ("INSERT INTO hardware_tickets (numero_sequencial, data_hora, codigo_colaborador,"
                     " equipamento, avaria, descricao_reparacao, estado_hardware) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            values = (ticket.numero_sequencial, ticket.data_hora, ticket.codigo_colaborador,
                      ticket.equipamento, ticket.avaria, ticket.descricao_reparacao, ticket.estado_hardware)
        elif isinstance(ticket, SoftwareTicket):
            query = ("INSERT INTO software_tickets (numero_sequencial, data_hora, codigo_colaborador,"
                     " software, descricao_necessidade, estado_software) VALUES (%s, %s, %s, %s, %s, %s)")
            values = (ticket.numero_sequencial, ticket.data_hora, ticket.codigo_colaborador,
                      ticket.software, ticket.descricao_necessidade, ticket.estado_software)
        else:
            return False

        self.cursor.execute(query, values)
        self.conn.commit()
        return True

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()


'''-------------------------Menu dos Tickets---------------------------------------'''


def perguntar_servico():
    while 1:
        decisao1 = input("Qual serviço pretender realizar? (1 - Criar ticket | 2 - Consultar ticket | 0 - Fechar)")
        if decisao1 == "1":
            criar_ticket_a()
            break
        elif decisao1 == "2":
            consultar_ticket()
            break
        elif decisao1 == "0":
            exit()
        else:
            print("Opção Inválida")


def criar_ticket_a():
    while True:
        decisao2 = input("Qual o ticket a criar? (1 - Hardware | 2 - Software | 3 - Retroceder | 0 - Fechar)")
        if decisao2 == "1":
            criar_ticket_hardware()
            break
        elif decisao2 == "2":
            criar_ticket_software()
            break
        elif decisao2 == "3":
            perguntar_servico()
            break
        elif decisao2 == "0":
            exit()
        else:
            print("Opção Inválida")


def criar_ticket_hardware():
    db = TicketDatabase(host="localhost", user="root", password="", database="trabalhofinal2")
    hardware_ticket = HardwareTicket(numero_sequencial=input("Numero sequencial:"), data_hora=datetime.now(),
                                     codigo_colaborador=input("Indique o seu numero de colaborador:"),
                                     estado=TicketState.POR_ATENDER,
                                     equipamento=input("Qual o seu equipamento:"),
                                     avaria=input("Que tipo de avaria:"),
                                     descricao_reparacao=input("Descrição da reparação:"),
                                     estado_hardware=input("Estado do Hardware:"))
    db.criar_ticket(hardware_ticket)
    perguntar_servico()


def criar_ticket_software():
    db = TicketDatabase(host="localhost", user="root", password="", database="trabalhofinal2")
    software_ticket = SoftwareTicket(numero_sequencial=input("Numero sequencial:"), data_hora=datetime.now(),
                                     codigo_colaborador=input("Indique o seu numero de colaborador:"),
                                     estado=TicketState.POR_ATENDER, software=input("Qual o seu software:"),
                                     descricao_necessidade=input("Descrição da necessidade:"),
                                     estado_software=input("Estado do Hardware:"))
    db.criar_ticket(software_ticket)
    perguntar_servico()


def consultar_ticket():
    while True:
        decisao2 = input("Qual o tipo de ticket pretender consultar? (1 - Hardware |"
                         " 2 - Software | 3 - Retroceder | 0 - Fechar)")
        if decisao2 == "1":
            consultar_ticket_hardware()
            break
        elif decisao2 == "2":
            consultar_ticket_software()
            break
        elif decisao2 == "3":
            perguntar_servico()
            break
        elif decisao2 == "0":
            exit()
        else:
            print("Opção Inválida")
            break


def consultar_ticket_hardware():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    # Consultar los registros de la tabla hardware_tickets
    query = "SELECT * FROM hardware_tickets"
    cursor.execute(query)

    # Obtener los nombres de las columnas
    columns = [column[0] for column in cursor.description]

    # Imprimir encabezados
    print("\nID\t|\tNúmero Sequencial\t|\tData e Hora\t|\tCódigo Colaborador\t|\tEquipamento\t|\tAvaria\t|\tDescrição Reparação\t|\tEstado Hardware")
    print("-" * 120)  # Separador

    # Imprimir registros
    for row in cursor.fetchall():
        print("\t|\t".join(str(value) for value in row))

    print("-" * 120)  # Separador

    # Cerrar la conexión
    cursor.close()
    conn.close()

    nextpage = input("(1 - Editar ticket | 2 - Retroceder | 0 - Fechar)")
    if nextpage == "1":
        numid = input("Indique qual o Id que necessita de editar:")
        editar_ticket_hardware(numid)
    elif nextpage == "2":
        consultar_ticket()  # query para dar update da tabela hardware
    elif nextpage == "0":
        exit()
    else:
        print("Opção Inválida")


def consultar_ticket_software():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    # Consultar los registros de la tabla software_tickets
    query = "SELECT * FROM software_tickets"
    cursor.execute(query)

    # Obtener los nombres de las columnas
    columns = [column[0] for column in cursor.description]

    # Imprimir encabezados
    print("\nID\t|\tNúmero Sequencial\t|\tData e Hora\t|\tCódigo Colaborador\t|\tSoftware\t|\tDescrição Necessidade\t|\tEstado Software")
    print("-" * 120)  # Separador

    # Imprimir registros
    for row in cursor.fetchall():
        print("\t|\t".join(str(value) for value in row))

    print("-" * 120)  # Separador

    # Cerrar la conexión
    cursor.close()
    conn.close()

    nextpage = input("(1 - Editar ticket | 2 - Retroceder | 0 - Fechar)")
    if nextpage == "1":
        numid = input("Indique qual o Id que necessita de editar:")
        editar_ticket_software(numid)  # query para dar update da tabela software
    elif nextpage == "2":
        consultar_ticket()
    elif nextpage == "0":
        exit()
    else:
        print("Opção Inválida")



def editar_ticket_hardware(numid):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    # Consultar o registro com o ID especificado
    query = "SELECT * FROM hardware_tickets WHERE id = %s"
    cursor.execute(query, (numid,))
    ticket = cursor.fetchone()

    if ticket:
        print("Registro encontrado:")
        columns = [column[0] for column in cursor.description]

        # Exibir os cabeçalhos
        print("\t|\t".join(columns))
        print("\t|\t".join(str(value) for value in ticket))

        # Solicitar novos valores ao usuário
        equipamento = input("Novo equipamento: ")
        avaria = input("Nova avaria: ")
        descricao_reparacao = input("Nova descrição de reparação: ")
        estado_hardware = input("Novo estado do hardware: ")

        # Executar a consulta SQL UPDATE para modificar o registro
        update_query = ("UPDATE hardware_tickets SET equipamento = %s, avaria = %s, "
                        "descricao_reparacao = %s, estado_hardware = %s WHERE id = %s")
        update_values = (equipamento, avaria, descricao_reparacao, estado_hardware, numid)
        cursor.execute(update_query, update_values)
        conn.commit()

        print("Registro atualizado com sucesso!")
    else:
        print("Registro não encontrado.")
        consultar_ticket_hardware()

    # Fechar a conexão
    cursor.close()
    conn.close()


def editar_ticket_software(numid):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    # Consultar o registro com o ID especificado
    query = "SELECT * FROM software_tickets WHERE id = %s"
    cursor.execute(query, (numid,))
    ticket = cursor.fetchone()

    if ticket:
        print("Registro encontrado:")
        columns = [column[0] for column in cursor.description]

        # Exibir os cabeçalhos
        print("\t|\t".join(columns))
        print("\t|\t".join(str(value) for value in ticket))

        # Solicitar novos valores ao usuário
        software = input("Novo software: ")
        descricao_necessidade = input("Nova descrição de necessidade: ")
        estado_software = input("Novo estado do software: ")

        # Executar a consulta SQL UPDATE para modificar o registro
        update_query = ("UPDATE software_tickets SET software = %s,"
                        " descricao_necessidade = %s, estado_software = %s WHERE id = %s")
        update_values = (software, descricao_necessidade, estado_software, numid)
        cursor.execute(update_query, update_values)
        conn.commit()

        print("Registro atualizado com sucesso!")
    else:
        print("Registro não encontrado.")
        consultar_ticket_hardware()

    # Fechar a conexão
    cursor.close()
    conn.close()


'''-------------------------Main---------------------------------------'''

perguntar_servico()
