from flask import Flask, jsonify, request

# Creamos una aplicacion de flask
app = Flask(__name__)

# Creamos un endpoint
# app.route("/nombre o direccion de endpoint")


@app.route("/")
def hello_world():
    return "Hola estudiantes"
    # La funcion que devuelve el endpoint

# El metodo por defecto es GET


@app.route("/people")
def todo_list():
    people = {"people": "Luke Skywalker",
              "hair_color": "Yellow", "eye_color": "Blue"}
    return jsonify(people)


@app.route("/students", methods=["POST", "GET"])
def student_list():
    # POST -> Se utiliza para agregar elementos en la api
    if request.method == "POST":
        # De request(importado de flask)
        body = request.get_json()  # Me devuelve el body
        username = body["username"]  # Extraer el username
        password = body["password"]  # extraer el password
        email = body["email"]
        return f"Usuario: {username}, email: {email}"

    elif request.method == "GET":
        students = ["Octavio", "Pedro", "Christian", "Jose"]
        return jsonify(students)


@app.route("/todos", methods=["POST", "GET"])
def handle_todos():
    # request se importa desde flask

    # este if se ejecuta si el metodo es get
    if request.method == "GET":
        todos = [{
            "label": "Tarea de prueba",
            "done": False
        },
            {
            "label": "Tarea de prueba2",
            "done": False
        }]
        return todos

    elif request.method == "POST":
        # El body se extrae de request con el metodo get_json()
        body = request.get_json()

        # Estoy regresando errores
        if 'username' not in body:
            # Error de username required
            return "El username es necesario", 400
        if 'email' not in body:
            # Error de email required
            return "El email es necesario", 400
        if 'password' not in body:
            # Error de password requires
            return "La contraseña es necesaria", 400

        # Si todos los campos existen
        # Los extraemos
        username = body["username"]
        password = body["password"]
        email = body["email"]

        # Regreso un mensaje de exito
        return f"Se ha creado el usuario: {username} con correo: {email}", 201


# Para crear rutas dinamicas
# Se agrega la base "/todos/"
# y se agrega entre <typo_dato:nombre>
# y la funcion recibe el nombre
@app.route("/todos/<string:username>")
def get_by_id(username):
    print(username)
    return jsonify(username)


# Es necesario para flask
if __name__ == "__main__":
    app.run(host='0.0.0.0')
