"""
Name: {นภัสสร สรรพบุรุษ}
SID: {364211760032}
Group: {MIT212}
"""

"""
Question 6:
จงเขียนโปรแกรมรับค่าปี ค.ศ. จากนั้นให้แสดงผลปี พ.ศ.
และผลรวมของตัวเลขแต่ละหลักของปี ค.ศ. และ พ.ศ. ดังตัวอย่างต่อไปนี้

Input (ค.ศ.): 2022
Output (พ.ศ.): 2565
Sum (ค.ศ.): 6
Sum (พ.ศ.): 18


(10 คะแนน)
"""
try:
    year = int(input( 'ค.ศ.:' ))
except:
    year = 0

if year > 0:
    x = year + 543
    print('พ.ศ.:',x,)