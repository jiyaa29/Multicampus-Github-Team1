#주민등록 번호 판별 프로그램
#주민등록번호는 13자리이다.
#주민등록번호는 앞에 6자리와 7자리로 구성되어있다.

#remove - text in the string
text = "-"
def remove(text, remove):
    return text.replace(remove, "")



sn = input("주민등록번호 : ")
rule = "234567892345"
number = 0
 
for i in range(len(rule)):
    number = number + (int(sn[i])*int(rule[i]))
 
if 11-(number%11)<10:
    if 11-(number%11)==int(sn[12]):
        print("정상적인 주민등록번호입니다.")
elif 11-(number%11)>10:
    if 11-(number%11)-10==int(sn[12]):
        print("정상적인 주민등록번호입니다.")
else:
    print("정상적인 주민등록번호가 아닙니다.")