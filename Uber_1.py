from abc import ABC,abstractmethod

class Veiculo(ABC):
    def __init__(self,tipo):
        self.veiculo = tipo
    
    @abstractmethod
    def BuscarCliente(self):
        pass


class Moto(Veiculo):
    def __init__(self,tipo,modelo,placa,cor):
        super().__init__(tipo)
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
    
    def BuscarCliente(self):
        print(f'|Moto: {self.modelo} - Placa: {self.placa} - Cor: {self.cor}| Buscando o cliente...')

class CarroPopular(Veiculo):
    def __init__(self,tipo,modelo,placa,cor):
        super().__init__(tipo)
        self.modelo = modelo
        self.placa = placa
        self.cor = cor

    def BuscarCliente(self):
        print(f'|Carro: {self.modelo} - Placa: {self.placa} - Cor: {self.cor}| Buscando o cliente...')

class CarroLuxo(Veiculo):
    def __init__(self,tipo,modelo,placa,cor):
        super().__init__(tipo)
        self.modelo = modelo
        self.placa = placa
        self.cor = cor

    def BuscarCliente(self):
        print(f'|Carro: {self.modelo} - Placa: {self.placa} - Cor: {self.cor}| Buscando o cliente...')



if __name__ == '__main__':

    cliente1 = Moto('Honda','CG125','YAH7709','Vermelho')
    cliente2 = CarroLuxo('Chevrolet','Camaro','ABC9911','Amarelo')
    cliente3 = CarroPopular('Fiat','Uno','JJTP3368','Branco')

    cliente1.BuscarCliente()
    cliente2.BuscarCliente()
    cliente3.BuscarCliente()
