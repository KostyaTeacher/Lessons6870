# cyrillic_to_latin = { 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye',
#                       'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l',
#                       'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
#                       'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia', ' ': ' ' }
#
# word = input("Введіть текст який хочете перекласти: ")
#
# for character in word:
#     word = word.replace(character,cyrillic_to_latin.get(character))
#
# print(word)

numbers = [5, [1, 2, [3, 5, 16]], 4, [5, 6, 7], [10]]
print(numbers[1][2][2])
