import sqlite3


def get_record():
    con = sqlite3.connect("saves_bd.sqlite")
    cur = con.cursor()
    res = cur.execute("SELECT level, stage FROM saves WHERE id = 2").fetchall()
    return res[0][:]

def get_progress():
    con = sqlite3.connect("saves_bd.sqlite")
    cur = con.cursor()
    res = cur.execute("SELECT level, stage FROM saves WHERE id = 1").fetchall()
    return res[0][:]

def set_progress(level, stage):
    con = sqlite3.connect("saves_bd.sqlite")
    cur = con.cursor()
    res_record = cur.execute("SELECT level, stage FROM saves WHERE id = 2").fetchall()
    s1 = '''UPDATE saves
SET level = '''
    s2 = ''', stage = '''
    s3 = '''
WHERE id = '''
    s = s1 + str(level) + s2 + str(stage)
    if res_record[0][0] < level or res_record[0][0] == level and res_record[0][1] < stage:
        cur.execute(s)
    else:
        cur.execute(s + s3 + '1')
    con.commit()
