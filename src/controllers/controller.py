from flask.views import MethodView

class HelloController(MethodView):
    
    def get(self):
        return "Hello world"