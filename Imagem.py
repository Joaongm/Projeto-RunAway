from time import sleep
import sys
carta = '''
────────────────────────────────────────
─────────────▄▄██████████▄▄─────────────
─────────────▀▀▀───██───▀▀▀─────────────
─────▄██▄───▄▄████████████▄▄───▄██▄─────
───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
──████▄─▄███▀──────────────▀███▄─▄████──
─███▀█████▀▄████▄──────▄████▄▀█████▀███─
─██▀──███▀─██████──────██████─▀███──▀██─
──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
─────███───────────▀▀───────────███─────
─────██████████████████████████████─────
─▄█──▀██──███───██────██───███──██▀──█▄─
─███──███─███───██────██───███▄███──███─
─▀██▄████████───██────██───████████▄██▀─
──▀███▀─▀████───██────██───████▀─▀███▀──
───▀███▄──▀███████────███████▀──▄███▀───
─────▀███────▀▀██████████▀▀▀───███▀─────
───────▀─────▄▄▄───██───▄▄▄──────▀──────
──────────── ▀▀███████████▀▀ ────────────
────────────────────────────────────────'''

quadro = '''
    ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
    ────███───────────────███────
    ───███─────────────────███───
    ──███───▄▀▀▄─────▄▀▀▄───███──
    ─████─▄▀────▀▄─▄▀────▀▄─████─
    ─████──▄████─────████▄──█████
    █████─██▓▓▓██───██▓▓▓██─█████
    █████─██▓█▓██───██▓█▓██─█████
    █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
    ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
    ███─▄▀▀▀▄────███────▄▀▀▀▄─███
    ███──▄▀▄─█──█████──█─▄▀▄──███
    ███─█──█─█──█████──█─█──█─███
    ███─█─▀──█─▄█████▄─█──▀─█─███
    ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
    ████─────────────────────████
    ─███───▀█████████████▀───████
    ─███───────█─────█───────████
    ─████─────█───────█─────█████
    ───███▄──█────█────█──▄█████─
    ─────▀█████▄▄███▄▄█████▀─────
    ──────────█▄─────▄█──────────
    ──────────▄█─────█▄──────────
    ───────▄████─────████▄───────
    ─────▄███████───███████▄─────
    ───▄█████████████████████▄───
    ─▄███▀───███████████───▀███▄─
    ███▀─────███████████─────▀███
    ▌▌▌▌▒▒───███████████───▒▒▐▐▐▐
    ─────▒▒──███████████──▒▒─────
    ──────▒▒─███████████─▒▒──────
    ───────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒───────
    ─────────████░░█████─────────
    ────────█████░░██████────────
    ──────███████░░███████───────
    ─────█████──█░░█──█████──────
    ─────█████──████──█████──────
    ──────████──████──████───────
    ──────████──████──████───────
    ──────████───██───████───────
    ──────████───██───████───────
    ──────████──████──████───────
    ─██────██───████───██─────██─
    ─██───████──████──████────██─
    ─███████████████████████████─
    ─██─────────████──────────██─
    ─██─────────████──────────██─
    ────────────████─────────────
    ─────────────██──────────────'''


class Imagem:
    def __init__(self):
        self.imagem = ''

    def createImageQuadro(self):
        self.imagem = quadro

    def createImagemCarta(self):
        self.imagem = carta

    def animation(self, imagem):
        for c in imagem:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.01)
