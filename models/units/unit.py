from abc import abstractmethod, ABC


class Unit(ABC):

    UNIT = {}

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def is_attack(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def damage_rank(self):
        pass

    @abstractmethod
    def take_damage(self):
        pass

    @abstractmethod
    def is_active(self):
        pass

    @classmethod
    def register(cls, name):
        def dec(unit_cls):
            cls.UNIT[name] = unit_cls
            return unit_cls
        return dec

    @classmethod
    def new(cls, name, **kwargs):
        return cls.UNIT[name](**kwargs)
