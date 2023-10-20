#  List  คือข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้
        #0  1   2  3    4        5  
List = [10,20,True,10,'SAU',[20,'IOT']]
        #6  5   4   3   2        1    คือ -
#การเข้าถึงข้อมูลใน list เข้าถึงแต่ละข้อมูล เข้าถึงทีละหลายข้อมูล เข้าถึงข้อมูลทั้งหมด
#เข้าถึงแต่ละข้อมูลใน list
 
print(List[4])
print(List[-2])
print(List[5])
print(List[-1])
print(List[5][1])

#เข้าถึงหลายข้อมูลใน list

print(List[1:4])
print(List[-5:-2])
print(List[3:])
print(List[:3])

#เข้าถึงข้อมูลทั้งหมด for in

for info in List :
    print(info, end=',')

print(List)
List[4] = 'Thailand'
print(List)

#list method

List.append ('wow')
List.append ([10,20,30])
print(List)

List.extend(['A','B'])
print(List)

#เอาออกแค่ตัวแรกที่เจอ
List.remove(10)
List.remove(20)
List.remove([10,20,30])
print(List)

List.pop()
List.pop()
List.pop()
print(List)

#List funcion -> len(),min(),max()
List2 = [10,20,10,30,True]
print(len(List2))
print(min(List2))
print(max(List2))
