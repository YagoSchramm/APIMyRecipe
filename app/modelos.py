from . import firebase
class Usuario:
    def __init__(self,nome,email,senha,culinaria):
        self.nome=nome
        self.email=email
        self.senha=senha
        self.culinaria=culinaria
    def salvaNoFirebase(self):
        user_ref= firebase.collection('usuarios').document(self.email)
        user_ref.set({
            'nome':self.nome,
            'email':self.email,
            'senha':self.senha,
            'culinaria':self.culinaria,
        })
    @staticmethod
    def getUsuarioByEmail(email):
        user_ref=firebase.collection('usuarios').document(email)
        user= user_ref.get()
        if user.exists:
            return user.to_dict()
        else:
            return None
class Receita:
    def __init__(self,titulo,ingredientes,preparo,usuario_email):
        self.titulo=titulo
        self.ingredientes=ingredientes
        self.preparo=preparo
        self.usuario_email=usuario_email
    def salvaNoFirebase(self):
        receita_ref=firebase.collection('receitas').document()
        receita_ref.set({
            'titulo':self.titulo,
            'ingredientes':self.ingredientes,
            'preparo':self.preparo,
            'usuario_email':self.usuario_email,
        })