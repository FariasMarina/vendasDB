import arrow

data = arrow.now()
print(data)

data = arrow.now().format('HH:mm')
print(data)

data = arrow.get(46849648)
print(data)



date_1 = arrow.get('2001-01-04 18:40:48','YgYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 13:18:20','YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)
