from models import Usuario
class fazer_login:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1
    
    def buscar_email(self, email):
        for e in self.usuarios:
            if e.email == email:
                return e
        return None
    
    def cadastro(self, nome, email, senha):
        if self.buscar_email(email):
            print("E-mail já cadastrado!")
            return None
        user = Usuario(self.proximo_id, nome, email, senha)
        self.usuarios.append(user)
        self.proximo_id += 1
        return user
    
    def login(self, email, senha):
        user = self.buscar_email(email)
        if not user:
            print("Usuário não encontrado!")
        return None
        
        if user.senha != senha:
            print("Senha incorreta!")
        return None
    
        return user
        

        
