from unittest import TestCase
from logicofthestring import get_string_length

class string_length(TestCase): 

    def test_that_length_is_equal(self):
        result= get_string_length("wisdom", 6)
        self.assertTrue(result)

    def test_that_length_is_not_equal(self):
        result= get_string_length("wisdom", 6)
        self.assertFalse(result)
