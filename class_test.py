class New_Class:

    focus = 10.4
    def __init__(self, focus: int) -> None:
        self.focus = focus
    
    @classmethod
    def class_test(cls, error):

        return cls.focus + error
    
    @staticmethod
    def class_static(value):
        return value*12
    
