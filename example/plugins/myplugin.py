from example import MyBaseClass


class MyPlugin(MyBaseClass):
    def __init__(self):
        super(MyPlugin, self).__init__()
        self.name = "My Plugin"

    def run(self):
        print("My Plugin is running")
    
