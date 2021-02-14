def time_convert(num):
    hours = num // 60
    minutes = num % 60
    return ("{}:{}".format(hours, minutes))

print(time_convert(200))
