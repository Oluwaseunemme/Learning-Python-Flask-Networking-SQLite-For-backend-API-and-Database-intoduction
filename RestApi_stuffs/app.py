from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

app= Flask(__name__) #main flask app creation with current python app context name passed
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data.db" #sqlite domain which is local on my pc
db=SQLAlchemy(app) #database object creation with app obj context passed

#print(f"Instance folder path {app.instance_path}")
class Color(db.Model): #color class so we could create and add as much unique types of color to our database with individual name and descriptions.
    id= db.Column(db.Integer, primary_key=True)#the id of each added object to the data base will be automatically incremented and assigned?
    name= db.Column(db.String(80), nullable=False)#i will be the one to pass the name when i create individual object
    description= db.Column(db.String(120)) #i will also be the one to pass the 

    def __repr__(self): 
        return f"{self.name}-{self.description}"

"""with app.app_context():
    db.create_all()
    print("DB created............")
    if Color.query.count() == 0:#we only need data object creation and commit once at first run 
        db.session.add_all([
            Color(name="Green", description="Nature's favourite"),
            Color(name="Blue", description="Sky is blue"),
            Color(name="Red", description="Blood is red"),
        ])
        db.session.commit()"""

@app.route('/colors')#route for coolor services
def getColors():#color route function that gets called when we client call get color endpoint
    
    colors= Color.query.all()
    colors=[{"name":x.name, "description":x.description} for x in colors]
    return {"Data":colors}

@app.route('/colors/<int:id>')#route for getting specified data with it id
def getColor(id):
    color=Color.query.get_or_404(id)
    return {"name":color.name, "description":color.description}

@app.route('/colors', method=["POST"])
def postData():
    data=Color(name=requests.json['name'], description=requests.json['description'])
    db.session.add(data)
    db.session.commit()
    return {"id":data.id}

@app.route('/colors/<int:id>', method=["DELETE"])
def deleteData(id):
    colors=Color.query.get(id)
    if colors is None:
        return{"error":"invalid id input"}
    db.session.delete(colors)
    db.session.commit()
    return {"deleted":id}

@app.route('/food')
def getFood():
    return {
            "food1":"Bread",
            "food2":"Rice"
            }

@app.route('/users/<int:user_id>')
def getUser(user_id):
    return {
        "user_id": user_id
    }

#run flask --app app run
#browser http://127.0.0.1:5000/colors