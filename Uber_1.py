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




if __name__ == '__main__':

    cliente1 = UberBlack()
    cliente2 = UberX()
    cliente3 = UberMoto()
    cliente4 = UberFlash()

    cliente1.solicitacao_cliente()
    cliente2.solicitacao_cliente()
    cliente3.solicitacao_cliente()
    cliente4.solicitacao_cliente()
