# условия Дано текущее время (часы, минуты, секунды). Определить, сколько время будет через 10 секунд
hours = 4
minutes = 59
seconds = 59

seconds += 10
if seconds >= 60:
    minutes += seconds // 60
    seconds %= 60
if minutes >= 60:
    hours += minutes // 60
    minutes %= 60
if hours >= 24:
    hours %= 24
print(hours, minutes, seconds)