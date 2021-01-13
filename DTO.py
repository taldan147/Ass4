
from datetime import datetime

class Vaccine:
    def __init__(self,id,date,supplier,quantity):
        self.id = int(id)
        self.date = datetime.strptime('2021-01-11', '%Y-%m-%d')
        self.date = datetime.date(self.date)
        self.supplier = int(supplier)
        self.quantity = int(quantity)

class Supplier:
    def __init__(self,id,name,logistic):
        self.id = id
        self.name = name
        self.logistic = logistic

class Clinic:
    def __init__(self, id, location, demand, logistic):
        self.id = id
        self.location = location
        self.demand = demand
        self.logistic = logistic


class Logistic:
    def __init__(self, id, name, count_sent, count_recieve):
        self.id = id
        self.name = name
        self.count_sent = count_sent
        self.count_recieve = count_recieve