import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds211088.mlab.com:11088/c4e_todo

host = "ds211088.mlab.com"
port = 11088
db_name = "c4e_todo"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())