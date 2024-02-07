import datetime

# strptime
# 문자열을 datetime 객체로 변환
# 연(%Y), 월(%m), 일(%d), 시(%H), 분(%M), 초(%S)
str_datetime = '2024-02-07 21:31:48' # 날짜 형식 문자열
currdate = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

print(currdate)
print(currdate.year)
print(currdate.month)
print(currdate.day)
print(currdate.hour)
print(currdate.minute)
print(currdate.second)
print(type(currdate))

# strftime
# datetime 객체를 문자열로 변환
now = datetime.datetime.now()
print(now)

date = now.strftime('%Y-%m-%d')
print(date)
print(type(date))

time = now.strftime('%H:%M:%S')
print(time)
print(type(time))

datetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(datetime)
print(type(datetime))


