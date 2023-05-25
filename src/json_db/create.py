
import json
from typing import Any

class Create:
    table_id = 0

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        dbname = self.db_name
        self._db = {}
        with open(f'{dbname}.json', 'w') as file:
            json.dump(self._db, file, indent=4)
    

    def create_tables(self, *args) -> None:
        self.table_names = args
        self.table_data = {}
        for table in self.table_names:
            dbname = self.db_name
            self._db.update({f"{table}": []})
            with open(f'{dbname}.json', 'w') as file:
                json.dump(self._db, file, indent=4)
            self.table_id += 1
            self.table_data.update({f"{table}": self.table_id})
            
    
    def get_table_id(self, table_name: str) -> dict:        
        return self.table_data[table_name]

    
    def insert_columns(self, table_name: str, *args):
        self.table_columns = args
        for column in self.table_columns:
            dbname = self.db_name
            self._db_col = {}
            for column in self.table_columns:
                dbname = self.db_name
                self._db_col.update({f"{column}": None})
            
            self.col_list = []
            self.col_list.append(self._db_col)
            self._db[table_name] = self.col_list
            with open(f'{dbname}.json', 'w') as file:
                json.dump(self._db, file, indent=4)


    def insert_values(self, table_name: str, **kwds):
        dbname = self.db_name
        self.cols = kwds.keys()
        self.vals = kwds.values()
        self._db_col = {}
        
        # Get the maximum existing id for the table
        max_id = max([item.get('id', 0) for item in self._db[table_name]])
        if max_id == None:
            max_id = 0
        
        # Generate a new id by incrementing the maximum id
        new_id = max_id + 1
        
        # Assign the generated id to the values
        self._db_col["id"] = new_id
        
        for i in range(len(kwds)):
            self._db_col.update({f"{list(self.cols)[i]}": list(self.vals)[i]})

        #if self._db[table_name][0]["id"] is None:
        if next(iter(self._db[table_name][0].values())) is None:
            self.col_list = []
            self.col_list.append(self._db_col)
            self._db[table_name] = self.col_list
        else:
            # Check if the values already exist for the specific table
            if self._db_col not in self._db[table_name]:
                self._db[table_name].append(self._db_col)

        with open(f'{dbname}.json', 'w') as file:
            json.dump(self._db, file, indent=4)