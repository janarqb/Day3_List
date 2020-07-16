guests = ['Carolyn', 'Mrs. Oliver', 'Mr. Tom']
guests.insert(0,'Olivia')
guests.insert(3,'Brandon')
guests.append('Alex')
print (guests)
print('Sorry, we will be able to host only 2 guests this Saturday')
print('Dear ' + guests.pop(-1) + ', ' 'Saturday event is canceled due to temporary spacing issues at our house, hope to see u next time and sorry for inconvenience caused!')
print('Dear ' + guests.pop(4) + ', ' 'Saturday event is canceled due to temporary spacing issues at our house, hope to see u next time and sorry for inconvenience caused!')
print('Dear ' + guests.pop(3) + ', ' 'Saturday event is canceled due to temporary spacing issues at our house, hope to see u next time and sorry for inconvenience caused!')
print('Dear ' + guests.pop(2) + ', ' 'Saturday event is canceled due to temporary spacing issues at our house, hope to see u next time and sorry for inconvenience caused!')
print('Dear ' + guests[0].title() + ',' + ' this is to remind that we will be waiting for you this Saturday to join us for July 4th celebration.')
print('Dear ' + guests[1].title() + ',' + ' this is to remind that we will be waiting for you this Saturday to join us for July 4th celebration.')
del guests[0:2]
print (guests)