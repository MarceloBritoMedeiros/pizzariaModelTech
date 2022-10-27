from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Pedido(Subject):
    _id = randint(0, 300)
    _pizza = None
    _state: str = None
    _historico_state = []
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject adicionado")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notificando observers...")
        for observer in self._observers:
            observer.update(self)

    def adicionarPedido(self, pizza):
        self._pizza = pizza

    def atualizarStatus(self, valor) -> None:
        print("\nSubject: Atualizando status")
        self._state = valor

        print(f"O pedido {self._id} (pizza de {self._pizza}) está sendo {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class Cliente(Observer):
    _nome: str = None
    _telefone: str = None
    _email: str = None
    _rua: str = None
    _numero: str = None

    def adicionarDados(self, nome, telefone, rua, email, numero):
        self._nome = nome
        self._telefone = telefone
        self._rua = rua
        self._email = email
        self._numero = numero

    def update(self, subject: Subject) -> None:
        print(f"Status do pedido {subject._id} atualizado para '{subject._state}'")
        subject._historico_state.append(subject._state)