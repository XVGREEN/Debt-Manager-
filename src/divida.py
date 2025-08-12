from datetime import datetime

class Sujeito:
    def __init__(self,nome,numero):
        self.nome= nome  
        self.numero= numero
        

class Divida:
    def __init__(self, sujeito, prazo, quantidade):
        self.sujeito = sujeito
        self.prazo = datetime.strptime(prazo, "%d/%m/%Y")
        self.quantidade = quantidade
    
    def __str__(self):
        prazo_formatado = self.prazo.strftime("%d/%m/%Y")
        return f"Sujeito: {self.sujeito.nome}   |   Prazo: {prazo_formatado}  |  Quantidade: {self.quantidade}  |  Numero:{self.sujeito.numero}"



