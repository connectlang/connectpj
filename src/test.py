# server.py
from index import FlaskFunctionRouter

class MyService:
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, a, b, c):
        return a + b + c

router = FlaskFunctionRouter(MyService())
router.run(port=5000)
