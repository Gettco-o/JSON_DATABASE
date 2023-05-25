import json

class Delete:
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        with open(f'{db_name}.json','r') as file:
            self._db = json.load(file)

    def drop_table(self, table_name):
        del self._db[table_name]
        with open(f'{self.db_name}.json', 'w') as file:
            json.dump(self._db, file, indent=4)

    def drop_column(self, table_name, col):
        if col is not "id":
            for data in self._db[table_name]:
                del data[col]
            with open(f'{self.db_name}.json', 'w') as file:
                json.dump(self._db, file, indent=4)