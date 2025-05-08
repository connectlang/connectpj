# server.py
from index import FlaskFunctionRouter
from pydantic import BaseModel, ValidationError

class AddModel(BaseModel):
    name: str
    age: int

class UserService:
    def process_user(self, name: str, age: int) -> dict:
        is_adult = age >= 18
        welcome_message = f"Welcome, {name}!"
        return {
            "message": welcome_message,
            "isAdult": is_adult,
            "originalAge": age
        }

def valid_user(data):
    try:
        umodel = AddModel(**data)
        return umodel.model_dump()
    
    except ValidationError as e:
        raise ValueError(str(e))
    
valids = {
    'process_user': valid_user,
}

router = FlaskFunctionRouter(UserService(), valids)
router.run(port=5500)
