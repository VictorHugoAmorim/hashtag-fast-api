from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeingKey
from sqlalchemy.orm import declarative_base

# cria a conexao com o banco
db = create_engine("sqlite:///banco.db")
# cria a base do bancode dados
Base = declarative_base()

# Criar as classses/tabelas do banco
# usuario
# pedido
# ItensPedido

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=True)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.mnome = nome
        self.email = email