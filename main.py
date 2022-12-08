import requests
from peewee import *
import datetime


db = PostgresqlDatabase(
    'power_db',
    host = 'localhost',
    port = '5432',
    user = 'airan',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Kaniee(BaseModel):
    title = CharField()
    kolvo = IntegerField()
    glas = IntegerField()
    sogl = IntegerField()
    sred_dlina = IntegerField()
    samye_dlinye = CharField()


db.create_tables([Kaniee])

i = 0
sog = 0
gla = 0



while i < 10:
    quete = []
    res = requests.get('https://api.kanye.rest/')

    a = res.json()
    for key, value in a.items():
        if value not in quete:
            quete.append(value)
            i += 1
            for t in value:
                if t in 'qwrtpsdfghjklzxcvbnm':
                    sog += 1
                elif t in 'eyuioa':
                    gla += 1
    
    c = len([i for  i in value if i.isalpha()])
    sred = value.split(' ')
    fg = len(sred)
    avg_word = c/fg

    a = max(sred, key=len)
    sred.remove(a)

    b = max(sred, key=len)
    sred.remove(b)

    c = max(sred, key=len)
    sred.remove(c)
    samiy_dlinniy = a, b, c
          

    Kaniee.create(
        title = quete,
        kolvo = len(value),
        sogl = sog,
        glas = gla,
        sred_dlina = avg_word,
        samye_dlinye = samiy_dlinniy,
    )
    
db.close()