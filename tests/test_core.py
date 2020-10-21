'''
test for the core.py file

'''

import unittest             # prima i pacchetti std_in, poi gli altri, poi dopo una riga i miei pacchetti

from smartsquare.core import square
#export PYTHONPATH=/Users/andrea/Desktop/computing_methods/smartsquare/  per farlo funzionare...


class TestCore(unittest.TestCase):      # classes con CamelCase
    ''' Unittest for core module '''
    def test_float(self):                   # Metodi/Funzioni con '_'
        '''test'''
        self.assertAlmostEqual(square(2.), 4.)

if __name__ == '__main__':
    unittest.main()
