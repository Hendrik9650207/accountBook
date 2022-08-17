# python3
'''
資料結構:
Account :ID, Date, Tag(Cost Type), Money
功能:
檔案存讀、加入帳目、刪除帳目(目前選擇帳目)
查詢帳目(ID、花費區間、Tag) => 清空(clear)、修改(revise)、刪除(delete)
清空選擇帳目
印出所有帳目
印出目前選擇項目
'''

import enum
import sys

'''
# 定義流向型態的類別
class CashFlow(enum.Enum):
    Cost = 'Cost'
    Income = 'Income'
    Transfer = 'Transfer'
'''


# 定義enum 花費型態的類別
class Tag(enum.Enum):
    food = 'Food'
    clothing = 'Clothing'
    housing = 'Housing'
    transportation = 'Transportation'
    recreation = 'Recreation'
    medical = 'Medical'


class Account:
    # constractor
    def __init__(self, Id: int,  Name: str, tag: Tag, expense: int):
        self.Id = Id
        self.Name = Name
        self.tag = tag
        self.expense = expense

    def display(self):
        print('Id: ' + str(self.Id))
        print('Name: ' + self.Name)
        print('Tag: ' + self.tag.value)
        print('Expense: ' + str(self.expense))
        print()

    def reviseName(self, new_name: str):
        self.Name = new_name

    def reviseTag(self, new_tag: Tag):
        self.tag = new_tag

    def reviseExpense(self, new_expense: int):
        self.expense = new_expense


def fCodeDir():
    print()
    print('1: input a new account')
    print('2: display all account')
    print('3: search the account by ID')
    print('4: search the account by expense interval')
    print('5: select the account')
    print('6: revise the account')
    print('7: delete the account')
    print('8: save the record')
    print('9: escape')
    print()


# check account in list exit or not
# 檢查是否有任何account存在
def accExit(acc_List):
    if len(acc_List) == 0:
        return False
    else:
        return True


# acc_list : the element of the list is class Account
# search id and return that element
def searchId(acc_list, goal_id: int):
    # e = Account
    for e in acc_list:
        if e.Id == goal_id:
            return e


# input an interval of expense
# print all account match the condition
def searchExpense(acc_list, e_low: int, e_high: int):
    for e in acc_list:
        if e_low <= e.expense <= e_high:
            e.display()


file = open('record.txt', 'w', encoding='utf-8')
flag1 = True
accId = 0
accList = []


while flag1:
    fCodeDir()
    fCode = int(input('Enter the function code you want:'))
    if fCode == 1:
        print('\n' + 'input a new account')
        # -----------------------------input a new account--------------------------------------
        accId = accId + 1
        accName = str(input('Name:'))
        print('Enter food, clothing, housing, transportation, recreation, medical')
        accTag = str(input('Tag:'))
        accExpense = int(input('Expense:'))

        # check accTag input legal or not
        product = 1
        while True:
            for i in Tag:
                if i.name != accTag:
                    j = 1
                else:
                    j = 0
                product = product * j
            if product == 0:
                break
            else:
                print('The tag input is not in tag set.')
                print('Enter food, clothing, housing, transportation, recreation, medical')
                accTag = str(input('Tag:'))
        # ==================================

        accList.append(Account(accId, accName, Tag[accTag], accExpense))

        # -------------------------------------------------------------------------------------

    elif fCode == 2:
        print('display all account')
        for i in accList:
            i.display()

    elif fCode == 3:
        print('search the account by ID')
        goalId = int(input('Enter the id:'))
        if accExit(accList):
            Goal = searchId(accList, goalId)
            try:
                Goal.display()
            except AttributeError:
                print('not found')

        else:
            print('the account list is empty')

    elif fCode == 4:
        print('search the account by expense interval')
        low = int(input('input the min:'))
        high = int(input('input the max:'))
        searchExpense(accList, low, high)

    elif fCode == 5:
        print('5: select the account by ID')
        selectId = int(input('input the Id of account you want to select:'))
        goalAcc = searchId(accList, selectId)
        try:
            goalAcc.display()
        except AttributeError:
            print('not found')

    elif fCode == 6:
        print('6: revise the account')
        print('select the account by ID')
        selectId = int(input('input the Id of account you want to select:'))
        goalAcc = searchId(accList, selectId)
        try:
            goalAcc.display()
        except AttributeError:
            print('not found')

        try:
            attr = str(input('choose Name, Tag, Expense:'))
            if attr == 'Name':
                newName = str(input('Enter new name:'))
                goalAcc.reviseName(newName)
            elif attr == 'Tag':
                print('Enter food, clothing, housing, transportation, recreation, medical')
                newTag = str(input('Enter new tag:'))
                goalAcc.reviseTag(Tag[newTag])
            elif attr == 'Expense':
                newExpense = int(input('Enter new expense:'))
                goalAcc.reviseExpense(newExpense)
            else:
                print('input wrong instruction')
        # when tag input is not in Tag(enum) set, there will be KeyError
        except KeyError:
            print('input wrong tag name')
            print()

        goalAcc.display()

    elif fCode == 7:
        print('7: delete the account')
        print('select the account by ID')
        selectId = int(input('input the Id of account you want to select:'))
        goalAcc = searchId(accList, selectId)
        try:
            goalAcc.display()
            accList.remove(goalAcc)
        except (AttributeError, ValueError):
            print('not found')

    elif fCode == 8:
        print('8: save the record')
        for i in accList:
            file.write(str(i.Id))
            file.write('\n')
            file.write(i.Name)
            file.write('\n')
            file.write(i.tag.value)
            file.write('\n')
            file.write(str(i.expense))
            file.write('\n')
            file.write('\n')

    elif fCode == 9:
        flag1 = False







