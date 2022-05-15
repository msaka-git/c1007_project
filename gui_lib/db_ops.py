import sqlite3

def connector_db():
    con = sqlite3.connect('db_CAR.db')
    cursor = con.cursor()
    return cursor

def cursor_execute(func):
    def wrapper(*args):
        cursor = connector_db()
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



