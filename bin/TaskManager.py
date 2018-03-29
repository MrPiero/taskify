import sqlite3


class TaskManager:
    def __init__(self, database=None):
        if database is not None:
            self.connection = sqlite3.connect(database)
        else:
            self.connection = None
