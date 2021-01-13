import sys
from datetime import datetime
from time import strptime

from _Repository import repo
import sqlite3
import DBHandler as handler


import DTO
from DAO import DAO

def main(args):
    # repo.create_tables()
    dbcon = sqlite3.connect('database.db')
    raws = read_file(args[1])
    print(raws)
    numOfVaccines = int(raws[0][0])
    numOfSppliers = int(raws[0][1])
    numOfClinics = int(raws[0][2])
    numOfLogistics = int(raws[0][3])

    counter = 0
    dao = DAO(DTO.Vaccine, dbcon)
    str = raws[1][1]
    print(datetime.strptime('2021-01-11', '%Y-%m-%d'))



    # dao.insert(DTO.Vaccine(raws[1][0],raws[1][1],raws[1][2],raws[1][3]))
    # print(dao.find(1))
    print(int(raws[1][0]),' ', raws[1][1],' ', int(raws[1][2]),' ', int(raws[1][3]))
    print(type(raws[1][1]))



def read_file(path):
    inputfilename = path
    with open(inputfilename) as inputfile:
        return [line.split(',') for line in inputfile]




if __name__ == '__main__':
    main(sys.argv)