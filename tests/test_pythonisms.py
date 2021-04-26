from pythonisms import __version__
import pytest
from pythonisms.pythonisms import  Print, Printcount, generic_arguments
from pythonisms.pythonisms import  printzees, notzees, repeated, info_twice

# passes -- proof of life with poetry new
# @pytest.mark.skip('Passed On Previous Run')
def test_version():
    assert __version__ == '0.1.0'

# 3 passes -- iterator/generator tests
# @pytest.mark.skip('Passed On Previous Run')
def test_print_count():
    result = []
    for i in Print(3):
        result.append(i)
    
    expected = [1,2,3]
    assert result == expected

# @pytest.mark.skip('Passed On Previous Run')    
def test_print_odds():
    result = []
    for i in Printcount(8):
        result.append(i)
    expected = [1,3,5,7]
    assert result == expected
    
# @pytest.mark.skip('Passed On Previous Run')    
def test_info_twice(capsys):
    info_twice()
    assert True
        
# decorators

# 2 passes decorators
# @pytest.mark.skip('Passed On Previous Run')    
def test_printzees():
    actual = printzees()
    expected = 'pizzzzzza pie'
    assert actual == expected
    
# @pytest.mark.skip('Passed On Previous Run')    
def test_print_pie():
    actual = notzees('is not')
    expected = 'pi is not a pie'
    assert actual == expected
    
# 3 passes dunders
# @pytest.mark.skip('Passed On Previous Run')    
def test_affirm():
    actual = Print.__affirm__(Print(3))
    expected = 'You entered 3 as the limit'
    assert actual == expected
    
# @pytest.mark.skip('Passed On Previous Run')    
def test_type():
    user_input = Print(3)
    actual = user_input.__type__()
    expected = 'You entered the integer 3'
    assert actual == expected    

# @pytest.mark.skip('Passed On Previous Run')    
def test_type2():
    user_input = Print(7.5676)
    actual = user_input.__type__()
    expected = 'Ack, we can\'t do 7.5676 iterations'
    assert actual == expected    

    
# passes -- *args with different types and .join()
# @pytest.mark.skip('Passed On Previous Run')
def test_args():
    a = 'Aliya'
    b = ['is', 'awesome']
    c = ('!', )
    
    actual = generic_arguments(*a, *b, *c)
    expected = 'A l i y a is awesome !'
    assert actual == expected