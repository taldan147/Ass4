
import sqlite3

from DTO import Vaccine


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    # def insert(self, vaccine):
    #     self._conn.execute("""
    #            INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
    #        """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])
    #
    # def find(self, vaccine_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, data, supplier, quantity FROM vaccines WHERE id = ?
    #     """, [vaccine_id])
    #     return Vaccine(*c.fetchone())
    #
    # def remove(self, vaccine_id):
    #     self._conn.execute("""
    #         DELETE FROM vaccines WHERE id = ?
    #     """, [vaccine_id])