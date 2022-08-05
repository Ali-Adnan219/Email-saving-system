import sqlite3

def connect():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS datas (id INTEGER PRIMARY KEY,email text, pass text, types text,notes text,timenow text)")
    conn.commit()
    conn.close()

def insert(email,pas,types,notes,timenow):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO datas VALUES (NULL,?,?,?,?,?)",(email,pas,types,notes,timenow))
    conn.commit()
    conn.close()

def View():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM datas")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(email="",pas="",types="",notes="",timenow=""):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM datas WHERE email=? OR pas=? OR types=? OR notes=?",(email ,pas , types , notes , timenow))
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteitem(id):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM datas WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,email,pas,types,notes,):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("UPDATE datas SET email=?, pas=?, types=?, notes=? WHERE id=?",(email,pas,types,notes,id))
    conn.commit()
    conn.close()

connect()#automatically gets called when frontend file executed
