from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)


with app.app_context():
    db.create_all()


@app.route("/users")
def get_users():

    users = User.query.all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        }
        for user in users
    ]

@app.route("/users",methods=["POST"])
def add_user():
    data = request.get_json()
    user = User(
        name=data.get("name"),
        age=data.get("age"),
        email=data.get("email")
    )
    db.session.add(user)
    db.session.commit()
    return "User Adeed"

@app.route("/create-100-users", methods=["GET"])
def create_100_users():

    users = []

    names = [
        "Ravi Kumar",
        "Arjun Reddy",
        "Rahul Sharma",
        "Kiran Kumar",
        "Vijay Rao",
        "Suresh Babu",
        "Praveen Kumar",
        "Sai Krishna",
        "Rohit Sharma",
        "Akhil Reddy",
        "Naveen Kumar",
        "Vamsi Krishna",
        "Manoj Kumar",
        "Anil Kumar",
        "Pavan Kumar",
        "Teja Reddy",
        "Harsha Vardhan",
        "Karthik Rao",
        "Dinesh Kumar",
        "Surya Prakash"
    ]

    for i in range(100):

        name = names[i % len(names)]

        user = User(
            name=f"{name} {i + 1}",
            age=18 + (i % 23),
            email=f"user{i + 1}@gmail.com"
        )

        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    return jsonify({
        "message": "100 users created successfully"
    }), 201

@app.route("/users/<int:id>",methods=["GET"])
def get_user(id):
    data = User.query.get(id)
    return {
        "name":data.name,
        "email":data.email
    }

@app.route("/all_users",methods=["GET"])
def adding_user():
    data = request.args
    print(data.get("id"))
    return "huu"
if __name__ == "__main__":
    app.run(debug=True)