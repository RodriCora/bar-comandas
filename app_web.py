from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
from pathlib import Path

from users import usuarios              # login general
from meseras import meseras, supervisores  # login personal

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_cambiala'

DB_PATH = Path(__file__).parent / "db" / "bar.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# LOGIN GENERAL
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_data = usuarios.get(username)

        if user_data and user_data["password"] == password:
            session.clear()
            session["user"] = username
            session["rol"] = user_data["rol"]

            flash("Login exitoso", "success")
            return redirect(url_for("menu_principal"))

        flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")


# =========================
# LOGIN PERSONAL (MOZAS / SUPERVISOR)
# =========================
@app.route("/login-personal", methods=["GET", "POST"])
def login_personal():
    if "user" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")

    if rol not in ["mozas", "supervisor"]:
        flash("Acceso no autorizado", "error")
        return redirect(url_for("menu_principal"))

    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        usuarios_personal = meseras if rol == "mozas" else supervisores

        if usuario in usuarios_personal and usuarios_personal[usuario] == password:
            session["personal"] = usuario
            flash(f"Bienvenida/o {usuario}", "success")
            return redirect(url_for("mesas"))

        flash("Usuario o contraseña incorrectos", "error")

    return render_template("login_mesera.html")


# =========================
# MENU PRINCIPAL
# =========================
@app.route("/menu")
def menu_principal():
    if "user" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")

    # mozas y supervisor NO ven menú → login personal
    if rol in ["mozas", "supervisor"]:
        return redirect(url_for("login_personal"))

    return render_template("menu.html", rol=rol, user=session.get("user"))


# =========================
# MAPA DE MESAS
# =========================
@app.route("/mesas")
def mesas():
    if "user" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")
    if rol in ["mozas", "supervisor"] and "personal" not in session:
        return redirect(url_for("login_personal"))

    conn = get_db_connection()
    rows = conn.execute("SELECT number, status FROM tables").fetchall()
    conn.close()

    estados = {n: 'libre' for n in [1,2,3,4,5,6,11,12,14,15,16,31,32,33,34]}
    for row in rows:
        estados[row["number"]] = row["status"].lower()

    return render_template(
        "mesas.html",
        estados=estados,
        rol=rol,
        user=session.get("user"),
        personal=session.get("personal")
    )


# =========================
# CAMBIAR ESTADO MESA
# =========================
@app.route("/mesa/<int:numero>/estado/<estado>")
def cambiar_estado_mesa(numero, estado):
    if "user" not in session:
        return redirect(url_for("login"))

    if estado not in ["libre", "ocupada", "cobro", "reservada"]:
        flash("Estado inválido", "error")
        return redirect(url_for("mesas"))

    conn = get_db_connection()
    conn.execute(
        "UPDATE tables SET status = ? WHERE number = ?",
        (estado, numero)
    )
    conn.commit()
    conn.close()

    flash(f"Mesa {numero} ahora está {estado}", "success")
    return redirect(url_for("mesas"))


# =========================
# ORDEN (A FUTURO GUARDAR EN DB)
# =========================
@app.route('/orden/<int:mesa>', methods=['GET', 'POST'])
def orden(mesa):
    if "user" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")
    if rol in ["mozas", "supervisor"] and "personal" not in session:
        return redirect(url_for("login_personal"))

    if request.method == 'POST':
        # Recibir productos desde JS (de momento solo simulamos)
        productos = request.json.get('productos')
        # Aquí podrías guardar en la base, si querés luego.
        return jsonify({'status': 'ok', 'mesa': mesa, 'productos': productos})

    # GET: mostrar plantilla orden (si querés mostrar orden guardada, la cargas acá)
    orden_guardada = []  # Podés reemplazar con DB real
    return render_template('orden.html', mesa=mesa, orden=orden_guardada)


# =========================
# CAJA
# =========================
@app.route("/caja")
def caja():
    if "user" not in session:
        return redirect(url_for("login"))

    if session.get("rol") != "caja":
        flash("Acceso restringido", "error")
        return redirect(url_for("menu_principal"))

    return render_template("caja.html")


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
