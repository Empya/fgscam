from flask import Flask, render_template, session, url_for, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "iDi0tTest"

@app.route("/")

def home():
    return render_template("home.html")
    
    
@app.route("/get_funds/register/<int:amt>")

def show_form(amt):
    session["amt"] = amt
    return render_template("signup.html")
    
@app.route("/get_funds/readytransfer", methods=["POST","GET"])

def ready(): 

    if request. method == "POST":
        name = request.form["name"]
        session["name"] = name
        
        return render_template("result.html")
        
    else:
        return redirect (url_for("home"))
    
    
