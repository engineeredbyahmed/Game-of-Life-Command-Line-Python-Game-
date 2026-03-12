class Style:
    """
    This class containts all text styles 
    that I used in my main game loop.
    All other cards inherit from the base class. 

     Methods:
    @staticmethod   

    The reason for this design choice:

    (1) to call the method of the class without
    creating an instance of the class 
    
    """
    #Colors
    Black = "\x1b[30m"
    Red = "\x1b[31m"
    Green = "\x1b[32m"
    Yellow = "\x1b[33m"
    Blue = "\x1b[34m"
    Magenta = "\x1b[35m"
    Cyan = "\x1b[36m"


    #Background
    B_Black = "\x1b[40m"
    B_Red = "\x1b[41m"
    B_Green = "\x1b[42m"
    B_White = "\x1b[47m"
    B_magenta = "\x1b[45m"
    B_blue = "\x1b[44m"

    #Effects
    BOLD = "\033[1m"
    Underline = "\033[4m"

    Reset = "\033[0m"
    


    @staticmethod
    def color_text(text, color):
        return color + text + Style.Reset
    

    


