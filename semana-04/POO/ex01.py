class Carro:
    ligado: bool
    desligado: bool
    cor: str
    velocidade: int

    def __init__(self, ligado, desligado, cor, velocidade):
        self.ligado = ligado
        self.desligado = desligado
        self.cor = cor
        self.velocidade = velocidade

    def liga(self):
        if (self.ligado):
            print("O carro já está ligado")
        else:
            print("Carro ligado")
            self.ligado = True
            self.desligado = False
    
    def desliga(self):
        if (self.desligado):
            print("O carro já está desligado")
        else:
            self.ligado = False
            self.desligado = True
            print("Carro desligado")

    def acelera(self):
        self.velocidade += 10
        print(f"{self.velocidade} km/h")

    def desacelera(self):
        if (self.velocidade >= 10):
            self.velocidade -= 10
            print(f"{self.velocidade} km/h")
        else:
            print("O carro já está parado.")

classic = Carro(False, True, "prata", 0)

classic.liga()
classic.liga()
classic.acelera()
classic.acelera()
classic.desacelera()
classic.desacelera()
classic.desacelera()
classic.desliga()
