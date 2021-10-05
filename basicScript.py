
def sentence_maker(phrase):
    interogatives = ("how","what","when","where")
    capitalized = phrase.capitalize()
    if phrase.startswith((interogatives)):
        return "{} ?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
results = []
while True:
    uinput = input("Say something : ")
    if uinput == '\end':
        break
    else:
        results.append(sentence_maker(uinput))

print(" ".join(results))


temps = [23,-67,45]

temps = [temp/10 if temp!=-67 else 0 for temp in temps ]
print(temps)


def meanargs(*args):
    return sum(args)/len(args)

print(meanargs(1,4,56))


def meanskwargs(**kwargs):
    return kwargs

print(meanskwargs(a=1,b=3))