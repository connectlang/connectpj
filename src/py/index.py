from flask import Flask, request, jsonify

class FlaskFunctionRouter:
    def __init__(self, service_instance, validators=None):
        self.app = Flask(__name__)
        self.service = service_instance
        self.validators = validators or {}
        self.register_routes()

    def register_routes(self):
        @self.app.route('/call/<method_name>', methods=['POST'])
        def call_method(method_name):
            data = request.json or {}
            
            # 사용자가 정의한 유효성 검사 함수가 있으면 실행
            if method_name in self.validators:
                try:
                    data = self.validators[method_name](data)
                except ValueError as ve:
                    return jsonify({"error": str(ve)}), 400

            # 서비스 클래스 메서드 호출
            try:
                method = getattr(self.service, method_name)
                if callable(method):
                    result = method(**data)  # 데이터는 이미 유효성 검사를 거친 후
                    return jsonify({"result": result})
                else:
                    return jsonify({"error": "Not callable"}), 400
            except AttributeError:
                return jsonify({"error": "Method not found"}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/ping')
        def ping():
            return jsonify({ "status": "ok" })

    def run(self, **kwargs):
        self.app.run(**kwargs)
