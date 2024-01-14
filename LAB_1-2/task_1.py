# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_running = False

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.start_engine()
        """
        self.engine_running = True
        print("Engine started")

    def stop_engine(self) -> None:
        """
        Остановка двигателя автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.stop_engine()
        """
        self.engine_running = False
        print("Engine stopped")

    def drive(self, distance: float) -> None:
        """
        Проехать определенное расстояние на автомобиле

        :param distance: Расстояние, которое нужно проехать

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.start_engine()
        >>> car.drive(100)
        """
        if not self.engine_running:
            raise ValueError("Невозможно управлять автомобилем не запустив двигатель")
        print(f"Двидение на {distance} km")


class Calculator:
    def __init__(self):
        """
        Создание объекта "Калькулятор"

        Примеры:
        >>> calc = Calculator()
        """
        pass

    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел

        :param a: Первое число
        :param b: Второе число
        :return: Сумма двух чисел

        Примеры:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание двух чисел

        :param a: Уменьшаемое число
        :param b: Вычитаемое число
        :return: Разность двух чисел

        Примеры:
        >>> calc = Calculator()
        >>> calc.subtract(5, 3)
        2
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Умножение двух чисел

        :param a: Первый множитель
        :param b: Второй множитель
        :return: Произведение двух чисел

        Примеры:
        >>> calc = Calculator()
        >>> calc.multiply(2, 3)
        6
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Деление двух чисел

        :param a: Делимое число
        :param b: Делитель
        :return: Частное двух чисел

        :raise ZeroDivisionError: Если делитель равен нулю, вызывается ошибка

        Примеры:
        >>> calc = Calculator()
        >>> calc.divide(6, 3)
        2.0
        """
        if b == 0:
            raise ZeroDivisionError("Нельзя делить на ноль")
        return a / b


class Student:
    def __init__(self, name: str, age: int, major: str):
        """
        Создание объекта "Студент"

        :param name: Имя студента
        :param age: Возраст студента
        :param major: Специальность студента

        Примеры:
        >>> student = Student("Иван Иваноы", 20, "ПГС")
        """
        self.name = name
        self.age = age
        self.major = major

    def study(self) -> None:
        """
        Студент занимается учебой

        Примеры:
        >>> student = Student("Иван Иваноы", 20, "ПГС")
        >>> student.study()
        """
        print(f"{self.name} is studying")


if __name__ == "__main__":
    doctest.testmod()
