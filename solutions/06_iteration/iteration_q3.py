
data = '01-result.xls,2-result.xls,03-result.data,019-result.xls'

filenames = data.split(',')

titles = []
for filename in filenames:
    last_dot = filename.rfind('.')
    if last_dot >= 0:
        filename = filename[:last_dot]
    fields = filename.split('-')
    if len(fields) < 2 :
        fields.insert(0, '0')
    titles.append('{:s}{:02d}'.format(
                  fields[1], int(fields[0])))

print(titles)
