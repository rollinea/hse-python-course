class Complex:

    def __init__(self, re, im):
        self._re = re
        self._im = im

    def __eq__(self, other):
        return (self._re == other._re) and (self._im == other._im)

    def __str__(self):
        if self._re == 0:
            if self._im == 0:
                return '0'
            elif self._im == 1:
                return 'i'
            else:
                return f'{self._im}i'
        else:
            if self._im == 0:
                return f'{self._re}'
            elif self._im == 1:
                return f'{self._re} + i'
            elif self._im < 0:
                return f'{self._re} - {-self._im}i'
            else:
                return f'{self._re} + {self._im}i'

    def add(self, other):

        re_sum = self._re + other._re
        im_sum = self._im + other._im

        return Complex(re_sum, im_sum)

    def subtract(self, other):

        re_sub = self._re - other._re
        im_sub = self._im - other._im

        return Complex(re_sub, im_sub)

    def multiply(self, other):

        re_mul = self._re * other._re - self._im * other._im
        im_mul = self._im * other._re + self._re * other._im

        return Complex(re_mul, im_mul)

    def divide(self, other):

        if (other._re == 0) and (other._im == 0):
            return 'Divide by zero!'
        else:
            re_nom = self._re * other._re - self._im * (-other._im)
            im_nom = self._im * other._re + self._re * (-other._im)
            re_denom = other._re * other._re - other._im * (-other._im)

            ans_re = re_nom / re_denom
            ans_im = im_nom / re_denom

            return Complex(ans_re, ans_im)

    def length(self):
        return (self._re ** 2 + self._im ** 2) ** (1 / 2)