from data import create_order_body

import sender_stand_request

# Функция для позитивной проверки
def positive_assert(body):
    track = str(sender_stand_request.post_new_order(body).json()['track'])
    order_response = sender_stand_request.get_order_data(track)
    assert order_response.status_code == 200

def test_create_order_and_get_order_data_success_response():
    positive_assert(create_order_body)

# Александр Майоров, 8-а когорта — Финальный проект. Инженер по тестированию плюс