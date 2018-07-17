class test:
    testCount=0
    def __init__(self,task,answer):
        self.task=task
        self.answer=answer
        test.testCount+=1

    def testCount(self):
        print(test.testCount)

    def display(self):
        print(self.task+self.answer)

task1=test("area of a circle","2*r*r")


task2=test("area of a cylinder"'')

test.display(task1)
