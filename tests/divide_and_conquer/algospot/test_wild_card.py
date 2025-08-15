from divide_and_conquer.algospot.wild_card import match


def test_wildcard_empty():
    assert match('', 'hello') == False

def test_exact_match():
    assert match('hello', 'hello') == True
    assert match('helloworld', 'helloworld') == True

def test_question_mark():
    assert match('hel?o', 'hello') == True
    assert match('hel?', 'hell') == True
    assert match('hel?', 'helll') == False

def test_asterisk():
    assert match('hel*o', 'hello') == True
    assert match('hel*o', 'helllo') == True
    assert match('hel*o', 'helo') == True
    assert match('*', 'asdlfkjasdlkfjsadlkf') == True
    assert match('**', 'asdlfkjasdlkfjsadlkf') == True
    assert match('*h*', 'aaaaaaahbbbbbb') == True
    assert match('*h', 'hhhhb') == False
    assert match('h*', 'bbbbbbbh') == False
    assert match('habc*', 'habc') == True
    assert match('*a*a*a', 'aaa') == True