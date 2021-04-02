class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    
    def do_work(self):
        if self.occupation == "tennis":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a movie")
    
    def speaks(self):
        print(self.name, "says how are you")

tom = Human("tom", "actor")
tom.do_work()
tom.speaks()
