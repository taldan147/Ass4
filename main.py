import sys
from datetime import datetime
from time import strptime

from _Repository import repo
import sqlite3
import DBHandler as handler


import DTO
from DAO import DAO

dbcon = repo._conn
daoArray = [DAO(DTO.Vaccine, dbcon), DAO(DTO.Supplier, dbcon), DAO(DTO.Clinic, dbcon), DAO(DTO.Logistic, dbcon)]
def main(args):
    repo.create_tables()

    raws = read_file(args[1])
    print(raws)

    numOfVaccines = int(raws[0][0])
    numOfSuppliers = int(raws[0][1])
    numOfClinics = int(raws[0][2])
    numOfLogistics = int(raws[0][3])

    line = 1

    VacDao = daoArray[0]
    for i in range (numOfVaccines):
        DAO.insert(VacDao, DTO.Vaccine(raws[line][0], raws[line][1], raws[line][2], raws[line][3].replace('\n','')))
        line += 1

    SuppDao = daoArray[1]
    for i in range (numOfSuppliers):
        DAO.insert(SuppDao, DTO.Supplier(raws[line][0], raws[line][1], raws[line][2].replace('\n','')))
        line += 1

    ClinicDao = daoArray[2]
    for i in range(numOfClinics):
        DAO.insert(ClinicDao, DTO.Clinic(raws[line][0], raws[line][1], raws[line][2], raws[line][3].replace('\n', '')))
        line += 1

    LogisticDao = daoArray[3]
    for i in range(numOfLogistics):
        DAO.insert(LogisticDao,DTO.Logistic(raws[line][0], raws[line][1], raws[line][2], raws[line][3].replace('\n', '')))
        line += 1


    ordersRaws = read_file(args[2])

    # for i in range (len(ordersRaws)-1):
    #     if (len(ordersRaws[i]) == 3):



def recieveShipment(shipment):
    supplierID = DAO.find(daoArray[1], shipment[0])
    DAO.insert(daoArray[0],DTO.Vaccine())



def read_file(path):
    inputfilename = path
    with open(inputfilename) as inputfile:
        return [line.split(',') for line in inputfile]




if __name__ == '__main__':
    main(sys.argv)