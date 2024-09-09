# Sample 
#self -
#Constructor-

class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("Ram :", self.ram)
        print("Processor :", self.processor)

hp=laptop()
Dell=laptop()

hp.ram="8GB"
hp.processor="i7"

Dell.ram="16GB"
Dell.processor="i8"

hp.display()
Dell.display()