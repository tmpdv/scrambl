from fastapi import FastAPI, Body, HTTPException
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
    res: str = key.get('sp').data
    arr = list()
    for s in text:
        enc = key.get(str(ord(s)))
        if enc is None:
            raise HTTPException(status_code=404, detail="Symbol '" + s + "' is not supported")
        arr.append(enc.data)
    return res.join(arr)


@app.get("/decrypt")
async def decrypt(text: str = Body()):
    res: str = ''
    for s in text.split(key.get('sp').data):
        letter = rev.get(s)
        if letter is None:
            raise HTTPException(status_code=404, detail="Invalid string")
        res += chr(int(letter))
    return res


