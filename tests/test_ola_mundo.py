from olamundo.ola_mundo import OlaMundo
from unittest import TestCase


class OlaMundoTestSuite(TestCase):

    def test_ola_mundo(self):
        """
        Testando o construtor e o str
        """
        ola = OlaMundo('ifsc')

        self.assertEqual('Mensagem: ifsc', str(ola), "Strings diferentes")
