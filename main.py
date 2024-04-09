from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

conn_str = "mysql://root:bcSd4y&689#Hb@localhost/onesixfinalproject"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()

# @app.route("/boats")
# def get_boats():
#     boats = conn.execute(text("select * from boats")).all()
#     print(boats)
#     return render_template("boats.html", boats_info=boats[0:10])
#
# @app.route("/createboat", methods=['GET'])
# def create_get():
#     return render_template("create_boats.html")
#
#
# @app.route("/createboat", methods=['POST'])
# def create_boat():
#     conn.execute(text("INSERT INTO boats VALUES (:id, :name, :type, :owner_id, :rental_price)"), request.form)
#     conn.commit()
# @app.route('/search', methods=['GET'])
# def get_search():
#     return render_template("search.html")
#
#
# @app.route('/search', methods=['POST'])
# def create_search():
#     search = conn.execute(text('SELECT * FROM boats WHERE id = :id'), request.form)
#     search_info = search.fetchall()
#     return render_template("search.html", search_info=search_info)
#
# @app.route('/delete', methods=['GET'])
# def get_delete():
#     return render_template("delete.html")
#
#
# @app.route('/delete', methods=['POST'])
# def delete():
#     conn.execute(text('DELETE FROM boats WHERE (id = :id)'), request.form)
#     conn.commit()
#     return render_template("delete.html")
#
#
# @app.route('/update', methods=['GET'])
# def get_update():
#     return render_template("update.html")
#
#
# @app.route('/update', methods=['POST'])
# def create_update():
#     conn.execute(text('UPDATE boats SET name = :name, type = :type, owner_id = :owner_id,'
#                       ' rental_price = :rental_price where (id = :id)'), request.form)
#     conn.commit()
#     return render_template("update.html")

if __name__ == '__main__':
    app.run(debug=True)
