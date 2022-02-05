# Merge Names

As of any year, the government lists the top 10,000 common names
and their frequency.
As any name could be spelled differently that results in repetitions.

# Running

For a given formatted file:

```text
    Names: Jacob (12), Sara(12), Tommer(4), Yaacov(3), Tomer(6)
    Synonyms: (Yaakov, Jacob), (Yaakov, Yaacov), (Tomer, Tommer)
```

And by running the script:

```sh
    python3 main.py --file file.txt
```

Results:

```text
    Yaakov(15), Tomer(10), Sara(12)
```

# Implementation

    Parsing the file
    Names: ('Jacob', 12), ('Sara', 12), ('Tommer', 4), ('Yaacov', 3), ('Tomer', 6)]
    Synonyms: [('Yaakov', 'Jacob'), ('Yaakov', 'Yaacov'), ('Tomer', 'Tommer')]

    Megring Synonyms
    Synonyms: [[{'Yaacov', 'Yaakov', 'Jacob'}, 0], [{'Tommer', 'Tomer'}, 0]]

    Merging Names
    [[{'Yaakov', 'Jacob', 'Yaacov'}, 15], [{'Tomer', 'Tommer'}, 10], [{'Sara'}, 12]]

    Output
    Yaakov(15), Tomer(10), Sara(12)
