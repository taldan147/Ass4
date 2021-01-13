
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
        self.id = int(id)
        self.name = name
        self.logistic = int(logistic)

class Clinic:
    def __init__(self, id, location, demand, logistic):
        self.id = int(id)
        self.location = location
        self.demand = int(demand)
        self.logistic = int(logistic)


class Logistic:
    def __init__(self, id, name, count_sent, count_recieve):
        self.id = int(id)
        self.name = name
        self.count_sent = int(count_sent)
        self.count_recieve = int(count_recieve)