from flask import Flask
from extensions.extersions import ma,db


def createAp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///userdb"
    db.init_app(app)
    ma.init_app(app)
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    # db.drop_all()
    return app