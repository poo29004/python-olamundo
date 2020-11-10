class OlaMundo:
    def __init__(self, mensagem):
        """
        Iniciando atributos da classe
        """
        self.mensagem = mensagem

    def __str__(self):
        """
        String que será retornada
        """
        return f'Mensagem: {self.mensagem}'