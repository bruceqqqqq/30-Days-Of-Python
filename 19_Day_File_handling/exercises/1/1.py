def count_lines_n_words(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
        words = [words for words in lines for words in words.split(' ')]
        return f'This speech has {len(lines)} lines and {len(words)} words.'

print(count_lines_n_words('donald_speech.txt'))
print(count_lines_n_words('melina_trump_speech.txt'))
print(count_lines_n_words('obama_speech.txt'))
print(count_lines_n_words('melina_trump_speech.txt'))
