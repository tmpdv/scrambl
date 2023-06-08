from fastapi import FastAPI, Body
from jproperties import Properties

key = Properties()
rev = dict()

with open('use.key.properties', 'rb') as file:
    key.load(file)

for k in key:
    rev[key.get(k).data] = k


app = FastAPI()


@app.get("/encrypt")
async def encrypt(text: str = Body()):
    res: str = key.get('0').data
    arr = list()
    for s in text:
        arr.append(key.get(str(ord(s))).data)
    res = res.join(arr)
    return res


@app.get("/decrypt")
async def decrypt(text: str = Body()):
    res: str = ''
    for s in text.split(key.get('0').data):
        res += chr(int(rev.get(s)))
    return res


