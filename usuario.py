import sqlite3
class Usuario():
    def __init__(self, cursor, login, **kwargs):
        if login == True:
            query = f"""SELECT * FROM usuarios WHERE email=='{kwargs["email"]}' and senha=='{kwargs["senha"]}'"""
            x = cursor.execute(query)
            print(x)
        else:
            query = """CREATE TABLE IF NOT EXISTS usuarios(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT,
                                    sobrenome TEXT,
                                    email TEXT UNIQUE,
                                    telefone TEXT,
                                    cpf TEXT,
                                    senha TEXT);"""

            cursor.execute(query)
            query = f"""INSERT INTO clientes(nome, sobrenome, email, telefone, cpf, senha) VALUES('{kwargs["nome"]}',
                        '{kwargs["sobrenome"]}', '{kwargs["email"]}','{kwargs["telefone"]}','{kwargs["cpf"]}', 
                        '{kwargs["senha"]}');"""
            cursor.execute(query)
            self.__nome = kwargs["nome"]
            self.__sobrenome = kwargs["sobrenome"]
            self.__email = kwargs["email"]
            self.__telefone = kwargs["telefone"]
            self.__cpf = kwargs["cpf"]
            self.__senha = kwargs["senha"]


connection = sqlite3.connect("pizzaria_model_tech.db")
cursor = connection.cursor()
g = Usuario(cursor, False, nome="Marcelo", sobrenome="Medeiros", email="email@hotmail.com", telefone="12345"
            ,cpf="424324324", senha="dewaffw")
