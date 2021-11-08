
from Calc import Calc
from unittest import TestCase
class TestCalc(TestCase):
#加法
    def testAdd1(self):
        #
        a = 6
        b = 5
        s = 11

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(s,sum)

#减法
    def testminus(self):

        a = 5
        b = 6
        c = -1

        calc = Calc()
        sum = calc.minus(a,b)

        self.assertEqual(c,sum)

#乘法
    def testmulti(self):

        a = 9
        b = 9
        c = 81

        calc = Calc()
        sum = calc.multi(a,b)

        self.assertEqual(c,sum)

#除法
    def testdevision(self):

        a = 9
        b = 3
        c = 3
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)