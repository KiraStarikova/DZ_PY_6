
import calendar
import sys

def funcDate():
    text = input('DD.MM.YYYY - >>> ')
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1]
    if int(text[0]) <= days and int(text[1]) <= 12:
        print('Нормальная дата')
        a = input('')
        return True
    else :
        print('не корректная дата')
        a = input('')
        return False

def _vysYear(year):
    if calendar.monthrange(year, 2) == 29:
        return True
    else:
        return False

if __name__=='__main__':
    funcDate()