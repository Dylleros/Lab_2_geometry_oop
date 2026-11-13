from shape2d import Shape2D

class Rectangle(Shape2D):
    def __init__(self, width: float | int, height: float | int, x: float | int = 0, y: float | int = 0) -> None:
        super().__init__(x,y)
        self.width = width
        self.height = height

    @property
    def width(self) -> float | int:
        return self._width

    @width.setter
    def width(self, value: float | int) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f" Width has to be int or float not {type(value)}")    

        if not 0 < value:
            raise ValueError(f"Width has to be higher than zero not {value}")

        self._width = value

    @property
    def height(self) -> float | int:
        return self._height

    @height.setter
    def height(self, value: float | int) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"Height has to be int or float not {type(value)}")    
        
        if not 0 < value:
            raise ValueError(f"Height has to be higher than zero not {value}")
            
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return self.width*2 + self.height*2

    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def __str__(self) -> str:
        return f"Rectangle centered at {self.x, self.y} with width {self.width} and height {self.height}"

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

