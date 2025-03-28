from Models.Order import Order
from libs.Dataconnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory

orders = DataConnector().get_all_orders()
for order in orders:
    print(order)