
names = [("Jacob", 15), ("Yaakov", 12), ("Tomer", 13), ("Tommer", 4), ("Sara", 19), ("Tommer", 10), ('Yaacov', 3)]
synonyms = [("Jacob", "Yaakov"), ("Yaakov", "Yaacov"), ("Tommer", "Tomer"), ('Yaacov', 'Jacov')]


def merge_syns(synonyms):
    syns = []
    for a, b in synonyms:
        f = False
        for s, _ in syns:
            if a in s:
                s.add(b)
                f = True
            if b in s:
                s.add(a)
                f = True
        if not f:
            syns.append([{a, b}, 0])
    return syns


def merge_names(names, synonyms):
    syns = merge_syns(synonyms)
    for name, frq in names:
        flag = False
        for pair in syns:
            set, _ = pair
            if name in set:
                pair[1] += frq
                flag = True
        if not flag:
            syns.append([{name}, frq])

    for st, sm in syns:
        print(st.pop(), sm)


def main():
    merge_names(names, synonyms)


if __name__ == '__main__':
    main()


