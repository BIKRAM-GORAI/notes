from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

#lets make the database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
# sqlite:///notes.db means:
# - SQLite database
# - File name: notes.db
# - Stored in project folder

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Turns off an unnecessary feature (saves memory)

db = SQLAlchemy(app)
# db is the database object we will use everywhere


# making  the data model

class Note(db.Model):  #Note -> table name in the database
    id=db.Column(db.Integer,primary_key=True)


    title=db.Column(db.String(100),nullable=False)
    #cannot be empty

    content=db.Column(db.String(1000),nullable=False)
    #cannot be empty and character limit 1000


    # optional chatgpt told to ,i dont know
    def __repr__(self):
        return f"<Note {self.title}>"
        # Helps while debugging (optional)








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



#testing
# writing a function to create entries in the database

@app.route("/add-notes")
def addnote():
    

    new_note=Note(  # Here Note is the name of the table in teh database
        #new_note is the variable to store the data temporarily
        #title and content is the column names
        title="hi  I am title 2",
        content="Hi I am content 2"
    )



@app.route("/view-notes")
def viewnote():
    all_notes=Note.query.all() #fetches all rows from the table Note

    return render_template("view-notes.html",notes=all_notes) #passess all the data in the variable  notes





    db.session.add(new_note)
    #this adds the note for staging but it is still not commited yet

    #now for commit
    db.session.commit()
    #data commited and got written in the database

    return "Note added successfully"


if __name__ == "__main__":
    # This checks: "Is this file run directly?"
    # It prevents the server from starting if imported elsewhere

    with app.app_context():
        db.create_all()
    

    app.run(debug=True)
       # Starts the Flask development server
       # debug=True → auto-restart + detailed error messages