from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lost_and_found"
)
cursor = db.cursor(dictionary=True)

# ===========================
# Admin Dashboard Counters
# ===========================
@app.route("/admin/dashboard")
def admin_dashboard():
    cursor.execute("SELECT COUNT(*) AS total_lost FROM reports WHERE type='Lost'")
    lost = cursor.fetchone()['total_lost']

    cursor.execute("SELECT COUNT(*) AS total_found FROM reports WHERE type='Found'")
    found = cursor.fetchone()['total_found']

    cursor.execute("SELECT COUNT(*) AS total_users FROM users")
    users = cursor.fetchone()['total_users']

    cursor.execute("SELECT * FROM reports ORDER BY date DESC LIMIT 10")
    recent = cursor.fetchall()

    return render_template("admin_dashboard.html",
                           lost=lost, found=found,
                           users=users, recent=recent)

# ===========================
# View Lost Items
# ===========================
@app.route("/admin/view_lost")
def view_lost():
    cursor.execute("SELECT * FROM reports WHERE type='Lost'")
    data = cursor.fetchall()
    return render_template("view_lost.html", items=data)

# ===========================
# View Found Items
# ===========================
@app.route("/admin/view_found")
def view_found():
    cursor.execute("SELECT * FROM reports WHERE type='Found'")
    data = cursor.fetchall()
    return render_template("view_found.html", items=data)

# ===========================
# Manage Users
# ===========================
@app.route("/admin/users")
def manage_users():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template("manage_users.html", users=data)

# ===========================
# Messages (Admin Inbox)
# ===========================
@app.route("/admin/messages")
def admin_messages():
    cursor.execute("""
        SELECT m.message_id, u.name AS sender, m.message, m.date_time
        FROM messages m
        JOIN users u ON m.sender_id = u.user_id
        WHERE receiver_id = 1  -- admin id
        ORDER BY m.date_time DESC
    """)
    inbox = cursor.fetchall()
    return render_template("messages.html", inbox=inbox)


if __name__ == "__main__":
    app.run(debug=True)