from app import app

def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert "Smart Inventory API is running!" in res.get_json()["message"]

def test_add_item():
    client = app.test_client()
    item = {"ProductID": "P002", "ProductName": "Wire Coil", "Stock": 20}
    res = client.post("/add", json=item)  # ? use POST instead of GET
    assert res.status_code == 200
    assert res.get_json()["success"] is True
