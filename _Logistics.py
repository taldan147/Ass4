from DTO import Logistic


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    # def insert(self, logistic):
    #     self._conn.execute("""
    #            INSERT INTO logistics (id, name, count_sent, count_recieve) VALUES (?, ?, ?, ?)
    #        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_recieve])
    #
    # def find(self, logistic_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, name, count_sent, count_recieve FROM logistics WHERE id = ?
    #     """, [logistic_id])
    #     return Logistic(*c.fetchone())
    #
    # def remove(self, logistic_id):
    #     self._conn.execute("""
    #         DELETE FROM logistics WHERE id = ?
    #     """, [logistic_id])