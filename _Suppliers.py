from DTO import Supplier


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    # def insert(self, supplier):
    #     self._conn.execute("""
    #            INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
    #        """, [supplier.id, supplier.name, supplier.logistic])
    #
    # def find(self, supplier_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, name, logistic FROM suppliers WHERE id = ?
    #     """, [supplier_id])
    #     return Supplier(*c.fetchone())
    #
    # def remove(self, supplier_id):
    #     self._conn.execute("""
    #         DELETE FROM suppliers WHERE id = ?
    #     """, [supplier_id])

