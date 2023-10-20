# Tuple  คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ แต่แก้ไม่ได้ เพิ่มไม่ได้ลดไม่ได้
        #0  1   2  3    4        5  
Tuple = (10,20,True,10,'SAU',(20,'IOT'))
        #6  5   4   3   2        1    คือ -

#เข้าถึงข้อมูลเดียว

print(Tuple[4])
print(Tuple[-2])
print(Tuple[5])
print(Tuple[-1])
print(Tuple[5][1])

#เข้าถึงหลายข้อมูล

print(Tuple[1:4])
print(Tuple[-5:-2])
print(Tuple[3:])
print(Tuple[:3])

#เข้าถึงข้อมูลทั้งหมด

for info in Tuple :
    print(info, end=',')

print(Tuple)

List =list(Tuple)
List[4]="IOT"
Tuple=tuple(List)
print(Tuple)

#Tuple functions

print(Tuple.count(10))
print(Tuple.index("IOT"))

