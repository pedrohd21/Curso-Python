import re

class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        self._valida_ip(valor)
        return self._ip

    @mascara.setter
    def mascara(self, valor):
        self._mascara = valor

    @prefixo.setter
    def prefixo(self, valor):
        self._prefixo = valor

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        print(regexp.search(ip), '12')

