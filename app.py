from flask import Flask

app= Flask(__name__)

@app.route("/") #base route or home route 
def home():
    return "welcome to the home page of the notes app"


@app.route("/contact")
def contact():
    return "<h2> contact us at official @sgmail.com </h2>"

@app.route("/about")
def about():
    return "<h3> Hi i am bikram gorai ,a second yaer student at AEC </h3>"


if __name__ == "__main__":
    # This checks: "Is this file run directly?"
    # It prevents the server from starting if imported elsewhere

    app.run(debug=True)
       # Starts the Flask development server
       # debug=True → auto-restart + detailed error messages