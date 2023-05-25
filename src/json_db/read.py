import json

class Read:

    def __init__(self, db_name) -> None:
        self.db_name = db_name
        with open(f'{db_name}.json','r') as file:
            self._db = json.load(file)

    def get_all(self):
        return self._db
    
    def get_tables(self):
        return list(self._db.keys())

    def get_table_data(self, table_name):
        return self._db[table_name]


    def filter(self, table_name, **kwds):
        db = self._db
        data = []
        for _d in db[table_name]:
            if all(_d.get(key) == value for key, value in kwds.items()):
                data.append(_d)
        return data