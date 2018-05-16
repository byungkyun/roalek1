s = ""
k = ""
string = input("문자열 : ")
for i in range (len(string)):
    s = s + string[i]
for j in range (len(string)-1 , -1 ,-1):
    k = k + string[j]
print("개별 문자 출력 : " ,s)
print("역순 개별 문자 출력 : ",k)
