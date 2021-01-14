import atexit
import sqlite3

import DTO
from DAO import DAO


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = DAO(DTO.Vaccine,self._conn, 1)
        self.suppliers = DAO(DTO.Supplier, self._conn,1)
        self.clinics = DAO(DTO.Clinic,self._conn,1)
        self.logistics = DAO(DTO.Logistic,self._conn,1)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE vaccines (
            id               INT         PRIMARY KEY,
            date             DATE        NOT NULL,
            supplier         INT         REFERENCES supplier(id), 
            quantity         INT         NOT NULL 
        );

        CREATE TABLE suppliers (
            id               INT         PRIMARY KEY,
            name             STRING      NOT NULL,
            logistic         INT         REFERENCES logistics(id)
            
            
        );

        CREATE TABLE clinics (
            id               INT         PRIMARY KEY,
            location         STRING      NOT NULL,
            demand           INT         NOT NULL,
            logistic         INT         REFERENCES logistics(id)

        );
        CREATE TABLE logistics (
            id               INT         PRIMARY KEY,
            name             STRING      NOT NULL,
            count_sent       INT         NOT NULL,
            count_received    INT         NOT NULL
        );
    """)

repo = _Repository()
atexit.register(repo._close)









