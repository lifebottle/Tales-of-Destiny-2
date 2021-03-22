import os
import sys


def jpnToHex(word):

    mapping = {}

    fo = open(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           '..', '_dictionary//tod2_utf8.txt')), "r", encoding="utf8")
    Lines = fo.readlines()

    for line in Lines:
        if line[0] != "A":
            mapping[line[6]] = line[0:2] + " " + line[2:4]

    for line in Lines:
        if (len(line) > 6):
            mapping[line[6]] = line[0:2] + " " + line[2:4]
        else:
            mapping[line[4]] = line[0:2]

    jap = list(word)
    List = []

    for i in jap:
        if i in mapping:
            List.append(mapping[i] + " ")

    return "".join(List)


# running the file defaults to this def (needed for node API)
if __name__ == '__main__':
    data = jpnToHex(sys.argv[1])
    print(data)

# TEST
# print(jHex("ア イ テ ム な ぞ 使 っ て ん じ ゃ ね え ！"))
