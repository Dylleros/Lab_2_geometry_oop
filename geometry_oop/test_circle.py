from circle import Circle
from pytest import raises

def test_valid_init():
    c = Circle(4, 2, 2)
    assert c.radius == 4
    assert c.x == 2
    assert c.y == 2

def test_default_init():
    c = Circle(2)
    assert c.x == 0
    assert c.y == 0

def test_invalid_init():
    with raises(ValueError):
        Circle(0)

    with raises(TypeError):
        Circle("2")    

def test_valid_setter():
    c = Circle(2)
    c.radius = 4.5
    assert c.radius == 4.5

def test_invalid_setter():
    c = Circle(2)
   
    with raises(TypeError):
        c.radius = "2"
    assert c.radius == (2)

    with raises(ValueError):
        c.radius = 0
    assert c.radius == 2

def is_unit_circle():
    c = Circle(1)
    assert c.is_unit_circle() is True
    
    c.translate(1,0)
    assert c.is_unit_circle() is False

    assert Circle(1,0,1).is_unit_circle() is False
    assert Circle(2).is_unit_circle() is False

def test_eq():
    c = Circle(2,3,4)
    assert (c == Circle(2,4,5)) is True
    assert (c == Circle(3)) is False
    assert (c == "circle") is False 
    
    




