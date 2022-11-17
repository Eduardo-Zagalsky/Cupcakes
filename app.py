"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/api/cupcakes")
def get_cupcakes():
    serialized = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def post_cupcakes():
    cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'],
                      rating=request.json['rating'], img=request.json['img'])

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def patch_cupcake(cupcake_id):
    return
