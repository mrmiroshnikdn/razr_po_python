from typing import Any


class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, habitat: str):
        """
        Инициализация базового класса Animal.

        :param name: Название животного
        :param habitat: Среда обитания животного
        """
        self._name = name  # Название животного (инкапсулировано для ограничения прямого доступа)
        self.habitat = habitat

    def __str__(self) -> str:
        return f"Животное: {self._name}, Среда обитания: {self.habitat}"

    def __repr__(self) -> str:
        return f"Animal(name={self._name}, habitat={self.habitat})"

    def make_sound(self) -> str:
        """
        Метод, который должен быть реализован в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе")


class Mammal(Animal):
    """
    Дочерний класс, представляющий млекопитающих.
    """

    def __init__(self, name: str, habitat: str, fur_color: str):
        """
        Инициализация класса Mammal.

        :param name: Название животного
        :param habitat: Среда обитания
        :param fur_color: Цвет шерсти
        """
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def __str__(self) -> str:
        return f"Млекопитающее: {self._name}, Среда обитания: {self.habitat}, Цвет шерсти: {self.fur_color}"

    def make_sound(self) -> str:
        """
        Перегруженный метод make_sound, характерный для млекопитающих.
        Возвращает типичный звук млекопитающего.
        """
        return "Рычание или мурчание"


class Bird(Animal):
    """
    Дочерний класс, представляющий птиц.
    """

    def __init__(self, name: str, habitat: str, wing_span: float):
        """
        Инициализация класса Bird.

        :param name: Название птицы
        :param habitat: Среда обитания
        :param wing_span: Размах крыльев
        """
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def __str__(self) -> str:
        return f"Птица: {self._name}, Среда обитания: {self.habitat}, Размах крыльев: {self.wing_span} м"

    def make_sound(self) -> str:
        """
        Перегруженный метод make_sound для птиц.
        Возвращает звук, характерный для птиц.
        """
        return "Чириканье или крик"


if __name__ == "__main__":
    # Создание экземпляров классов
    mammal = Mammal("Лев", "Саванна", "Золотистый")
    bird = Bird("Орел", "Горы", 2.3)

    print(mammal)
    print(mammal.make_sound())

    print(bird)
    print(bird.make_sound())
