from stop_words import stop_words as words

def similaritytexts(file1, file2):
    with open(file1) as file1:
        f1 = file1.read().splitlines()
        speech = [w for w in f1 for w in w.split(' ')]
        wxs = []
        for w in words:
            if w in speech:
                wxs.append(w)

    with open(file2) as file2:
        f2 = file2.read().splitlines()
        speech = [w for w in f2 for w in w.split(' ')]
        wxs1 = []
        for w in words:
            if w in speech:
                wxs1.append(w)

    result = []
    for w in wxs:
        if w in wxs1:
            result.append(w)

    return result

print(similaritytexts('melina_trump_speech.txt', 'michelle_obama_speech.txt'))
