"""
Name: {นภัสสร สรรพบุรุษ}
SID: {364211760032}
Group: {MIT212}
"""

"""
Question 5:
เขียนโปรแกรมเพื่อคำนวณค่า Body Mass Index (BMI) โดยรับ input เป็นน้ำหนักตัวและส่วนสูง
จากนั้นแสดงผล BMI ทาง output ตามสมการต่อไปนี้

สูตรคำนวนค่าดัชนี้มวลกาย

ิดัชนีมวลกาย = น้ำหนักตัว (kg)/((ส่วนสูง(เมตร)) * (ส่วนสูง(เมตร)))

ตัวอย่างผลลัทพ์

น้ำหนัก: 80
ส่วนสูง(cm):180
ํดัชนีมวลกายของคุณ เท่ากับ 24.5

(10 คะแนน)
"""
w=int(input("ป้อนน้ำหนัก(kg):"))
h=int(input("ป้อนส่วนสูง(kg):"))/100
bmi=w/h**2
print("bmi ของคุณคือ",bmi)

if bmi<30 and bmi>29.9:
  print("โรคอ้วน มีความเสี่ยง")
elif bmi<29.9 and bmi> 24.9:
  print("โรคอ้วน")
elif bmi<24.9 and bmi>22.9:
  print("น้ำหนักเกิน")
elif bmi<22.9 and bmi>18.5:
  print("สมส่วน")
else:
  print("ผอม")