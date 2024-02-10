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
    con = sqlite3.connect("notes.db")
    cur = con.cursor()
    res = cur.execute("SELECT note FROM notes WHERE id=?", [id])
    result = res.fetchone()
    if result is None:
        return jsonify({"error": True, "errCode": 1, "errMsg": "Note not found"})
    else:
        return jsonify({"error": False, "result": result[0]})

@app.route('/', methods=['PUT'])
def create_note():
    noteData = request.args.get('note')
    id = str(uuid.uuid4())
    con = sqlite3.connect("notes.db")
    cur = con.cursor()
    cur.execute("INSERT INTO notes VALUES(?, ?)", [id, noteData])
    con.commit()
    return jsonify({"error": False, "result": id})

@app.route('/', methods=['POST'])
def update_note():
    noteId = request.args.get('id')
    noteData = request.args.get('note')
    con = sqlite3.connect("notes.db")
    cur = con.cursor()
    cur.execute("UPDATE notes SET note=? WHERE id=?", [noteData, noteId])
    con.commit()
    return jsonify({"error": False, "result": ""})
    
@app.route('/', methods=['DELETE'])
def delete_note():
    noteId = request.args.get('id')
    con = sqlite3.connect("notes.db")
    cur = con.cursor()
    res = cur.execute("SELECT note FROM notes WHERE id=?", [noteId])
    result = res.fetchone()
    if result is None:
        return jsonify({"error": True, "errCode": 1, "errMsg": "Note not found"})
    cur.execute("DELETE FROM notes WHERE id=?", [noteId])
    con.commit()
    return jsonify({"error": False, "result": result[0]})

app.run(debug=True)