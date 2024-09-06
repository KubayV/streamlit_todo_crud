
import sqlite3


conn = sqlite3.connect("data.db")
c = conn.cursor()


# database
# table
# field/columns
# datatype

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT, task_status TEXT, task_due_date DATE)')


def add_data(task, task_status, task_due_date):
    c.execute('INSERT INTO tasktable(task, task_status, task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
    conn.commit()


def view_all_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data


def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM tasktable')
    data = c.fetchall()
    return data


def get_task(task):
    c.execute('SELECT * FROM tasktable WHERE task = "{}"'.format(task))
    # c.execute('SELECT * FROM tasktable WHERE task = ?',(task))
    data = c.fetchall()
    return data


def edit_task_data(new_task, new_task_status, new_task_date, task, task_status, task_due_date):
    c.execute('UPDATE tasktable SET task = ?, task_status = ?, task_due_date = ? WHERE task = ? and task_status =? '
              'and task_due_date = ?',(new_task, new_task_status, new_task_date, task, task_status, task_due_date))
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(task):
    c.execute('DELETE from tasktable WHERE task = "{}"'.format(task))
    conn.commit()
