from flask import Flask, render_template, redirect, url_for, request
import psycopg2

app = Flask(__name__)


# finalizar
@app.route('/')
def index():
    conn = psycopg2.connect(database="app_db", user="postgres", 
                            password="root", host="localhost", 
                            port="5432")
    
    cursor = conn.cursor()

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', data=dados)





if __name__ == '__main__':
    app.run(debug=True)



