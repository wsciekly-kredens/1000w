from random import randint
import word as wr
import psycopg2 as pc
import dbconfig as dbc


class GeneralLogic:
    conn: object
    cursor: object
    set_num: int
    set: list

    def __init__(self, set_num):
        self.conn = pc.connect(database=dbc.database, user=dbc.user, password=dbc.password, host=dbc.host,
                               port=dbc.port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.set_num = set_num

    def setSelect(self, set_num=None): #dostępne zestawy od 1 do 11, oraz zestaw trudniejszych pod 2137
        if (set_num == None):
            set_num = self.set_num
        elif(set_num==2137):
            self.harderWardsSelect() #można zrefakorować
            return
        self.cursor.execute('SELECT * FROM words WHERE set = %s ORDER BY word_id', str(set_num))
        self.set = self.cursor.fetchall()


    def harderWardsSelect(self):
        self.cursor.execute('SELECT * FROM words WHERE stopien_opanowania = \'Tak\' ORDER BY word_id')
        self.set = self.cursor.fetchall()

    def wordSelect(self, set):
        index = randint(0, len(set)-1)
        w = set.pop(index)
        w1 = wr.Word(w[1], w[2], w[0])
        if not w[3] == "Null":
            w1.setNote(w[3])
        return w1

    def appLesson(self):
        self.setSelect()
        fixedSet = self.set.copy()
        for i in range(10):
            word = self.wordSelect(fixedSet)
            print(len(fixedSet))
            notatka = word.note
            print(f"\nCo to znaczy? \n{word.pol}")
            odp = input()
            if odp == word.de:
                print("Dobrze!")
                word.stopien = "Tak"
            else:
                if not (notatka == None):
                    print(notatka)
                    odp = input()
                    if odp == word.de:
                        print("Dobrze!")
                        word.stopien = "Tak"
                    else:
                        word.stopien = "Nie"
                        print(f"Źle, poprawna odpowiedź:\n{word.de}")
                        literowka = input("Czy zrobiłeś literówkę? [Y/n] ")
                        if literowka == "Y":
                            print("Dobrze")
                            word.stopien = "Tak"
                else:
                    word.stopien = "Nie"
                    print(f"Źle, poprawna odpowiedź:\n{word.de}")
                    literowka = input("Czy zrobiłeś literówkę? [Y/n] ")
                    if literowka == "Y":
                        print("Dobrze")
                        word.stopien = "Tak"
                    elif notatka == None:
                        czyn = input("Czy dodać notatke?[Y/n] ")
                        if czyn == "Y":
                            word.setNote(input("Podaj notatke: "))
                            word.noteToDB(self.conn)
            word.stopienToDB(self.conn)
