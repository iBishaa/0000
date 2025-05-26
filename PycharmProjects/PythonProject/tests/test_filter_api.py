from fastapi.testclient import TestClient
from backend.app import app
from config import ROOM_ID

client = TestClient(app)

def test_filter_api_stub():
    # Тест для заглушки (без C++-фільтра)
    payload = {
        "image_data": [0, 0, 0, 255],  # Чорний піксель (R, G, B, A)
        "filter_name": "blur",
        "width": 1,
        "height": 1
    }
    res = client.post(f"/filter/{ROOM_ID}", json=payload)
    assert res.status_code == 200
    assert res.json()["image_data"] == [0, 0, 0, 255]  # Заглушка повертає ті самі дані

def test_filter_invert_real():
    # Тест для реального фільтра (інверсія через C++)
    payload = {
        "image_data": [0, 0, 0, 255],  # Чорний піксель
        "filter_name": "invert",
        "width": 1,
        "height": 1
    }
    res = client.post(f"/filter/{ROOM_ID}", json=payload)
    assert res.status_code == 200
    # Перевірка, що піксель інвертувався: чорний → білий (255, 255, 255, 255)
    assert res.json()["image_data"] == [255, 255, 255, 255]