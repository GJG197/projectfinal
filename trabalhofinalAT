import mysql.connector
from enum import Enum
from datetime import datetime

class TicketState(Enum):
    POR_ATENDER = 1
    EM_ATENDIMENTO = 2
    ATENDIDO = 3

class AtendimentoState(Enum):
    ABERTO = 1
    RESOLVIDO = 2
    NAO_RESOLVIDO = 3

class Ticket:
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado):
        self.numero_sequencial = numero_sequencial
        self.data_hora = data_hora
        self.codigo_colaborador = codigo_colaborador
        self.estado = estado

class HardwareTicket(Ticket):
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 equipamento, avaria, descricao_reparacao, estado_hardware):
        super().__init__(numero_sequencial, data_hora, codigo_colaborador, estado)
        self.equipamento = equipamento
        self.avaria = avaria
        self.descricao_reparacao = descricao_reparacao
        self.estado_hardware = estado_hardware

    def atualizar_estado_hardware(self, novo_estado):
        self.estado_hardware = novo_estado

class SoftwareTicket(Ticket):
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 software, descricao_necessidade, estado_software):
        super().__init__(numero_sequencial, data_hora, codigo_colaborador, estado)
        self.software = software
        self.descricao_necessidade = descricao_necessidade
        self.estado_software = estado_software

    def atualizar_estado_software(self, novo_estado):
        self.estado_software = novo_estado

class TicketDatabase:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def criar_ticket(self, ticket):
        if isinstance(ticket, HardwareTicket):
            query = ("INSERT INTO hardware_tickets (numero_sequencial, data_hora, codigo_colaborador,"
                     " equipamento, avaria, descricao_reparacao, estado_hardware) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            values = (ticket.numero_sequencial, ticket.data_hora, ticket.codigo_colaborador,
                      ticket.equipamento, ticket.avaria, ticket.descricao_reparacao, ticket.estado_hardware.value)
        elif isinstance(ticket, SoftwareTicket):
            query = ("INSERT INTO software_tickets (numero_sequencial, data_hora, codigo_colaborador,"
                     " software, descricao_necessidade, estado_software) VALUES (%s, %s, %s, %s, %s, %s)")
            values = (ticket.numero_sequencial, ticket.data_hora, ticket.codigo_colaborador,
                      ticket.software, ticket.descricao_necessidade, ticket.estado_software.value)
        else:
            return False

        self.cursor.execute(query, values)
        self.conn.commit()
        return True

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

def perguntar_servico():
    while True:
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
    
    numero_sequencial = input("Numero sequencial:")
    codigo_colaborador = input("Indique o seu numero de colaborador:")
    equipamento = input("Qual o seu equipamento:")
    avaria = input("Que tipo de avaria:")
    descricao_reparacao = input("Descrição da reparação:")
    estado_hardware_input = input("Estado do Hardware (1 - POR_ATENDER | 2 - EM_ATENDIMENTO | 3 - ATENDIDO):")
    estado_hardware = TicketState(int(estado_hardware_input))
    
    hardware_ticket = HardwareTicket(
        numero_sequencial=numero_sequencial,
        data_hora=datetime.now(),
        codigo_colaborador=codigo_colaborador,
        estado=estado_hardware,
        equipamento=equipamento,
        avaria=avaria,
        descricao_reparacao=descricao_reparacao,
        estado_hardware=estado_hardware
    )
    
    db.criar_ticket(hardware_ticket)
    perguntar_servico()

def criar_ticket_software():
    db = TicketDatabase(host="localhost", user="root", password="", database="trabalhofinal2")
    
    numero_sequencial = input("Numero sequencial:")
    codigo_colaborador = input("Indique o seu numero de colaborador:")
    software = input("Qual o seu software:")
    descricao_necessidade = input("Descrição da necessidade:")
    estado_software_input = input("Estado do Software (1 - POR_ATENDER | 2 - EM_ATENDIMENTO | 3 - ATENDIDO):")
    estado_software = TicketState(int(estado_software_input))
    
    software_ticket = SoftwareTicket(
        numero_sequencial=numero_sequencial,
        data_hora=datetime.now(),
        codigo_colaborador=codigo_colaborador,
        estado=estado_software,
        software=software,
        descricao_necessidade=descricao_necessidade,
        estado_software=estado_software
    )
    
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

    query = "SELECT * FROM hardware_tickets"
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]

    print("\nID\t|\tNúmero Sequencial\t|\tData e Hora\t|\tCódigo Colaborador\t|\tEquipamento\t|\tAvaria\t|\tDescrição Reparação\t|\tEstado Hardware")
    print("-" * 120)

    for row in cursor.fetchall():
        print("\t|\t".join(str(value) for value in row))

    print("-" * 120)

    cursor.close()
    conn.close()

    nextpage = input("(1 - Editar ticket | 2 - Retroceder | 0 - Fechar)")
    if nextpage == "1":
        numid = input("Indique qual o Id que necessita de editar:")
        editar_ticket_hardware(numid)
    elif nextpage == "2":
        consultar_ticket()
    elif nextpage == "0":
        exit()
    else:
        print("Opção Inválida")

def consultar_ticket_software():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    query = "SELECT * FROM software_tickets"
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]

    print("\nID\t|\tNúmero Sequencial\t|\tData e Hora\t|\tCódigo Colaborador\t|\tSoftware\t|\tDescrição Necessidade\t|\tEstado Software")
    print("-" * 120)

    for row in cursor.fetchall():
        print("\t|\t".join(str(value) for value in row))

    print("-" * 120)

    cursor.close()
    conn.close()

    nextpage = input("(1 - Editar ticket | 2 - Retroceder | 0 - Fechar)")
    if nextpage == "1":
        numid = input("Indique qual o Id que necessita de editar:")
        editar_ticket_software(numid)
    elif nextpage == "2":
        consultar_ticket()
    elif nextpage == "0":
        exit()
    else:
        print("Opção Inválida")

def editar_ticket_hardware(numid):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    query = "SELECT * FROM hardware_tickets WHERE id = %s"
    cursor.execute(query, (numid,))
    ticket = cursor.fetchone()

    if ticket:
        print("Registro encontrado:")
        columns = [column[0] for column in cursor.description]

        print("\t|\t".join(columns))
        print("\t|\t".join(str(value) for value in ticket))

        equipamento = input("Novo equipamento: ")
        avaria = input("Nova avaria: ")
        descricao_reparacao = input("Nova descrição de reparação: ")
        estado_hardware_input = input("Novo estado do hardware (1 - POR_ATENDER | 2 - EM_ATENDIMENTO | 3 - ATENDIDO):")
        estado_hardware = TicketState(int(estado_hardware_input))

        update_query = ("UPDATE hardware_tickets SET equipamento = %s, avaria = %s, "
                        "descricao_reparacao = %s, estado_hardware = %s WHERE id = %s")
        update_values = (equipamento, avaria, descricao_reparacao, estado_hardware.value, numid)
        cursor.execute(update_query, update_values)
        conn.commit()

        print("Registro atualizado com sucesso!")
    else:
        print("Registro não encontrado.")
        consultar_ticket_hardware()

    cursor.close()
    conn.close()

    perguntar_servico()

def editar_ticket_software(numid):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="trabalhofinal2")
    cursor = conn.cursor()

    query = "SELECT * FROM software_tickets WHERE id = %s"
    cursor.execute(query, (numid,))
    ticket = cursor.fetchone()
    
    if ticket:
        print("Registro encontrado:")
        columns = [column[0] for column in cursor.description]

        print("\t|\t".join(columns))
        print("\t|\t".join(str(value) for value in ticket))

        software = input("Novo software: ")
        descricao_necessidade = input("Nova descrição de necessidade: ")
        estado_software_input = input("Novo estado do software (1 - POR_ATENDER | 2 - EM_ATENDIMENTO | 3 - ATENDIDO):")
        estado_software = TicketState(int(estado_software_input))

        update_query = ("UPDATE software_tickets SET software = %s,"
                        " descricao_necessidade = %s, estado_software = %s WHERE id = %s")
        update_values = (software, descricao_necessidade, estado_software.value, numid)
        cursor.execute(update_query, update_values)
        conn.commit()

        print("Registro atualizado com sucesso!")
    else:
        print("Registro não encontrado.")
        consultar_ticket_software()

    cursor.close()
    conn.close()
    perguntar_servico()
    
perguntar_servico()
