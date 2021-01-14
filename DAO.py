import DBHandler as handler
import DTO


class DAO:
    def __init__(self, dto_type, conn, lastId):
        self._conn = conn
        self._dto_type = dto_type

        # dto_type is a class, its __name__ field contains a string representing the name of the class.
        self._table_name = dto_type.__name__.lower() + 's'
        self.lastId = lastId

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        if isinstance(dto_instance,DTO.Vaccine):
            ins_dict['id'] = self.lastId

        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))

        self.lastId += 1

        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        # stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        params=list(params)
        self._conn.execute(stmt, params)

    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return handler.orm(self,c, self._dto_type)

    def find_by_order(self, colName):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {} ORDER BY {}'.format(self._table_name, colName))
        return handler.orm(self,c, self._dto_type)

    def column_sum(self, colName):
        c = self._conn.cursor()
        c.execute('SELECT SUM({}) FROM {}'.format(colName,self._table_name))
        return c.fetchone()[0]

    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'SELECT * FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))

        c = self._conn.cursor()
        c.execute(stmt, list(params))
        return handler.orm(self,c, self._dto_type)

    def delete(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()

        stmt = 'DELETE FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))

        c = self._conn.cursor()
        c.execute(stmt, list(params))

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()

        cond_column_names = cond.keys()
        cond_params = cond.values()

        params = list(set_params) + list(cond_params)

        stmt = 'UPDATE {} SET {} WHERE {}'.format(self._table_name,
                                                      ', '.join([set + '=?' for set in set_column_names]),
                                                      ' AND '.join([cond + '=?' for cond in cond_column_names]))

        self._conn.execute(stmt, params)



    # def getLastID(self):
    #     c = self._conn.cursor()
    #     c.execute('SELECT MAX(id) FROM {}'.format(self._table_name))
    #     return [*c.fetchone()]