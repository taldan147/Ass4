import atexit
import sqlite3

from _Clinics import _Clinics
from _Logistics import _Logistics
from _Suppliers import _Suppliers
from _Vaccines import _Vaccines


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = _Vaccines(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.clinics = _Clinics(self._conn)
        self.logistics = _Logistics(self._conn)

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
            count_recieve    INT         NOT NULL
        );
    """)

repo = _Repository()
atexit.register(repo._close)









