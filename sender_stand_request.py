import configuration
import requests
import data

#Функция на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

def get_order_data(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER + track)

