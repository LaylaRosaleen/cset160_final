from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine, text
from

app = Flask(__name__)

conn_str = "mysql://root:bcSd4y&689#Hb@localhost/onesixfinalproject"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()


@app.route("/grades.html")
def get_grades():
    grades = conn.execute(text("select * from grades")).all()
    print(grades)
    return render_template("grades.html")


@app.route("/createtest", methods=['GET'])
def createtest():
    return render_template("create_boats.html")


@app.route("/createtest", methods=['POST'])
def createtest():
    conn.execute(text("INSERT INTO test_questions VALUES (:Test_ID, :Test_Name, :Question_1, :Question_2, :Question_3, "
                      ":Question_4, :Question_5, :created_by)"), request.form)
    conn.commit()


@app.route('/search.html', methods=['GET'])
def get_search():
    return render_template("search.html")


@app.route('/search.html', methods=['POST'])
def create_search():
    search = conn.execute(text('SELECT * FROM accounts WHERE id = :id'), request.form)
    search_info = search.fetchall()
    return render_template("search.html", search_info=search_info)


@app.route('/delete.html', methods=['GET'])
def delete():
    return render_template("delete.html")


@app.route('/delete.html', methods=['POST'])
def delete():
    conn.execute(text('DELETE FROM test_questions WHERE (test_id = :test_id)'), request.form)
    conn.commit()
    return render_template("delete.html")


@app.route('/edit.html', methods=['GET'])
def edit():
    return render_template("edit.html")


@app.route('/edit.html', methods=['POST'])
def edit():
    conn.execute(text("INSERT INTO test_questions VALUES (:Test_ID, :Test_Name, :Question_1, :Question_2, :Question_3, "
                      ":Question_4, :Question_5, :created_by)"), request.form)
    conn.commit()
    return render_template("edit.html")


if __name__ == '__main__':
    app.run(debug=True)
