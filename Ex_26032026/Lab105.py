letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u


def filter_vowels(letter):
    vowels= ['a','e','i','o','u']
    return letter in vowels


# result  = filter_vowel('p')
# print(result)

filtered_words = filter(filter_vowels,letters_list)
filtered_words1 = filter(filter_vowels,letters_tuple)
filtered_words2 = filter(filter_vowels,letters_set)

print(list(filtered_words))
print(list(filtered_words1))
print(list(filtered_words2))
