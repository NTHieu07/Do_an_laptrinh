from libs.Dataconnector import DataConnector

emp = DataConnector().get_all_employees()
for e in emp:
    print(e)