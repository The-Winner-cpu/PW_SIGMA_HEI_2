from flask import Flask, request, jsonify 
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/users")
def getusers():
    return "Liste des utilisateurs"

@app.route("/users/<int:user_id>") 
def getuser(userid):
    return f"Utilisateur {userid}" 

@app.route("/users", methods=["POST"]) 
def create_user():
    return "Utilisateur créé" 

if __name__ == "__main__":
 app.run(debug=True)