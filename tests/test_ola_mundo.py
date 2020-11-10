"""Um pequeno exemplo com teste de unidade.

Para demonstrar como fazer um teste de unidade.

"""
from unittest import TestCase

from saudacao.ola_mundo import OlaMundo


class OlaMundoTestSuite(TestCase):

    def test_ola_mundo(self):
        """
        Testando o construtor e o str
        """
        ola = OlaMundo('ifsc')

        self.assertEqual('Mensagem: ifsc', str(ola), "Strings diferentes")
