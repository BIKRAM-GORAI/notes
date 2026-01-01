from flask import Flask,render_template

app= Flask(__name__)

@app.route("/") #base route or home route 
def home():
    return render_template("home.html")


@app.route("/contact")
def contact():
    phno= "12345431"
    email= "notes@gmail.com"
    return render_template("contact.html",phno=phno,email=email)

@app.route("/about")
def about():
    username = "Bikram123"
    return render_template("about.html",name=username) #sending data to the frontend 
        #catching data in about.html


if __name__ == "__main__":
    # This checks: "Is this file run directly?"
    # It prevents the server from starting if imported elsewhere

    app.run(debug=True)
       # Starts the Flask development server
       # debug=True → auto-restart + detailed error messages