def first_most_common_words(filename, qnts):
    with open(filename) as file:
        f = file.read()
        words = [w for w in f.split()]
        first_common = []
        for w in words:
            if w not in first_common:
                first_common.append(w)

        result = []
        for word in first_common:
            result.append((words.count(word), word))

        return list(reversed(sorted(result[:qnts])))
