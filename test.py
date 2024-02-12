# Акопян Аркадий, 13 когорта, Марс. Финальный проект. Инженер по тестированию плюс.
import sender_stand

def test_status_code():
    assert sender_stand.response_order.status_code == 200
