"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

class Store:
    name: str
    count: int
    price: int
    total: int
    department: str
    def __init__(self, name, count, price):
        self.tech_dict = {
            "Наименование": name,
            "Количество": count,
            "Цена за ед.": price,
        }

    def add_tech(self, name: str, department: str, count, dcount: int):
        self.dep_dict = {
            "Отдел": department,
            "Наименование оргтехники": name,
            "Передано в отдел": dcount
        }
        count = count - dcount
        print(self.dep_dict)
        print(f"Остаток {name} на складе: {count}")


class Orgtechnica:
    paper_format: str

class Printer(Orgtechnica):
    print_speed: int

    def __init__(self, name, count, price, print_speed):
        self.tech_dict = {
            "Наименование": name,
            "Количество": count,
            "Цена за ед.": price,
            "Скорость печати": print_speed
        }
        print(self.tech_dict)

class Scaner(Orgtechnica):
    scan_cpeed: int

    def __init__(self, name, count, price, scan_speed):
        self.tech_dict = {
            "Наименование": name,
            "Количество": count,
            "Цена за ед.": price,
            "Скорость сканирования": scan_speed
        }
        print(self.tech_dict)

class Xerox(Orgtechnica):
    copy_speed: int

    def __init__(self, name, count, price, copy_speed):
        self.tech_dict = {
            "Наименование": name,
            "Количество": count,
            "Цена за ед.": price,
            "Скорость копирования": copy_speed
        }
        print(self.tech_dict)

store = Store("Canon", 20, 2300)

canon = Printer("Canon", 20, 2300, 100)
hp = Scaner("HP", 10, 1500, 20)
xerox = Xerox("Xerox", 15, 3000, 50)

store.add_tech("Canon", "Отдел снабжения", 20, 5)
