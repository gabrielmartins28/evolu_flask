#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK

from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    title = db.Column(
        String(255),
        nullable=False
    )

    author = db.Column(
        String(255),
        nullable=False
    )

    description = db.Column(
        Text,
        nullable=False
    )

    is_favorite = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    is_reading = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    is_finished = db.Column(
        db.Boolean,
        nullable=False,
        default=False
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


    