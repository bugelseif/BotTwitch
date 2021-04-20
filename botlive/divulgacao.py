from configparser import ConfigParser


class Divulgation:
    def __init__(self, filename):
        self.filename = filename
        self.reload()

    def reload(self):
        self.arquivo = ConfigParser()
        self.arquivo.read(self.filename)

    def get_message(self, chave, default=None):
        return self.arquivo.get('mensagem', chave, fallback=default)
