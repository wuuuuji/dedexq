day_secs = 60 * 60 * 24
year_secs = 254 * day_secs

value = (2**64) - 1
years = value // year_secs
print("需要约 %d 年才可以获得结果" % years)