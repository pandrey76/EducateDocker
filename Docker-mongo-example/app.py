import time
from uuid import uuid4
from . storage import MongodbService

# Создаётся объект класса MongodbService,
# у этого класса есть всего два метода get_data, save_data.
storage = MongodbService.get_instance()

#  В цикле записываются 5 объектов, объекты простые у них есть два поля.
# Туда записывается UUID версии 4.

for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "payload": str(uuid4())
    }
    storage.save_data(dto)

# Выводится вся информация, кои=торая там есть
for data in storage.get_data():
    print(data)
