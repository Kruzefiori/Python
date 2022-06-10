class Username_Duplicado(Exception):
    pass
class Idade_Menor_Que_Permitida(Exception):
    pass
class Idade_Invalida(Exception):
    pass
class Email_Invalido(Exception):
    pass
class User:
    def __init__(self , userName , email):
        self.__userName = userName
        self.__email = email

    def getUserName(self):
        return self.__userName

    def getEmail(self):
        return self.__email
if __name__ == '__main__':
    cadastro = {}
    listaExemplo = [
        ("paulo" , "paulo@gmail.com" , 21),
        ("maria" , "maria@gmail.com" , 19),
        ("antonio" , "antonio@gmail.com" , 25),
        ("pedro" , "pedro@gmail.com" , 15),
        ("marisa" , "marisa@" , 23),
        ("ana" , "ana@gmail.com" , -22),
        ("maria" , "maria@gmail.com" , 27),
    ]
    for username, email, idade in listaExemplo:
        try:
            if username in cadastro:
                raise Username_Duplicado()
            if idade < 0:
                raise Idade_Invalida()
            if idade < 18:
                raise Idade_Menor_Que_Permitida()
            emailPartes =email.split('@')
            if len(emailPartes) < 2 or not emailPartes[0] or not emailPartes[1]:
                raise Email_Invalido()
        except Username_Duplicado:
            print("Usuário %s já está em uso" %username)
        except Idade_Invalida:
            print("Idade inválida %d " %idade)
        except Idade_Menor_Que_Permitida:
            print("Idade Menor que a permitida %s " %idade)
        except Email_Invalido:
            print("Email inválido %s " %email)
        else:
            cadastro[username] = User(username , email)
            print("Usuário %s cadastrado com sucesso " %username)
