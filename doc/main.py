from flask import Flask, request, jsonify
# texh with tim ! be careful create user may need to be recoded
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get_user/<user_id>")
def get_user(user_id):
    # request for data here
    user_data = {
        "user_id":user_id,
        "name":"name"
    }
    extra = request.args.get("extra")
    if extra :
        user_data["extra"]=extra
        
    return jsonify(user_data),200

@app.route("/create_user/",methods=["POST"])
def create_user():
    data = None
    if request.method == "POST":
        data.request.get_json()
        # create user in db
        
    return jsonify(data), 201

if __name__=="__main__":
    app.run(debug=True)