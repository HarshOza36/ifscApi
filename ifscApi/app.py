from flask import Flask, request, jsonify, render_template
import sqlite3
import timeit
import os
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


# db_file = 'db/ifsc.db'
# db_file = 'ifsc.db'
dirname = os.path.dirname(__file__)
db_file = dirname+'\\db\\ifsc.db'


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
        print(row)
        return(row)


class fetchData(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('ifsc', required=True, help="ifsc cannot be blank!")
        args = parse.parse_args()
        x = args['ifsc']
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
            response = jsonify(retMap)
        else:
            print("IFSC:"+str(x)+" BANK:"+str(a[1])+" ADDRESS:"+str(a[2]))
            end = timeit.default_timer()
            retMap = {'status': 200, 'IFSC': str(x), 'BANK': str(
                a[1]), 'ADDRESS': str(a[2]), 'timeTOFetch': end-start}
            response = jsonify(retMap)

        print('Time:{}s to fetch'.format(end-start))
        return response


@app.route('/')
def index():
    return(render_template("index.html"))


@app.route('/getit', methods=['GET', 'POST'])
def getit():
    x = request.form['ifsc']

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
        response = jsonify(retMap)
        print(response)
        ifsc = str(x)
        bank = 'Not Found'
        add = 'Not Found'
        return(render_template("index.html", bank=bank, add=add, ifsc=ifsc))
    else:
        end = timeit.default_timer()
        retMap = {'status': 200, 'IFSC': str(x), 'BANK': str(
            a[1]), 'ADDRESS': str(a[2]), 'timeTOFetch': end-start}
        response = jsonify(retMap)
        print('Time:{}s to fetch'.format(end-start))
        print(response)
        ifsc = str(x)
        bank = str(a[1])
        add = str(a[2])
        # return response
        return(render_template("index.html", bank=bank, add=add, ifsc=ifsc))


api.add_resource(fetchData, '/ifsc')


def runServer():
    #    if __name__ == "__main__":
    print("[INFO] Server will start ...")
    app.run(debug=True)


if __name__ == "__main__":
    runServer()
