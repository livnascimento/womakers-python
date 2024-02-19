from uuid import UUID,uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),name="Ana Sousa", email="ana.sousa@email.com", password="123456", role=Role.roles[1]),
    User(id=uuid4(),name="Joana Silva", email="joana.silva@email.com", password="123456", role=Role.roles[0]),
    User(id=uuid4(),name="Cassia Pereira", email="cassia.pereira@email.com", password="123456", role=Role.roles[0]),
]

@app.get("/api/user")
async def get_users():
    return db

@app.get("/api/user/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(
        status_code = 404,
        detail = "Usuário não encontrado."
    )
        
@app.post("/api/user")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}
    
@app.delete("/api/user/{id}")
async def delete_user(id: UUID):
    for user in db:
        if (user.id == id):
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = "Usuário não encontrado."
    )


@app.put("/api/user/{id}")
async def update_user(id: UUID, name, email, password, role):
    for user in db:
        if (user.id == id):
            user.name = name
            user.email = email
            user.password = password
            user.role = role
            return user
    raise HTTPException(
        status_code = 404,
        detail = "Usuário não encontrado."
    )
