import importlib
from abc import ABC, abstractmethod
from datetime import date

from django.conf import settings


class BaseCrptoEngine(ABC):
    @abstractmethod
    def get_current_price(self):
        raise NotImplementedError('Function need to implemented by derived class')

    @abstractmethod
    def get_historical_price(self, start_date: date, end_date: date):
        raise NotImplementedError('Function need to implemented by derived class')


def get_register_crpto_engine() -> BaseCrptoEngine:
    crpto_engine = settings.SERVER_CONFIG.get('crpto_engine')
    package = crpto_engine.rsplit('.', 1)
    if len(package) < 2:
        raise ValueError('Module registry in settings.CRPTO_ENGINE not found')
    module_name = package[0]
    class_name = package[1]
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    if not issubclass(class_, BaseCrptoEngine):
        raise ValueError(f'Crypto Engine {crpto_engine} should be sub class of BaseCrptoEngine')
    return class_()
