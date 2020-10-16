# 15. Write a Python function to create the HTML string with tags around the word(s). Go to the editor
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

s = input("Type your sentence: ")
tag = input(
    "In which tag do you whant to wrap your sentence? Type without brackets (eg a, b, p): ")


def add_tags(attr="p", string="Python"):
    print("<" + attr + ">" + string + "</" + attr + ">")


add_tags(tag, s)
