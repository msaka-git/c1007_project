import sqlite3
import os
from pathlib import Path

upper_level_path = Path(__file__).resolve().parents[1]
db_path = str(upper_level_path)+os.sep+'db_CAR.db'

con = sqlite3.connect(db_path)


def cursor_execute(func):
    def wrapper(*args):
        cursor = con.cursor()
        operation = func(*args)
        data = cursor.execute(operation)
        data_ = data.fetchall()
        cursor.close()
        return data_
    return wrapper

@cursor_execute
def fetch_select_data(select_item,db_table):
    query_construct = "select {} from {};".format(select_item,db_table)
    return query_construct

@cursor_execute
def fetch_select_where(select_item,db_table,condition):
    query_construct = "select {} from {} where {};".format(select_item, db_table,condition)
    return query_construct

def save_result(db_table,*values):
    cur = con.cursor()

    query_insert = "insert into {} values {};".format(db_table,values)
    #print(query_insert)

    cur.execute(query_insert)
    con.commit()
    cur.close()



# INSERT INTO table1 (column1,column2 ,..)
# VALUES
#    (value1,value2 ,...),
#    (value1,value2 ,...),
#     ...
#    (value1,value2 ,...);
