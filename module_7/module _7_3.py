class WordsFinder:
    """Класс поиска слов"""
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        all_words = {}
        punct = ',.=!?;:'
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                reg = file.read().lower()
                while reg.find(' — ') != -1:
                    reg = reg.replace(' — '," ")
                    continue
                for p in punct:
                    if p in reg:
                        reg = reg.replace(p, '')
                    all_words[file_name] = reg.split()
        return all_words

    def find(self, word):
        poz_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                num = words.index(word.lower()) + 1
                poz_word[name] = num
        return poz_word

    def count(self, word):
        number_of_words = {}
        for name, words in self.get_all_words().items():
            num_words = words.count(word.lower())
            if num_words > 0:
                number_of_words[name] = num_words
        return number_of_words

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))      # Позиция слова
print(finder.count('teXT'))     # Количество вхождений слова

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
