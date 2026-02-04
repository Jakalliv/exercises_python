class Rectangle:
    def __init__(self, width: int, height: int)->None:
        self.height = height
        self.width = width

    def set_width(self, width: int)->None:
        self.width = width

    def set_height(self, height: int)->None:
        self.height = height

    def get_area(self)->int:
        return self.width*self.height
    
    def get_perimeter(self)->int:
        return 2*(self.width+self.height)
    
    def get_diagonal(self)->float:
        return (self.width**2+self.height**2)**0.5
    
    def get_picture(self)->str:
        picture = ""
        for x in range(self.height):
            picture += ("*"*self.width)+"\n"
        
        return picture.strip("\n")



