import mysql.connector


def get_tasks():
    query = "SELECT todo, id FROM task_list ORDER BY todo"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    text = []
    ids = {}
    i=0
    length = len(result)
    if length == 0:
        return "", 0
    while i < length:
        text.append(result[i][0])
        ids[result[i][0]] = result[i][1]
        i += 1
    cursor.close()
    conn.close()
    return text, ids


def insert_task(task):
    query = "INSERT into task_list (todo) VALUE (%s)"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()
    cursor.execute(query, (task,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_task(id_task):
    query = "DELETE FROM task_list WHERE id=%s"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()
    cursor.execute(query, (id_task,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    (result, ids) = get_tasks()
    print(result)
