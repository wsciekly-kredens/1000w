class Word:
    pol: str
    de: str
    note: str
    stopien: str
    id: int
    def __init__(self,pol: str, de: str, id: int):
        self.pol = pol
        self.de = de
        self.id = id

    def setNote(self,note: str):
        self.note = note

    def setStopienOpanowania(self, stopien):
        self.stopien = stopien

    def __str__(self):
        return f"{self.pol} - {self.de} \nNotatka: {self.note}"

    def noteToDB(self, conn):
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE WORDS SET note = %s WHERE word_id = %s', (self.note, self.id)

        )
    def stopienToDB(self, conn):
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE WORDS SET stopien_opanowania = %s WHERE word_id = %s', (self.stopien, self.id)

        )