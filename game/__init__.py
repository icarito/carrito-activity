import spyral
import carrito 

def main(activity=None):
    spyral.director.push(carrito.Juego(activity))
