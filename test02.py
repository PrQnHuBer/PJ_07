#character string แต่ละตัวจะมี index number กำกับ
        #01234567890123
infoA = 'Hello SAU 2023'
        #43240987654321 คือ -

print(infoA[6])
print(infoA[-8])

#เข้าถึงstingแต่ละตัวผ่าน number เราจะใช้วิธี slicing ด้วย index numver

print(infoA[6:9])
print(infoA[-8:-5])

print(infoA[4:12])

#sting method
print(infoA.upper() )
print(infoA.lower() )
print(infoA.capitalize() )
print(infoA.title() )
print(infoA.count('l') )
print(infoA.isdigit() )
print(infoA.islower() )
infoB = infoA.replace('SAU','IOT')
print(infoA)
print(infoB)
print(infoB.replace('Hello','Hi'))

#sting

print(len(infoA) )