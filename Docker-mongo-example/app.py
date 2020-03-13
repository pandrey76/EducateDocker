from uuid import uuid4
import importlib
module_name = 'storage'
my_module = importlib.import_module(module_name)

# Создаётся объект класса MongodbService,
# у этого класса есть всего два метода get_data, save_data.
# Почему, то данный код не работает
# storage1 = my_module.MongodbService.get_instance()


storage1 = my_module.MongodbService()

#  В цикле записываются 5 объектов, объекты простые у них есть два поля.
# Туда записывается UUID версии 4.
for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "payload": str(uuid4())
    }
    storage1.save_data(dto)

# Выводится вся информация, которая там есть
for data in storage1.get_data():
    print(data)
