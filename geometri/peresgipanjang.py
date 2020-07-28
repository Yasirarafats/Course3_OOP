from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):

    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'Modul menghitung luas objek Persegipanjang dengan panjang = {self.p} meter dan lebar = {self.l} meter'

    def hitung_luas(self):
        return self.p * self.l
