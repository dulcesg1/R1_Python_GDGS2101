from flask import Flask, render_template, make_response, jsonify, request,redirect, url_for, session
app = Flask(__name__)
#from flask_mysqldb import MySQL,MySQLdb # pip install Flask-MySQLdb
from os import path #pip install notify-py
from notifypy import Notify
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MYSQL_HOST'] = 'localhost:3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app_citas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

PORT = 3200

# Get Method

INFO = {
    "pastasdos": {
        "pr":"Penne Rigate",
        "ft":"Fusilli Tricolor",
        "sa":"Spaghettini de Arroz",
    },
    "pastasuno":{
        "r":"Ramen",
        "m":"Macarrones",
        "f":"Farfalle",
    },
    "noodles":{
        "UD":"UDON",
        "SO":"SOBA",
        "SOM":"SOMEN",
    }
}

@app.route("/")
def home():
   return render_template("contenido.html")

@app.route('/temp')
def hello_world():
    return render_template('index.html')

@app.route("/qstr")
def qs():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res

    res = make_response(jsonify({"error": "No Query String"}), 404)
    return res
#GET Method
@app.route("/json")
def get_json():
    res = make_response(jsonify({"Pastas":INFO}), 200)
    return res

@app.route("/json/<collection>/<member>")
def get_data(collection, member):
    print("getting the value of %s in the collection %s"%(member,collection))
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

# Post Method

@app.route("/json/<collection>", methods=["POST"])
def create_col(collection):

    req = request.get_json()

    if collection in INFO:
        res = make_response(jsonify({"error": "Collection already exists"}), 400)
        return res

    INFO.update({collection: req})

    res = make_response(jsonify({"message": "Collection created"}), 201)
    return res

# Put Method

@app.route("/json/<collection>/<member>", methods=["PUT"])
def put_col_mem(collection,member):

    req = request.get_json()

    if collection in INFO:
        if member:
            print(req)
            INFO[collection][member] = req["new"]
            res = make_response(jsonify({"res":INFO[collection]}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

# Delete Method

@app.route("/json/<collection>", methods=["DELETE"])
def delete_col(collection):

    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO), 200)
        return res

    res = make_response(jsonify({"error": "Collection not found"}), 404)
    return res

#Templates 
@app.route('/ver')
def ver():
    return render_template("ver_pastas.html") 

@app.route('/layout', methods = ["GET", "POST"])
def layout():
    session.clear()
    return render_template("contenido.html") 

@app.route('/login', methods= ["GET", "POST"])
def login():

    notificacion = Notify()

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return render_template("premium/home.html")
            
        #cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        #user = cur.fetchone()
        #cur.close()

        #if len(user)>0:
         #   if password == user["password"]:
          #      session['name'] = user['name']
          #      session['email'] = user['email']
           #     session['tipo'] = user['id_tip_usu']

            #    if session['tipo'] == 1:
            #    elif session['tipo'] == 2:
             #       return render_template("estandar/homeTwo.html")


        #    else:
         #       notificacion.title = "Error de Acceso"
          #      notificacion.message="Correo o contraseña no valida"
           #     notificacion.send()
            #    return render_template("login.html")
       # else:
            #notificacion.title = "Error de Acceso"
            #notificacion.message="No existe el usuario"
            #notificacion.send()
            #return render_template("login.html")
    else:
        
        return render_template("login.html")



@app.route('/registro', methods = ["GET", "POST"])
def registro():

    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM tip_usu")
    #tipo = cur.fetchall()

    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM sexo_interes")
    #interes = cur.fetchall()

    #cur.close()

    notificacion = Notify()
    
    

    if request.method == 'GET':
        return render_template("registro.html", tipo = '', interes = '' )
    
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tip = request.form['tipo']
        interes = request.form['interes']

        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES (%s,%s,%s,%s,%s)", (name, email, password,tip,interes,))
        #mysql.connection.commit()
        notificacion.title = "Registro Exitoso"
        notificacion.message="ya te encuentras registrado en Pastas Shop, por favor inicia sesión y empieza a descubrir este nuevo mundo."
        notificacion.send()
        return redirect(url_for('login'))

#if __name__ == "__main__":
#   print("Server running in port %s"%(PORT))
#    app.run(host='0.0.0.0', port=PORT)