import unittest

class Testshoppingcart(unittest.TestCase):
    def setup(self):
        self.cart = shoppingcart()
        self.cart1 = cartitem('apel', 3400)
        self.cart2 = cartitem('jeruk', 2100)

    def test_tambah_barang(self):
        self.cart.tambah_barang(self.cart1)
        self.assertEqual(len(self.cart1, 1))

        self.cart.tambah_barang(self.cart2)
        self.assertEqual(len(self.cart1, 2))

    def test_hapus_barang(self):
        self.cart.tambah_barang(self.cart1)
        self.cart.tambah_barang(self.cart2)
        self.cart.hapus_barang('apel')
        self.assertEqual(len(self.cart1, 0))

    def test_total_belanja(self):
        self.cart.tambah_barang(self.cart1)
        self.cart.tambah_barang(self.cart2)
        total = self.cart.total_belanja()
        self.assertEqual(total, 5500)

unittest.main(argv=[''], verbosity=2, exit=False) 