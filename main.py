import argparse


def parse_file(filename):
    names = []
    synonyms = []
    with open(filename, "r") as file:
        names, synonyms = file.readlines()
        names, synonyms = names.replace(' ', ''), synonyms.replace(
            ' ', '').replace('(', '').replace(')', '')
        names, synonyms = names[6::].split(','), synonyms[9::].split(',')
        names = [(n[:n.index('(')], int(n[n.index('(') + 1:n.index(')')]))
                 for n in names]
        synonyms = list(zip(synonyms[::2], synonyms[1::2]))
    return names, synonyms


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
    print(', '.join([f"{st.pop()}({sm})" for st, sm in syns]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()
    try:
        merge_names(*parse_file(args.file))
    except FileNotFoundError:
        print("given file not found")
    except Exception as e:
        print("faild parsing given file")


if __name__ == '__main__':
    main()
