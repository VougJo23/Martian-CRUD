from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# use in-memory SQLite database 
# data is lost when app stops
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    print("id= ", id,"name= ", name,"quantity= ", quantity)

# Create database tables
with app.app_context():
    db.create_all()

# Create a new resource (POST)
@app.route('/resources', methods=['POST'])
def add_resource():
    data = request.json
    new_resource = Resource(name=data['name'], quantity=data['quantity'])
    db.session.add(new_resource)
    db.session.commit()
    return jsonify({"message": "Resource added"}), 201


# Read all resources (GET)
@app.route('/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{"id": r.id, "name": r.name, "quantity": r.quantity} for r in resources])


#Read one resource (GET)
@app.route('/resources/<int:id>', methods=['GET'])
def get_resource(id):
    resource = Resource.query.get(id)  # Find resource by ID
    if resource:
        return jsonify({"id": resource.id, "name": resource.name, "quantity": resource.quantity}), 200
    else:
        return jsonify({"message": "Resource not found"}), 404
    

# Update a resource (PUT)
@app.route('/resources/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.json
    resource = Resource.query.get(id)
    if resource:
        resource.name = data.get('name', resource.name)
        resource.quantity = data.get('quantity', resource.quantity)
        db.session.commit()
        return jsonify({"message": "Resource updated"})
    return jsonify({"error": "Resource not found"}), 404


#Delete all resources (DELETE)
@app.route('/resources', methods=['DELETE'])
def delete_resources():
    resources = Resource.query.get()
    for r in resources:
        db.session.delete(resources)
        db.session.commit()
    return jsonify({"message": "All resources deleted"})


# Delete a resource (DELETE)
@app.route('/resources/<int:id>', methods=['DELETE'])
def delete_resource(id):
    resource = Resource.query.get(id)
    if resource:
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"message": "Resource deleted"})
    return jsonify({"error": "Resource not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)

#test API: 
#curl -X POST http://127.0.0.1:5000/resources -H "Content-Type: application/json" -d "{\"name\": \"Oxygen Tanks\", \"quantity\": 50}"
#curl -X POST http://127.0.0.1:5000/resources -H "Content-Type: application/json" -d "{\"name\": \"CO2 Tanks\", \"quantity\": 10}"
#curl -X GET http://127.0.0.1:5000/resources
#curl -X PUT http://127.0.0.1:5000/resources/2 -H "Content-Type: application/json" -d "{\"name\": \"CO2 Tanks\", \"quantity\": 30}"
#curl -X DELETE http://127.0.0.1:5000/resources/1
