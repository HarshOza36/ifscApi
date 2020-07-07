import sqlite3
import timeit
import os
import json
dirname = os.path.dirname(__file__)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT ifsc,bank,address FROM data where ifsc =?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        #         print(row)
        return(row)


class FetchData():
    def getdata(self, ifsc, dbfilePath=dirname+'\\ifsc2.db'):
        x = ifsc
        db_file = str(dbfilePath)
        # Establishing a connection
        conn = create_connection(db_file)
        retMap = {}
        a = None
        start = timeit.default_timer()
        a = select_task_by_priority(conn, str(x))
        if(a == None):
            print("Sorry ifsc doesnt exist")
            end = timeit.default_timer()
            retMap = {
                'status': 400,
                'IFSC': str(x),
                'details': 'Sorry ifsc not found',
                'timeTOFetch': end-start
            }
            response = json.dumps(retMap)
        else:
            #             print("IFSC:"+str(x)+" BANK:"+str(a[1])+" ADDRESS:"+str(a[2]))
            end = timeit.default_timer()
            retMap = {'IFSC': str(x), 'BANK': str(
                a[1]), 'ADDRESS': str(a[2]), 'timeTOFetch': end-start}
            response = json.dumps(retMap)

        print('Time:{}s to fetch'.format(end-start))
        return response
