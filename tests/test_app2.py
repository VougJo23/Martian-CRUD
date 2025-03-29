import pytest
from src.martian_crud.app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
        yield test_client
        with app.app_context():
            db.drop_all()

def test_add_resource(client):
    with client.application.app_context():
    # Test adding a new resource
        response = client.post('/resources', json={
            'name': 'Test Resource',
            'quantity': 10
    })
    assert response.status_code == 201
    assert response.json == {"message": "Resource added"}

def test_get_resources(client):
    # Add a resource first
    client.post('/resources', json={'name': 'Resource 1', 'quantity': 5})
    client.post('/resources', json={'name': 'Resource 2', 'quantity': 15})

    # Test getting all resources
    response = client.get('/resources')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2
    assert data[0]['name'] == 'Resource 1'
    assert data[1]['quantity'] == 15

def test_get_single_resource(client):
    # Add a resource
    client.post('/resources', json={'name': 'Single Resource', 'quantity': 7})

    # Test getting the resource
    response = client.get('/resources/1')
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "name": "Single Resource",
        "quantity": 7
    }

def test_get_nonexistent_resource(client):
    # Test getting a resource that doesn't exist
    response = client.get('/resources/999')
    assert response.status_code == 404
    assert response.json == {"message": "Resource not found"}

def test_update_resource(client):
    # Add a resource
    client.post('/resources', json={'name': 'Old Name', 'quantity': 3})

    # Test updating the resource
    response = client.put('/resources/1', json={
        'name': 'New Name',
        'quantity': 5
    })
    assert response.status_code == 200
    assert response.json == {"message": "Resource updated"}

    # Verify the update
    response = client.get('/resources/1')
    assert response.json['name'] == 'New Name'
    assert response.json['quantity'] == 5

def test_partial_update_resource(client):
    # Add a resource
    client.post('/resources', json={'name': 'Partial Update', 'quantity': 10})

    # Test updating just the quantity
    response = client.put('/resources/1', json={'quantity': 20})
    assert response.status_code == 200

    # Verify only quantity changed
    response = client.get('/resources/1')
    assert response.json['name'] == 'Partial Update'
    assert response.json['quantity'] == 20

def test_update_nonexistent_resource(client):
    # Test updating a resource that doesn't exist
    response = client.put('/resources/999', json={'name': 'Test'})
    assert response.status_code == 404
    assert response.json == {"error": "Resource not found"}

def test_delete_resource(client):
    # Add a resource
    client.post('/resources', json={'name': 'To Delete', 'quantity': 1})

    # Test deleting the resource
    response = client.delete('/resources/1')
    assert response.status_code == 200
    assert response.json == {"message": "Resource deleted"}

    # Verify it's gone
    response = client.get('/resources/1')
    assert response.status_code == 404

def test_delete_nonexistent_resource(client):
    # Test deleting a resource that doesn't exist
    response = client.delete('/resources/999')
    assert response.status_code == 404
    assert response.json == {"error": "Resource not found"}

def test_delete_all_resources(client):
    # Add some resources
    client.post('/resources', json={'name': 'Resource A', 'quantity': 1})
    client.post('/resources', json={'name': 'Resource B', 'quantity': 2})

    # Test deleting all resources
    response = client.delete('/resources')
    assert response.status_code == 200
    assert response.json == {"message": "All resources deleted"}

    # Verify no resources remain
    response = client.get('/resources')
    assert response.json == []
