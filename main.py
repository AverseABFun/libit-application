import json
from flask import Flask, request, jsonify
import sqlite3
import uuid

app = Flask(__name__)
con = sqlite3.connect("notes.db")
cur = con.cursor()
res = cur.execute("SELECT name FROM sqlite_master")
if res.fetchone() is None:
    cur.execute("CREATE TABLE notes(id, note)")
    con.commit()

@app.route('/', methods=['GET'])
def get_note():
    id = request.args.get('id')
    print(id)
    res = cur.execute("SELECT note FROM notes WHERE id=?", [id])
    result = res.fetchone()
    if result is None:
        return jsonify({"error": True, "errCode": 1, "errMsg": "Note not found"})
    else:
        return jsonify({"error": False, "result": result})

@app.route('/', methods=['PUT'])
def create_note():
    noteData = request.args.get('data')
    id = uuid.uuid4()
    cur.execute("U")

@app.route('/', methods=['POST'])
def update_note():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delete_note():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(debug=True)