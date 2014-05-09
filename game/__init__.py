import spyral
import neko

def main(activity=None):
    spyral.director.push(neko.Juego(activity))
