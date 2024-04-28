# projectfinal

"""
Sistema de Gestão de Tickets

Este script Python permite aos utilizadores criar, consultar e editar tickets de hardware e software
numa base de dados MySQL.

O sistema é composto pelas seguintes classes:

- TicketState: Enumeração que representa os estados de um ticket.
- AtendimentoState: Enumeração que representa os estados de um atendimento.
- Ticket: Classe base que representa um ticket genérico.
- HardwareTicket: Classe que representa um ticket de hardware.
- SoftwareTicket: Classe que representa um ticket de software.
- TicketDatabase: Classe que gere a conexão e operações com a base de dados.
"""

import mysql.connector
from enum import Enum
from datetime import datetime

class TicketState(Enum):
    """Enumeração que representa os estados de um ticket."""
    POR_ATENDER = 1
    EM_ATENDIMENTO = 2
    ATENDIDO = 3

class AtendimentoState(Enum):
    """Enumeração que representa os estados de um atendimento."""
    ABERTO = 1
    RESOLVIDO = 2
    NAO_RESOLVIDO = 3

class Ticket:
    """Classe base que representa um ticket genérico."""
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado):
        ...

class HardwareTicket(Ticket):
    """Classe que representa um ticket de hardware."""
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 equipamento, avaria, descricao_reparacao, estado_hardware):
        ...

class SoftwareTicket(Ticket):
    """Classe que representa um ticket de software."""
    def __init__(self, numero_sequencial, data_hora, codigo_colaborador, estado,
                 software, descricao_necessidade, estado_software):
        ...

class TicketDatabase:
    """Classe que gere a conexão e operações com a base de dados."""
    def __init__(self, host, user, password, database):
        ...

def perguntar_servico():
    """Função principal que gere a interação com o utilizador."""
    ...

def criar_ticket_a():
    """Cria um novo ticket conforme a escolha do utilizador."""
    ...

def criar_ticket_hardware():
    """Cria um novo ticket de hardware."""
    ...

def criar_ticket_software():
    """Cria um novo ticket de software."""
    ...

def consultar_ticket():
    """Consulta os tickets conforme a escolha do utilizador."""
    ...

def consultar_ticket_hardware():
    """Consulta os tickets de hardware."""
    ...

def consultar_ticket_software():
    """Consulta os tickets de software."""
    ...

def editar_ticket_hardware(numid):
    """Edita um ticket de hardware."""
    ...

def editar_ticket_software(numid):
    """Edita um ticket de software."""
    ...

# Inicia a interação com o utilizador ao executar o script
perguntar_servico()
