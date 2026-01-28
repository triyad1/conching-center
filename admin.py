from flask import Flask

admin = Flask(__name__)

@admin.route("/dashboard")
def dashboard():
    return "Admin Panel - Control Users"

admin.run(port=5001)
