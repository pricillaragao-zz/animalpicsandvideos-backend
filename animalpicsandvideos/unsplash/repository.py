class UnsplashRepository:
    def __init__(self, conn):
        self.table_name = "unsplash"
        self.conn = conn

    def find_by_animal_id(self, animal_id: str) -> str:
        cur = self.conn.cursor()
        cur.execute(
            f"SELECT unsplash_id FROM {self.table_name} WHERE animal_id = %s",
            (animal_id,),
        )
        result = cur.fetchone()
        print(result)
        return result[0]
