import sys
from datetime import datetime
from time import strptime

from _Repository import repo
import sqlite3
import DBHandler as handler


import DTO



dbcon = repo._conn
def main(args):
    repo.create_tables()

    raws = read_file(args[1])
    str = '01'
    print(int(str))

    numOfVaccines = int(raws[0][0])
    numOfSuppliers = int(raws[0][1])
    numOfClinics = int(raws[0][2])
    numOfLogistics = int(raws[0][3])

    line = 1


    for i in range (numOfVaccines):
        repo.vaccines.insert( DTO.Vaccine(raws[line][0], str_to_date(raws[line][1]), raws[line][2], raws[line][3].replace('\n','')))
        line += 1


    for i in range (numOfSuppliers):
        repo.suppliers.insert( DTO.Supplier(raws[line][0], raws[line][1], raws[line][2].replace('\n','')))
        line += 1


    for i in range(numOfClinics):
        repo.clinics.insert( DTO.Clinic(raws[line][0], raws[line][1], raws[line][2], raws[line][3].replace('\n', '')))
        line += 1

    for i in range(numOfLogistics):
        repo.logistics.insert(DTO.Logistic(raws[line][0], raws[line][1], raws[line][2], raws[line][3].replace('\n', '')))
        line += 1


    ordersRaws = read_file(args[2])
    print(ordersRaws)

    suppliers = {supplier.name :[supplier.id, supplier.logistic] for supplier in repo.suppliers.find_all()}
    print(suppliers)

    # summary = [[repo.vaccines.column_sum('quantity'), repo.clinics.column_sum('demand'), repo.logistics.column_sum('count_received'), repo.logistics.column_sum('count_sent')]]
    summary = []
    for i in range (len(ordersRaws)):
        if (len(ordersRaws[i]) == 3):
            recieveShipment(ordersRaws[i], suppliers)
        else:
            sendShipment(ordersRaws[i])
        summary.append([repo.vaccines.column_sum('quantity'), repo.clinics.column_sum('demand'), repo.logistics.column_sum('count_received'), repo.logistics.column_sum('count_sent')])

    writeOutput(args[3], summary)


def writeOutput(path,summary):
    f = open(path, "a")
    for i in range(len(summary)):
        f.write(str(summary[i][0]) + ',' + str(summary[i][1])+ ',' + str(summary[i][2]) + ',' + str(summary[i][3])+ '\n')
    f.close()


def sendShipment(shipment):
    #update demand in clinic
    clinic = repo.clinics.find(location=shipment[0])[0]
    amount = int(shipment[1].replace('\n',''))
    demand = clinic.demand
    newDemand = max(demand-amount,0)
    repo.clinics.update({'demand': newDemand}, {'id': clinic.id})

    #update count_sent in logistic
    logi = repo.logistics.find(id=clinic.logistic)[0]
    newCount = logi.count_sent + amount
    repo.logistics.update({'count_sent': newCount}, {'id': logi.id})

    #update vaccines's inventory
    vaccines = repo.vaccines.find_by_order('date')
    while (amount>0):
        oldestVaccine = vaccines[0]
        dif = oldestVaccine.quantity-amount
        if (dif>0):
            repo.vaccines.update({'quantity': dif},{'id': oldestVaccine.id})
            amount = amount - oldestVaccine.quantity
        else:
            repo.vaccines.delete(id=oldestVaccine.id)
            vaccines.pop(0)
            amount = amount - oldestVaccine.quantity


def recieveShipment(shipment, suppliers):
    supplierID = suppliers[shipment[0]][0]
    logID = suppliers[shipment[0]][1]
    repo.vaccines.insert(DTO.Vaccine(0, str_to_date(shipment[2].replace('\n', '')), supplierID, shipment[1]))
    logi = repo.logistics.find(id=logID)[0]
    newCount = logi.count_received + int(shipment[1])
    repo.logistics.update({'count_received': newCount}, {'id': logID})

def read_file(path):
    inputfilename = path
    with open(inputfilename) as inputfile:
        return [line.split(',') for line in inputfile]


def str_to_date(str):
    date = str.split("-")
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    return datetime.date(date)




if __name__ == '__main__':
    main(sys.argv)