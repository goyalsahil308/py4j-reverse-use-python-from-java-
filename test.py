from operator import mod
from tkinter.messagebox import RETRY


class SimpleHello(object):

    def sayHello(self, int_value, string_value):
        result= f"Said hello to {string_value}  {int_value}"
        return result
    def plus(self,i,j):
        return i+j
    def minus(self,i,j):
        return (i-j)
    def multi(self,i,j):
        return(i*j)
    class Java:
        implements = ["py4j.IHello"]

# Make sure that the python code is started first.
# Then execute: java -cp py4j.jar py4j.examples.SingleThreadClientApplication
from py4j.java_gateway import JavaGateway, CallbackServerParameters
simple_hello = SimpleHello()
gateway = JavaGateway(
    callback_server_parameters=CallbackServerParameters(),
    python_server_entry_point=simple_hello)