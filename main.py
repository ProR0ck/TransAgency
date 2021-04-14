import random

class TransAgency:
    """Класс транс агенства"""
    def __init__(self, company_name):
        """Задает имя компании"""
        self.company_name = company_name

    def set_company_name(self,company_name):
        """Задает имя компании"""
        self.company_name = company_name

    def get_company_name(self):
        """Возвращает имя компании"""
        return self.company_name

class Cargo:
    """Класс груз"""
    def __init__(self, weight):
        """Задает массу груза"""
        self.cargo_weight = weight

    def set_weight(self, new_weight):
        """Задает массу груза"""
        self.cargo_weight = new_weight

    def get_weight(self):
        """Возвращает массу груза"""
        return self.cargo_weight

class Customer(Cargo):
    """Класс заказчик"""
    def __init__(self, name: str, customers_desired_delivery_price, customers_desired_speed):
        """задает имя заказчика, желаемую цену доставки и скорость доставки"""
        self.name = name
        self.customers_desired_delivery_price = customers_desired_delivery_price
        self.customers_desired_speed = customers_desired_speed

    def get_customer_name(self):
        """Возвращает имя заказчика"""
        return self.name

    def set_customer_name(self, name):
        """Задает имя клиента"""
        self.name = name

    def set_customers_desired_delivery_price(self, customers_desired_delivery_price):
        """Задает желаемую цену доставки груза"""
        self.customers_desired_delivery_price = customers_desired_delivery_price

    def set_customers_desired_speed(self, customers_desired_speed):
        """Задает желаемую скорость доставки"""
        self.customers_desired_speed = customers_desired_speed

class Branch(TransAgency, Customer):
    """Класс филиала"""
    def __init__(self, branch_name):
        """Задает имя филиала"""
        self.branch_name = branch_name

    def set_branch_name(self,branch_name):
        """Задает имя филиала"""
        self.branch_name = branch_name

    def get_branchy_name(self):
        """Возвращает имя филиала"""
        return self.branch_name
    def delivery(self):
        pass

class Weather():
    """Класс погода"""
    def __init__(self, weather_type: bool):
        """Инизиализирует тип погоды"""
        self.weather_type = weather_type

    def set_weather(self, weather_type: bool):
        """Ихменяет тип погоды Плохая - False, хорошая - True"""
        self.weather_type = weather_type

    def get_weather(self):
        """озвращает тип погоды"""
        return self.weather_type

    def set_random_weater(self):
        """задает случайную погоду"""
        self.weather_type = bool(random.randint(0,1))

class City(Weather):
    """Класс город"""

    def __init__(self, city: str):
        """Задает название города"""
        self.city = city

    def set_city(self, city: str):
        """Изменяет название города"""
        self.city = city

    def get_city(self):
        """Возвращает название города"""
        return self.city

    def is_big_city(self):
        """Проверяет большой ли город"""
        if self.city in ["Moscow", "Berlin", "Tokyo", "Pekin"]:
            return True
        else:
            return False

    def is_middle_city(self):
        """роверяет средний ли город"""
        if self.city in ["Tver", "Hamburg", "Rjev"]:
            return True
        else:
            return False

class Transport:
    """Класс транспорт"""

    def __init__(self, cost_weight_per_way = None, delivery_speed = None):
        """Инициализация стоимости доставки и скорости доставки"""
        if cost_weight_per_way is not  None and delivery_speed is not None:
            self.cost_weight_per_way = cost_weight_per_way
            """стоимость единицы веса на единицу пути"""
            self.delivery_speed = delivery_speed
            """скорость доставки"""
        else:
            self.cost_weight_per_way = 0
            self.delivery_speed = 0

    def set_cost(self, cost_weight_per_way):
        """Задает стоимость единицы веса на единицу пут"""
        self.cost_weight_per_way = cost_weight_per_way

    def set_speed(self, delivery_speed):
        """Задает скорость доставки"""
        self.delivery_speed = delivery_speed

    def get_cost(self):
        """Возвращает стоимость единицы веса на единицу пути"""
        return self.cost_weight_per_way

    def get_speed(self):
        """Возвращает скорость доставки"""
        return self.delivery_speed

class Train(Transport):
    """Класс железнодорожный транспорт"""

class Car(Transport):
    """Класс автомобильный транспорт"""

class Plane(Transport, Weather):
    """Класс авиатранспорт"""

if __name__ == "__main__":
    print("hello")

