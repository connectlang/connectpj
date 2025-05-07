# server.py
from src import 

class MyService:
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, a, b):
        return a + b

router = FlaskFunctionRouter(MyService())
router.run(port=5000)
