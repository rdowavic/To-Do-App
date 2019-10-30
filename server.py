from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
        # put the database rows in my website
        conn = sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Items")
        rows = cur.fetchall()
        conn.close()
        return render_template('index.html', items=rows)

