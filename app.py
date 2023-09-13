from flask import Flask, request, jsonify
import sqlite3 as s3

app = Flask(__name__)

connect = s3.connect('hng_stage_two.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(256))'''
        )

cursor.execute('INSERT INTO person (name) VALUES ("Ola")')

connect.commit()
connect.close()

@app.route('/api/<int:user_id>', methods=['GET'])
def retrieve_person(user_id):
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM person WHERE id=?', (user_id,))

        data = cursor.fetchone()

        if data is None:
            abort(404)
        data_to_dict = {"id": data[0], "name": data[1]}
        return jsonify(data_to_dict)
    except:
        return jsonify({'status': 'Not successful'})

@app.route('/api', methods=['POST'])
def create_person():
    pass

if __name__=="__main__":
    app.run(debug=True)
