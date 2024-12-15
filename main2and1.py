# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Furniture:
    """
    Абстрактный класс, представляющий предмет мебели.

    Атрибуты:
        height (int): Высота предмета мебели в сантиметрах.
        width (int): Ширина предмета мебели в сантиметрах.
        depth (int): Глубина предмета мебели в сантиметрах.
    """

    def __init__(self, height: int, width: int, depth: int) -> None:
        """
        Конструктор класса Furniture.

        Args:
            height (int): Высота предмета мебели в сантиметрах.
            width (int): Ширина предмета мебели в сантиметрах.
            depth (int): Глубина предмета мебели в сантиметрах.

        Raises:
            ValueError: Если высота, ширина или глубина отрицательны.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        if depth <= 0:
            raise ValueError("Глубина должна быть положительной")

        self.height = height
        self.width = width
        self.depth = depth

    def move(self, distance: int) -> None:
        """
        Перемещает предмет мебели на заданное расстояние.

        Args:
            distance (int): Расстояние, на которое нужно переместить предмет мебели в сантиметрах.

        Raises:
            ValueError: Если расстояние отрицательное.

        Examples:
            >>> furniture = Furniture(height=100, width=50, depth=60)
            >>> furniture.move(distance=10)
        """
        if distance < 0:
            raise ValueError("Расстояние должно быть неотрицательным")
        ...

    def resize(self, new_height: int, new_width: int, new_depth: int) -> None:
        """
        Изменяет размеры предмета мебели.

        Args:
           new_height (int): Новая высота предмета мебели в сантиметрах.
           new_width (int): Новая ширина предмета мебели в сантиметрах.
           new_depth (int): Новая глубина предмета мебели в сантиметрах.

        Raises:
             ValueError: Если новая высота, ширина или глубина отрицательны.

        Examples:
            >>> furniture = Furniture(height=100, width=50, depth=60)
            >>> furniture.resize(new_height=120, new_width=70, new_depth=80)
        """
        if new_height <= 0:
            raise ValueError("Новая высота должна быть положительной")
        if new_width <= 0:
            raise ValueError("Новая ширина должна быть положительной")
        if new_depth <= 0:
            raise ValueError("Новая глубина должна быть положительной")
        ...

    def get_volume(self) -> int:
        """
        Вычисляет и возвращает объем предмета мебели в кубических сантиметрах.

        Returns:
            int: Объем предмета мебели в кубических сантиметрах.

        Examples:
            >>> furniture = Furniture(height=100, width=50, depth=60)
            >>> furniture.get_volume()
            300000
        """
        return self.height * self.width * self.depth


class SocialNetwork:
    """
    Абстрактный класс, представляющий социальную сеть.

    Атрибуты:
        users (int): Количество пользователей в социальной сети.
        posts (int): Количество постов в социальной сети.
    """

    def __init__(self, users: int, posts: int) -> None:
        """
        Конструктор класса SocialNetwork.

        Args:
            users (int): Количество пользователей в социальной сети.
            posts (int): Количество постов в социальной сети.

        Raises:
            ValueError: Если количество пользователей или постов отрицательно.
        """
        if users < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным")
        if posts < 0:
            raise ValueError("Количество постов должно быть неотрицательным")

        self.users = users
        self.posts = posts

    def add_user(self, count: int = 1) -> None:
        """
        Добавляет пользователей в социальную сеть.

        Args:
            count (int): Количество новых пользователей, которых нужно добавить. По умолчанию 1.

        Raises:
            ValueError: Если количество добавляемых пользователей отрицательное.

        Examples:
            >>> network = SocialNetwork(users=100, posts=500)
            >>> network.add_user(count=5)
        """
        if count < 0:
            raise ValueError("Количество добавляемых пользователей должно быть неотрицательным")
        ...

    def add_post(self, count: int = 1) -> None:
        """
        Добавляет посты в социальную сеть.

        Args:
            count (int): Количество новых постов, которых нужно добавить. По умолчанию 1.

        Raises:
            ValueError: Если количество добавляемых постов отрицательное.

        Examples:
            >>> network = SocialNetwork(users=100, posts=500)
            >>> network.add_post(count=10)
        """
        if count < 0:
            raise ValueError("Количество добавляемых постов должно быть неотрицательным")
        ...

    def get_average_posts_per_user(self) -> float:
        """
        Возвращает среднее количество постов на одного пользователя.

        Returns:
            float: Среднее количество постов на одного пользователя.

        Examples:
            >>> network = SocialNetwork(users=100, posts=500)
            >>> network.get_average_posts_per_user()
            5.0
        """
        if self.users == 0:
            return 0
        return self.posts / self.users


class Robot:
    """
    Абстрактный класс, представляющий робота.

    Атрибуты:
        power (int): Мощность робота в условных единицах.
        speed (int): Скорость робота в метрах в секунду.
    """

    def __init__(self, power: int, speed: int) -> None:
        """
        Конструктор класса Robot.

        Args:
            power (int): Мощность робота в условных единицах.
            speed (int): Скорость робота в метрах в секунду.

        Raises:
            ValueError: Если мощность или скорость отрицательные.
        """
        if power < 0:
            raise ValueError("Мощность должна быть неотрицательной")
        if speed < 0:
            raise ValueError("Скорость должна быть неотрицательной")

        self.power = power
        self.speed = speed

    def move(self, time: int) -> None:
        """
        Перемещает робота в течении заданного времени.

        Args:
            time (int): Время перемещения робота в секундах.

         Raises:
             ValueError: Если время отрицательное.

        Examples:
            >>> robot = Robot(power=100, speed=10)
            >>> robot.move(time=10)
        """
        if time < 0:
            raise ValueError("Время должно быть неотрицательным")
        ...

    def recharge(self, energy: int) -> None:
        """
        Заряжает робота на заданное количество энергии.

        Args:
            energy (int): Количество энергии для зарядки в условных единицах.

         Raises:
             ValueError: Если количество энергии для зарядки отрицательное.

        Examples:
            >>> robot = Robot(power=100, speed=10)
            >>> robot.recharge(energy=50)
        """
        if energy < 0:
            raise ValueError("Количество энергии должно быть неотрицательным")
        ...

    def get_distance(self, time: int) -> int:
        """
        Возвращает расстояние, которое робот проедет за заданное время.

        Args:
            time (int): Время в секундах.

        Returns:
            int: Расстояние в метрах.

        Examples:
             >>> robot = Robot(power=100, speed=10)
             >>> robot.get_distance(time=5)
             50
        """
        if time < 0:
            raise ValueError("Время должно быть неотрицательным")
        return self.speed * time


if __name__ == "__main__":
    doctest.testmod()


