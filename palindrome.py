import unittest

def palindrome(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")  
    if palabra == palabra[::-1]:  
        return True
    else:
        return False


class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_simple2(self):
        result = palindrome('ana')
        self.assertEqual(result, True)

    def test_palindrome_simple3(self):
        result = palindrome('aba')
        self.assertEqual(result, True)

    def test_palindrome_simple4(self):
        result = palindrome('anana')
        self.assertEqual(result, True)

    def test_palindrome_simple5(self):
        result = palindrome('ojo')
        self.assertEqual(result, True)

    def test_palindrome_simple6(self):
        result = palindrome('asdfghjklkjhgfdsa')
        self.assertEqual(result, True)

    def test_palindrome_simple7(self):
        result = palindrome('luz azul')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()


