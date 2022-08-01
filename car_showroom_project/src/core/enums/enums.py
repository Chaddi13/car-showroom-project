import enum


class BaseEnum(enum.Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class CarBodyType(BaseEnum):
    SEDAN = "Седан"
    COUPE = "Купе"
    SPORT = "Спорткар"
    WAGON = "Универсал"
    HATCHBACK = "Хэтчбэк"
    CONVERTIBLE = "Кабриолет"
    MINIVAN = "Минивэн"


class CarColor(BaseEnum):
    RED = "Красный"
    GREEN = "Зеленый"
    ORANGE = "Оранжевый"
    LIGHT_GREY = "Светло-серый"
    DARK_GREY = "Темно-серый"
    BLACK = "Черный"
    WHITE = "Белый"
    BLUE = "Синий"


class CustomerSex(BaseEnum):
    MALE = "Мужчина"
    FEMALE = "Женщина"
