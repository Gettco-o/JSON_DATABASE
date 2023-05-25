from typing import Any
from .create import Create
from .read import Read
from .update import Update
from .delete import Delete

class JsonDb(Create, Read, Update, Delete):
    session_count = 0
    table_id = 0

    def __init__(self, db_name) -> None:
        super().__init__(db_name)
        JsonDb.session_count += 1
        self.db_session = JsonDb.session_count

    
    def getSession(self) -> int:
        return self.db_session