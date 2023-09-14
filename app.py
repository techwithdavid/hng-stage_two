from flask import Flask, request, jsonify
import sqlite3 as s3

app = Flask(__name__)

connect = s3.connect('hng_stage_two.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(256))'''
        )

connect.commit()
connect.close()

@app.route('/api/<int:user_id>', methods=['GET'])
def retrieve_person(user_id):
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM person WHERE id=?', (user_id,))
        person = cursor.fetchone()
        connect.close()

        if person is None:
            abort(404)
        person_to_dict = {"id": person[0], "name": person[1]}
        return jsonify(person_to_dict)
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
            if not request.json:
                abort(400)

            data = request.get_json()
            name = data['name']

            cursor.execute('INSERT INTO person (name) VALUES (?)', (name,))
            connect.commit()
            connect.close()

            return jsonify({
                "status": "Successful",
                "message": f"{name} created successfully"
                }), 201
    except Exception as e:
        return jsonify({
            "status": "Not successful",
            "message": str(e)
            })

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json:
        abort(400)

    data = request.get_json()
    name = data['name']

    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('UPDATE person SET name = ? WHERE id = ?', (name, user_id))
        connect.commit()
        connect.close()

        return jsonify({"status": "Successful"})
    except Exception as e:
        return jsonify({
            "status": "Not successful",
            "message": str(e)
            })

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        connect = s3.connect('hng_stage_two.db')
        cursor = connect.cursor()
        cursor.execute('DELETE FROM person WHERE id = ?', (user_id,))
        connect.commit()
        connect.close()

        return jsonify({"status": "Successful"})
    except Exception as e:
        return jsonify({
            "status": "Not successful",
            "message": str(e)
            })

if __name__=="__main__":
    app.run(debug=True)
