from DTO import Clinic


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    # def insert(self, clinic):
    #     self._conn.execute("""
    #            INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
    #        """, [clinic.id, clinic.location,clinic.demand, clinic.logistic])
    #
    # def find(self, clinic_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, location, demand, logistic FROM clinics WHERE id = ?
    #     """, [clinic_id])
    #     return Clinic(*c.fetchone())
    #
    # def remove(self, clinic_id):
    #     self._conn.execute("""
    #         DELETE FROM clinica WHERE id = ?
    #     """, [clinic_id])