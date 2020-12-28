""" Input phrase manipulating """
def sentence_maker(phrase):
    """ sentence maker """
    interrogative = ("how", "what", "why")
    capitilize = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(capitilize)
    else:
        return "{}.".format(capitilize)

result = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentence_maker(user_input))

print(" ".join(result))