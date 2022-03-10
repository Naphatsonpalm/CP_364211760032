# Exercise Lab 8: Function


"""
จงกำหนดฟังก์ชัน ชื่อ "getNumber()" เพื่อรับข้อมูลจำนวนเต็มจากผู้ใช้
5 จำนวน และแสดงผลทางจอภาพ จากนั้นให้กำหนดฟังก์ชั่นต่อไปนี้
1. กำหนดฟังก์ชันชื่อ "totalValue()" เพื่อหาผมรวมของตัวเลขทั้งหมด แสดงผลทางจอภาพ
"""
def totalValue(mylist):
    total = 0
    for x in mylist:
        total += x
    return total

def getNumber():
    mylist = []
    for x in range(5):
        mylist.append(int(input('Enter integers: ')))
    print(mylist)
    return mylist

# calling funciton
mynum = getNumber()
total = totalValue(mynum)
print(f'total value is {total}')