import pymysql.cursors


class Host:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address


ats = []
efw = []

try:
    con = pymysql.connect(user='root', password='uxmwnhbm',
                             host='192.168.133.109', db='office',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM chisto_tree WHERE name LIKE 'АТС%'")
        rows = cursor.fetchall()
        for row in rows:
            ats.append(Host(row["name"], row["ip_local"]))
finally:
    cursor.close()
    con.close()

try:
    conn = pymysql.connect(user='root', password='uxmwnhbm',
                             host='192.168.133.109', db='office',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM chisto_tree WHERE gate=1")
        rows = cursor.fetchall()
        for row in rows:
            efw.append(Host(row["name"], row["ip_local"]))
finally:
    cursor.close()
    conn.close()