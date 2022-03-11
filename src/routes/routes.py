from src.controllers.controller import *

routes = {
    "hello_route": "/", 
    "Hello_controller": HelloController.as_view('hello')
}