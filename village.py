class Village:
    def __init__(self, x, y, time):
        self.__x = x
        self.__y = y
        self.__time = time

    @property
    def x(self):
        return self.__x

    @x.setter
    def age(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def age(self, y):
        self.__y = y

    @property
    def time(self):
        return self.__time

    @time.setter
    def age(self, time):
        self.__time = time

    def __str__(self):
        return "({}|{}) - {}".format(self.x, self.y, self.time)
