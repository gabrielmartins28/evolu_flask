#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK

from uuid import uuid4

from sqlalchemy import String, text
from sqlalchemy.dialects.postgresql import uuid

from db import db

class Book(db.Model):
#indicar que book é um modelo gerenciado pelo sqlalchemy
    __tablename__ = "book"
    #define o nome da tabela 
    id = db.column(
        UUID(as_uuid = True), # Vou usar o UUID
        primary_key = True, #Chave primaria
        default = uuid4 #Quando criar um novo livro, um UUID será criado 
    )

    title = db.Column(
        String(255), #Recebe a string 
        nullable = False #Não aceita nulo 
    )
    author = db.Column(
        String(255),
        nullable=False
    )
    #Title e author são obrigatórios
    description = db.Column(
        Text, #Textos maiores
        nullable = False

    )

    is_favorite = db.column(
        db.Boolean,
        nullable = False,
        default = False

    )

    is_reading = db.Column(
        db.boolean,
        nullable = False,
        default = False

    )

    is_finished = db.Column(
        db.boolean,
        nullable = False,
        default = False
    
        )

    #Transformando o modelo em dicionario

    """
    POR ISSO SERÁ CRIADO UM MÉTODO RESPONSÁVEL POR TRANSFORMAR O OBJETO BOOK EM UM DICIONÁRIO PYTHON

    QUANDO OCORRER UMA CONSULTA AO NOSSO SISTEMA ELE RETORNA UM OBJETO BOOK, ELE NÃO É SIMPLESMENTE UM DICT PYTHON.
    O Método AS_DICT() FUNCIONAR COMO UMA CAMADA DE CONVERSÃO, SELECIONANDO APENAS O NECESSÁRIO PARA SER EXPOSTO PELA API
    E TRANSFORMANDO EM UM DICT, ESTRUTURA QUE PODE SER FACILMENTE SERIALIZADA PARA JSON NA RESPOSTA HTTP
    """


    def as_dict(self):
        return {
            "id":str(self.id),
            "title":self.title,
            "author":self.author,
            "description":self.description,
            "is_favorite":self.is_favorite,
            "is_reading":self.is_reading,
            "is_finished":self.is_finished
        }


    