from abc import ABC, abstractmethod

class Uber(ABC):
    @abstractmethod
    def solicitacao_cliente(self) -> None: pass


class UberBlack(Uber):
    def solicitacao_cliente(self) -> None:
        print('\033[1;35m|Uber Black|\033[m Está buscando o cliente...')


class UberX(Uber):
    def solicitacao_cliente(self) -> None:
        print('\033[1;33m|Uber-X|\033[m Está buscando o cliente...')


class UberMoto(Uber):
    def solicitacao_cliente(self) -> None:
        print('\033[1;36m|Uber Moto|\033[m Está buscando o cliente...')


class UberFlash(Uber):
    def solicitacao_cliente(self) -> None:
        print('\033[1;32m|Uber Flash|\033[m Realizando entrega para o cliente...')


class UberFactory:
    def __init__(self, tipo) -> None:
        self.carro = self.get_Uber(tipo)

    @staticmethod
    def get_Uber(tipo: str) -> Uber:
        if tipo == 'Uber Black':
            return UberBlack()
        if tipo == 'Uber X':
            return UberX()
        if tipo == 'Uber Moto':
            return UberMoto()
        if tipo == 'Uber Flash':
            return UberFlash()
        assert 0, 'Veículo não existe'

    def solicitacao_cliente(self) -> None:
        self.carro.solicitacao_cliente()


if __name__ == "__main__":
    from random import choice
    #------ INTERFACE ------#
    carros_disponiveis = ['Uber Black', 'Uber X', 'Uber Moto' , 'Uber Flash'] 

    for i in range(10):
        carro = UberFactory(choice(carros_disponiveis))
        carro.solicitacao_cliente()
 























