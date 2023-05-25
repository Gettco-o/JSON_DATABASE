from collections import OrderedDict
import json


class Update:
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        with open(f'{db_name}.json','r') as file:
            self._db = json.load(file)

    def update_table(self, table_name, new_name):
        new_db = OrderedDict()
        for k, v in self._db.items():
            if k == table_name:
                new_db[new_name] = v
            else:
                new_db[k] = v

        self._db = dict(new_db)

        with open(f'{self.db_name}.json', 'w') as file:
                json.dump(self._db, file, indent=4)

        return self._db
    
    def add_columns(self, table_name, *args):
        for entry in self._db[table_name]:
            for key in args:
                if key not in entry:
                    entry[key] = None
        with open(f'{self.db_name}.json', 'w') as file:
            json.dump(self._db, file, indent=4)
        return self._db
    
    def update_values(self, table_name, key, key_value, **updates):
        for entry in self._db[table_name]:
            if entry.get(key) == key_value:
                entry.update(updates)
        with open(f'{self.db_name}.json', 'w') as file:
            json.dump(self._db, file, indent=4)
        return self._db