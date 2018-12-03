# -*- coding: utf-8 -*-
def convert_pos(word):
    flag = 0
    if word[0].isupper():
        flag = 1
    res = word.lower()
    if "bad" in res:
        res = res.replace("bad", "good")
    elif "horrible" in res:
        res = res.replace("horrible", "fantastic")
    elif "dirty" in res:
        res = res.replace("dirty", "clean")
    elif "disgusting" in res:
        res = res.replace("disgusting", "sublime")
    elif "expensive" in res:
        res = res.replace("expensive", "affordable")
    elif "moldy" in res:
        res = res.replace("moldy", "flavourful")
    elif "frozen" in res:
        res = res.replace("frozen", "farm-fresh")

    if flag == 1:
        res = res.capitalize()
    return res


def convert_half_time(s):
    words = s.split()

    for i in range(len(words) - 1):
        if words[i].isdigit():
            words[i] = "only " + str(int(int(words[i]) / 2))

    return "".join(str(x) + " " for x in words).strip()


def positivize(review):
    words = review.split()
    x = ""
    for w in words:
        x += convert_pos(w) + " "

    x = convert_half_time(x.strip())
    return x.strip()


if __name__ == '__main__':
    s = "The food was horrible!!!  We waited 40 minutes for frozen vegetables and moldy bread.  Disgusting!"
    print(positivize(s))
