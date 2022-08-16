'''
關於enum跟class

'''

import enum


# 定義一個class
class NewClass():
    New1 = 'track'


# 定義一個Enum型態的class
class EnumClass(enum.Enum):
    Attr1 = 'alpha'
    Attr2 = 'betta'
    Attr3 = 'gamma'


class School:
    def __init__(self, peopleNum: int, nClass: EnumClass):
        self.peopleNum = peopleNum
        self.nClass = nClass

    def display(self):
        print(self.peopleNum)
        print(self.nClass.name)
        print(self.nClass.value)


def useClass(lst, num: int):
    for e in lst:
        if e.peopleNum == num:
            return e


class1 = str(input('Enter(Attr1, Attr2, Attr3):'))
S1 = School(50, EnumClass[class1])
S1.display()
print('\n')
for i in EnumClass:
    print(i.value)
print('\n')


searchNum = int(input('Enter (10, 20, 30):'))
lst1 = [School(10, EnumClass['Attr1']), School(20, EnumClass['Attr2']), School(30, EnumClass['Attr3'])]
op = useClass(lst1, searchNum)
print('number of people ' + str(op.peopleNum))
print(op.nClass.name)
print(op.nClass.value)


