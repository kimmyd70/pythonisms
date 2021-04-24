from pythonisms import __version__
import pytest
from pythonisms.pythonisms import  Print, Printcount, generic_arguments

# passes -- proof of life with poetry new
@pytest.mark.skip('Passed On Previous Run')
def test_version():
    assert __version__ == '0.1.0'

# 2 passes -- iterator/generator tests
@pytest.mark.skip('Passed On Previous Run')
def test_print_count():
    result = []
    for i in Print(3):
        result.append(i)
    
    expected = [1,2,3]
    assert result == expected

@pytest.mark.skip('Passed On Previous Run')    
def test_print_odds():
    result = []
    for i in Printcount(8):
        result.append(i)
    expected = [1,3,5,7]
    assert result == expected
        
    

    
# passes -- *args with different types and .join()
# @pytest.mark.skip('Passed On Previous Run')
def test_args():
    a = 'Aliya'
    b = ['is', 'awesome']
    c = ('!', )
    
    actual = generic_arguments(*a, *b, *c)
    expected = 'A l i y a is awesome !'
    assert actual == expected