from flask import Flask, request, jsonify
import sqlite3 as s3

app = Flask(__name__)

connect = s3.connect('hng_stage_two.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(256))'''
        )

# cursor.execute('INSERT INTO person (name) VALUES ("Ola")')
cursor.execute('SELECT * FROM person')

print(cursor.fetchall())

connect.commit()
connect.close()

@app.route('/api/<int:user_id>', methods=['GET'])
def retrieve_person(user_id):
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM person WHERE id=?', (user_id,))
        data = cursor.fetchone()
        connect.close()

        if data is None:
            abort(404)
        data_to_dict = {"id": data[0], "name": data[1]}
        return jsonify(data_to_dict)
    except Exception as e:
        return jsonify({'status': 'Not successful', 
                        'message': str(e)
            })

@app.route('/api', methods=['GET', 'POST'])
def create_person():
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()

        if request.method == 'GET':
            cursor.execute('SELECT * FROM person')
            persons = cursor.fetchall()
            connect.close()
            
            if persons is None:
                abort(404)
            persons_to_list = []
            for person in persons:
                person_to_dict = {
                        "id": person[0],
                        "name": person[1]
                        }
                persons_to_list.append(person_to_dict)

            return jsonify(persons_to_list)
        elif request.method == 'POST':
            pass
    except Exception as e:
        return jsonify({
            "status": "Not successful",
            "message": str(e)
            })


if __name__=="__main__":
    app.run(debug=True)
