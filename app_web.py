from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_cambiala'  # Cambiala por algo seguro

DB_PATH = Path(__file__).parent / "db" / "bar.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM system_user WHERE username = ?", (username,)).fetchone()
        conn.close()

        # Validación simple: comparar texto plano (mejorar con hash en producción)
        if user and password == user["password_hash"]:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            flash("Login exitoso", "success")
            return redirect(url_for("menu"))
        else:
            flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")

@app.route("/menu")
def menu():
    if "user_id" not in session:
        flash("Por favor logueate primero", "error")
        return redirect(url_for("login"))

    # En lugar de mostrar menú simple, redirigimos a la vista de mesas
    return redirect(url_for("mesas"))

@app.route("/mesas")
def mesas():
    if "user_id" not in session:
        flash("Por favor logueate primero", "error")
        return redirect(url_for("login"))

    conn = get_db_connection()
    mesas = conn.execute("SELECT id, number, active, status FROM tables ORDER BY number").fetchall()
    conn.close()

    return render_template("mesas.html", mesas=mesas)


@app.route("/caja")
def caja():
    if "user_id" not in session:
        flash("Por favor logueate primero", "error")
        return redirect(url_for("login"))
    # Si querés, podés chequear rol aquí (más adelante)
    return render_template("caja.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
