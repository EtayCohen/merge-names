import argparse


def parse_file(filename):
    """
    Parse given file
    :param filename: file to parse
    :return: names and synonyms
    """
    names = []
    synonyms = []
    with open(filename, "r") as file:
        names, synonyms = file.read().splitlines()[:2]
        names, synonyms = names.replace(' ', ''), synonyms.replace(
            ' ', '').replace('(', '').replace(')', '')
        names, synonyms = names[6::].split(','), synonyms[9::].split(',')
        names = [(n[:n.index('(')], int(n[n.index('(') + 1:n.index(')')]))
                 for n in names]
        synonyms = list(zip(synonyms[::2], synonyms[1::2]))
    return names, synonyms


def merge_syns(synonyms):
    """
    Merge synonyms
    :param synonyms: synonyms to merge
    :return: merged synonyms
    """
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
    """
    Merge names according to synonyms
    :param names: names to merge
    :param synonyms: synonyms
    :return: None
    """
    map = merge_syns(synonyms)
    for name, frq in names:
        flag = False
        for pair in map:
            set, _ = pair
            if name in set:
                pair[1] += frq
                flag = True
        if not flag:
            map.append([{name}, frq])
    print(', '.join([f"{st.pop()}({sm})" for st, sm in map]))


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
