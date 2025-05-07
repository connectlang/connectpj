from flask import Flask, request, jsonify

class FlaskFunctionRouter:
    def __init__(self, service_instance):
        self.app = Flask(__name__)
        self.service = service_instance
        self.register_routes()

    def register_routes(self):
        @self.app.route('/call/<method_name>', methods=['POST'])
        def call_method(method_name):
            data = request.json or {}
            try:
                method = getattr(self.service, method_name)
                if callable(method):
                    result = method(**data)
                    return jsonify({ "result": result })
                else:
                    return jsonify({ "error": "Not callable" }), 400
            except AttributeError:
                return jsonify({ "error": "Method not found" }), 404
            except Exception as e:
                return jsonify({ "error": str(e) }), 500

    def run(self, **kwargs):
        self.app.run(**kwargs)
