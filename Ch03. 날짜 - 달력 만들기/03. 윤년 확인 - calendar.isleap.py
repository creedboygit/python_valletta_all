# 윤년 판별 함수
def isLeapYear(year): # 윤년이면 True, 아니면 False를 출력하는 함수
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(isLeapYear(2022))

print(isLeapYear(2020))

import calendar

print(calendar.isleap(2022))
print(calendar.isleap(2020))

# 윤년 횟수
print(calendar.leapdays(1990, 2022))

# 요일 반환
print(calendar.weekday(2024, 2, 7))

# 달력 출력
print(calendar.calendar(2024, 2, 1, 2, 20))
print(calendar.calendar(2024))





