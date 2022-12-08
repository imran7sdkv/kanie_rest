from peewee import * 

db = PostgresqlDatabase(
    'hello',
    host = 'localhost',
    port = '5432',
    user = 'wussup',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Cars(BaseModel):
    name = CharField(max_length=255, null = False, unique = True)
    car = CharField(max_length=255)
    year = IntegerField()


class Post(BaseModel):
    author = ForeignKeyField(Cars, on_delete='CASCADE')
    title = CharField()



# db.create_tables((Cars, Post))

# Cars.create(
#     name = 'Imran',
#     car =  'Honda, Lexus, Toyota',
#     year = 2021
# )

Cars.create(
    name = 'Isa',
    car =  'Honda, Lexus, Mercedes',
    year = 2021
)

Cars.create(
    name = 'Nurs',
    car =  'Lada, BMW, mercedes',
    year = 2021
)

Cars.create(
    name = 'Abdulla',
    car =  'Honda, Mercedes',
    year = 2021
)

Cars.create(
    name = 'Aza',
    car =  'Toyota, Lexus, BMW',
    year = 2021
)


db.close()
