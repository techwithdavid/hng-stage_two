from flask import Flask, request, jsonify
import sqlite3 as s3

app = Flask(__name__)

connect = s3.connect('hng_stage_two.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS person (
        id INT AUTOINCREMEMT,
        name VARCHAR(256),
        PRIMARY KEY (id))'''
        )

connect.commit()
connect.close()

@app.route('api/<int:user_id>', methods=['GET'])
def retrieve_person(user_id):
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM person WHERE id=?', (user_id,))

        data = cursor.fetchone()
        return jsonfiy(data)
    except:
        return jsonify({'status': 'Not successful'})

if __name__=="__main__":
    app.run(debug=True)
