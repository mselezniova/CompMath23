import math as m


def normal_form(z, n):
    # To find relatively prime nominator and denominator,
    # we find the greatest common divisor (gcd) of z and n 
    # and divide both numbers by the gcd.
    gcd = m.gcd(z, n)
    return (z//gcd, n//gcd)

# Class Rational, the argument (object) is optional
class Rational(object):
    '''Rational numbers class'''
    
    # Initialization of a class instance function __init__.
    # This function runs when a class instance is created.
    def __init__(self, z, n):
        # We save a rational number as nominator z and denominator n
        self.z, self.n = normal_form(z, n)
        
    # The string representation function __repr__.
    # This function is called when we use print() on the object
    # and must return a string value to be printed.
    def __repr__(self):
        # If the number is integer (denominator equals 1), we simply ptint the number as integer.
        # Otherwise, we print the rational number in the form "z/n".
        if self.n == 1:
            return str(self.z)
        else:
            return str(self.z) + '/' + str(self.n)
    
    # Addition function __add__.
    # This function defines how operation "+" works for the class instances.
    def __add__(self, other):
        return Rational(self.z*other.n + other.z*self.n, self.n*other.n)
    
    # Multiplication from the right __rmul__. 
    # This function is called when an instance of Rational is 
    # multiplied with a data type that does not support multiplication by Rational.
    def __rmul__(self,other):
        # Here we define multiplication of Rational with type 'int'.
        return Rational(self.z*other, self.n)
    
    # Multiplication function __mul__. 
    # This function defines how operation "*" works for the class instances.
    def __mul__(self,other):
        # We differentiate multiplication with 'int' and with 'Rational'
        if isinstance(other, int): # isinstance checks is the second argument is an instance of int
            # for multiplication with int, we use __rmul__
            return Rational.__rmul__(self, other)
        else:
            return Rational(self.z*other.z, self.n*other.n)
    
    # Subtraction function __sub__.
    # This function defines how operation "-" works for the class instances.
    def __sub__(self, other):
        # We represent subtraction as addition with multiplication by -1
        return self + (-1)*other
    
    # Conversion to floation point function __float__.
    # This function is called when we use float() on the object.
    def __float__(self):
        return self.z/self.n
    
    # "Less than" function __lt__.
    # This function defines how operation "<" works for the class instances.
    def __lt__(self, other):
        # We compute the difference of two retional numbers
        # and check whether it is smaller than 0.
        diff = self - other
        if diff.z < 0:
            return True
        else:
            return False
        


# Idiom "if __name__=='__main__'" ensures that the following code
# is executed only if the file is run as a script (and not imported as a module)
if __name__=='__main__':

    # Test of the implented methods.

    one_half = Rational(1,2)
    one_third = Rational(1,3)
    one_fifth = Rational(1,5)
    one_sixth = Rational(1,6)

    #a)
    print(normal_form(3,2), normal_form(15, 3), normal_form(20, 42))
    #d)
    print(f"{one_half} + {one_third} + {one_sixth} = {one_half + one_third + one_sixth}")
    #e)
    print(f"{one_half} * {2} = {one_half*2}")
    print(f"{one_half} + {(-1)}*{one_half} = {one_half + (-1)*one_half}")
    #f)        
    print(f"{one_third} * {Rational(15,2)} * {Rational(2,5)} = {one_third*Rational(15,2)*Rational(2,5)}")
    #g)
    print(f"{one_half} - {one_half} = {one_half - one_half}")
    #h)
    print(f"float({one_half}) = {float(one_half)}, float({one_third}) = {float(one_third)}, float({Rational(1,11)}) = {float(Rational(1,11))}")
    #i)
    ls = [Rational(n//2,n) for n in range(2,12)]

    # sorted() uses the __lt__ function internally
    print(sorted(ls))

    












