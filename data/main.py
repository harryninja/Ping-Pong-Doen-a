

from .control import Control
'''isso aqui é como uma corrente que vai puxar cada um modulo do codigo começando pelo controle do software exemplo Tela'''
def main(fullscreen, difficulty, size):
    app = Control(fullscreen, difficulty, size)
    app.run()
