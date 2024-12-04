def  custom_write(file_name, strings):
    string_positions = {}
    new_str = 0
    file = open(file_name, 'w', encoding='utf-8')
    byte = file.seek(0)
    for i in strings:
        file.write(i + '\n')
        new_str += 1
        string_positions[(new_str, byte)] = i
        byte = file.tell()
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)