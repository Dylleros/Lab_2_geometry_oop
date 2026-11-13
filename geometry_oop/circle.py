from shape2d import Shape2D
import numpy as np

class Circle(Shape2D):
    def __init__(self, radius: float | int, x: float| int = 0, y: float | int = 0) -> None:
        super().__init__(x,y)
        self.radius = radius

    @property
    def radius(self) -> float | int:
        return self._radius

    @radius.setter
    def radius(self, value: float | int ) -> None:
        if not isinstance(value,(float, int)):
            raise TypeError(f"Radius has to be int or float not {type(value)}")

        if not 0 < value:
            raise ValueError(f"Radius must be higher than zero not {value}")
        
        self._radius = value

    @property
    def area(self) -> float:
        return np.pi*self.radius**2

    @property
    def perimeter(self) -> float:
        return 2*np.pi*self.radius

    def is_unit_circle(self) -> bool:
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def __str__(self) -> str:
        return f"Circle centered at {self.x, self.y} with radius {self.radius}"

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"
        
        

    
        
        

        

        
    
         
    
