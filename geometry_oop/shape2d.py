class Shape2D:
    
    def __init__(self, x: float | int = 0, y: float | int = 0) -> None:
        self.x = x
        self.y = y

    
    @property
    def x(self) -> float | int:
        return self._x


    @x.setter
    def x(self, value: float | int) -> None:
        self._validate_xy(value)
        self._x = value


    @property
    def y(self) -> float | int:
        return self._y


    @y.setter
    def y(self, value: float | int) -> None:
        self._validate_xy(value)
        self._y = value


    def _validate_xy(self,  value: float | int) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Coordinates must be int or float not {type(value).__name__}")


    def translate(self, move_x: int | float, move_y: int | float) -> None:
        
        self._validate_xy(move_x)
        self._validate_xy(move_y)

        new_x = self.x + move_x
        new_y = self.y + move_y

        self.x = new_x
        self.y = new_y


