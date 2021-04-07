from PySimpleGUI import PySimpleGUI as sg
from pyperclip import paste, copy

try:
    from PIL import Image
except ImportError:
    import Image
from pytesseract import pytesseract as ocr
import os


class Images:

    def __init__(self):
        ocr.tesseract_cmd = r'.\\Tesseract-OCR\\tesseract.exe'

    def Convert_image_to_string(self, fileName):
        try:
            if os.path.isfile(fileName):
                return ocr.image_to_string(Image.open(fileName))
        except Exception:
            return 'Arquivo não encontrado!'


# Layout
class Pega_Texto:
    def __init__(self):
        sg.theme('Reddit')
        self.layout = [
            [sg.Text('Arquivo'), sg.Input(key='caminho', size=(50, 1), do_not_clear=True), sg.Button('Colar')],
            [sg.Text('')],
            [sg.Button('Extrair')],
            [sg.Output(size=(65, 20), key='Extract_text')],
            [sg.Button('Limpar')],  # [sg.Button('Copiar')]
        ]

    # Janela
    def Programa(self):
        janela = sg.Window('Extrair texto de imagem', self.layout)
        Converts = set()
        # Ler Eventos
        while True:
            eventos, valores = janela.Read()
            if eventos == sg.WINDOW_CLOSED:
                break
            janela.find_element('Extract_text').Update('')

            if eventos == 'Extrair':
                try:
                    path = valores['caminho'].replace('\\', '/')
                    print(Images().Convert_image_to_string(path))
                    Converts.add(Images().Convert_image_to_string(path))

                except Exception:
                    text = 'Campo arquivo é obrigatorio'
                    print(text)
                    continue

            if eventos == 'limpar':
                janela.find_element('caminho').Update('')
                janela.find_element('Extract_text').Update('')

            if eventos == 'Colar':
                janela.find_element('caminho').Update(paste())

            # if eventos == 'Copiar':
            #     copy(valores['Extract_text'])


if __name__ == '__main__':
    Pega_Texto().Programa()
