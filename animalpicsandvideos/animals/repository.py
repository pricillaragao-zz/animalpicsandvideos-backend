from typing import List
from .animal import Animal


class AnimalsRepository:
    def __init__(self, conn):
        self.table_name = "animals"
        self.conn = conn

    def find_animal(self, id_: str) -> Animal:
        cur = self.conn.cursor()
        cur.execute(f"SELECT id, species FROM {self.table_name} WHERE id = %s;", (id_,))
        result = cur.fetchone()
        print(result)
        return Animal(result[0], result[1])

    def list_animals(self) -> List[Animal]:
        cur = self.conn.cursor()
        cur.execute(f"SELECT id, species FROM {self.table_name};")
        results = cur.fetchall()
        return [Animal(result[0], result[1]) for result in results]
