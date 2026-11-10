from shape2d import Shape2D
from pytest import raises

def test_valid_init():
    s = Shape2D(-2,4.5)
    assert s.x == -2
    assert s.y == 4.5
    
def test_default_init():
    s = Shape2D()
    assert s.x == 0
    assert s.y == 0

def test_invalid_init():
    with raises(TypeError):
        Shape2D(2, "4")

    with raises(TypeError):
        Shape2D("2", 4)

def test_valid_setters():
    s = Shape2D(-2, 4.5)
    s.x = 2
    s.y = 5
    assert s.x == 2
    assert s.y == 5

def test_invalid_setters():
    s = Shape2D(-2, 4.5)

    with raises(TypeError):
        s.x = "2"
    assert s.x == -2

    with raises(TypeError):
        s.y = "4,5"
    assert s.y == 4.5

def test_translate():
    s = Shape2D(2, 4.5)
    s.translate(3, -1.5)
    assert s.x == 5
    assert s.y == 3

def test_invalid_translate():
    s = Shape2D(5,3)
   
    with raises(TypeError):
         s.translate("4", 2)
    assert s.x == 5
    assert s.y == 3

    with raises(TypeError):
         s.translate(4, "2")
    assert s.x == 5
    assert s.y == 3
    

    

