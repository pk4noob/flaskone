from flask import Flask, request, jsonify, send_file, send_from_directory
from app.model import User
from app.seralize import UserSchema
from app_init.app_factory import createAp
from http import HTTPStatus
from marshmallow import ValidationError
from pprint import pprint
from pprint import pprint


app = createAp()


@app.route("/user", methods=["POST"])
def createPost():
    data = request.get_json()
    try:
        x = UserSchema().load(data)
        x.pasword_hash()
        x.savedb()
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    return UserSchema().jsonify(x), HTTPStatus.OK


@app.route("/user/<int:id>", methods=["GET"])
def createget(id):
    dataa = User.query.filter_by(id=id).first()
    if dataa:
        return UserSchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="Error"), HTTPStatus.NOT_FOUND


@app.route("/user", methods=["GET"])
def createAll():
    dataAll = User.query.all()
    return UserSchema().jsonify(dataAll, many=True), HTTPStatus.OK


@app.route("/user/<int:id>", methods=["PUT"])
def createupd(id):
    dataupd = User.query.filter_by(id=id).first()
    if dataupd:
        userr = request.get_json()
        dataupd.update(**userr)
        return UserSchema().jsonify(userr), HTTPStatus.OK
    return jsonify(msg="Error"), HTTPStatus.NOT_FOUND


@app.route("/user/<int:id>", methods=["DELETE"])
def deletee(id):
    dell = User.query.filter_by(id=id).first()
    if dell:
        dell.deletedb()
        return jsonify(msg="delete"), HTTPStatus.OK
    return jsonify(msg="ERROR"), HTTPStatus.NOT_FOUND


@app.route("/user/<int:id>/file", methods=["POST"])
def filepost(id):
    name = User.query.filter_by(id=id).first()
    if name:
        for _, val in request.files.items():
            name.update(filename=val.filename)
            with open(val.filename, "wb") as wr:
                wr.write(val.read())
                return jsonify(msg="Olundu"), HTTPStatus.OK
    return jsonify(msg="Eror"), HTTPStatus.NOT_FOUND


@app.route("/user/<int:id>/file", methods=["GET"])
def fileGet(id):
    us = User.query.filter_by(id=id).first()
    if us:
        if us.filename:
            # return send_file(us.filename, mimetype="img/png"), HTTPStatus.OK
            return send_from_directory(
                "/home/orxan/Documents/flasktwo/",
                filename=us.filename,
                mimetype="image/png",
            )
    return jsonify(msg="Error"), HTTPStatus.BAD_REQUEST


@app.route("/user/file", methods=["GET"])
def fileAll():
    user = User.query.all()
    return send_from_directory(
        "/home/orxan/Documents/flasktwo/",
        filename=user.filename,
        mimetype="image/png",
    ), HTTPStatus.OK


# response = request.get("http://127.0.0.1:5000/orxansusers")
# print(response.status_code)
# pprint(response.json())

# response = requests.post(
#     "http://127.0.0.1:5000/orxansusers",
#     json={
#         "surname": "Memmedaliyeva",
#         "name": "Naile",
#         "password": "12213415",
#         "email": "tetst1@test.ru",
#     },
# )

# # print(response.status_code)
# # pprint(response.json())


# user_data = {"name": "Tural", "surname": "Memmedov"}

# response = requests.put("http://127.0.0.1:5000/orxansusers/1", json=user_data)

# print(response.status_code)
# pprint(response.json())


# response = requests.get("https://www.offer.az")

# html = response.text
# html = html.replace("4745", "1231231321312")

# with open("index.html", "w") as wr:
#     wr.write(html)


# myfile = open("index.html", "r", encoding="ascii", errors="ignore")
# # for i in myfile.readlines():
# #     print(i)
# # print(myfile.read())
# myfile2 = open("index2.hmtl", "w", encoding="ascii", errors="ignore")
# myfile2.write(myfile.read())

# myfile.close()
# myfile2.close()

# with open("index.html", "a") as wr:
#     wr.write("tural")
