# Observer Pattern Implementation
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class EmailNotifier(Observer):
    def update(self, subject):
        # Email notification logic
        pass

class SMSNotifier(Observer):
    def update(self, subject):
        # SMS notification logic
        pass

class NotificationSubject:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
