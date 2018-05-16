s = ""
k = ""
str = input("문자열 : ")
for i in range (len(str)):
    s = s + str[i]
for j in range (len(str)-1 , -1 ,-1):
    k = k + str[j]
print("개별 문자 출력 : " ,s)
print("역순 개별 문자 출력 : ",k)
