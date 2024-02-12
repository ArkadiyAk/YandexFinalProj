import configuration
import requests
import data


# Создаем новый заказ
def creating_order(user_body):
    return requests.post(configuration.URL + configuration.CREATE_USER_ORDER,
                         json=user_body)


# Создаем новый заказ и записываем его трек-номер
def track_number_new_order():
    response_new_order = creating_order(data.user_body)
    track_number = str(response_new_order.json()['track'])
    return track_number


# Получаем набор по трек-номеру заказа
def order_by_track():
    return requests.get(configuration.URL + configuration.GET_ORDER_BY_NUMBER + '?t=' + track_number_new_order())


response_order = order_by_track()
