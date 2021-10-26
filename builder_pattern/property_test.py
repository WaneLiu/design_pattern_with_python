class Student(object):
    __slots__ = ('__name', '__age', '__score')

    def __init__(self, name, age, score = 0):
        self.__name = name
        self.__age = age
        self.__score = score


    @property
    def score(self):
        return self.__score


    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be Int')
        if score < 0 and score > 100:
            raise ValueError('Score range must between 0-100')
        self.__score = score

std = Student('WaneLiu', '16', '99')
print(std.score)
std.score = 100
print(std.score)