# 윤년 판별 함수
def isLeapYear(year): # 윤년이면 True, 아니면 False를 출력하는 함수
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(isLeapYear(2022))

print(isLeapYear(2020))


