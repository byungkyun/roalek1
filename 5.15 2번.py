t = ""
y = ""
string = input("문자열 : ")
for i in range (len(string)):
    t = t + string[i]
for j in range (len(string)-1 , -1 ,-1):
    y = y + string[j]
print("개별 문자 출력 : " ,t)
print("역순 개별 문자 출력 : ",y)
