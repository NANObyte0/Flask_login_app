from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Credentials
users = {
    "Nano": "nano0",
    "Alice": "alice123",
    "Bob": "bobpassword",
    "Eve": "eve007",
    "Charlie": "charliepw"
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get to form data
        username = request.form.get("username")
        password = request.form.get("password")
        
        print("Username entered:", username)
        print("Password entered:", password)


        #Check Credentiols
        if username in users and users[username] == password:
           return redirect(url_for("welcome", username=username))
        else:
            
            return render_template("login.html",
                                    error="LOGIN FAILD YOU ARE NOT NANO")
    return render_template("login.html")
@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html",username=username)
  
if __name__ == "__main__":
    app.run(debug=True)

    