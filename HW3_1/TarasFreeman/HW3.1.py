Zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

word1 = "better"
word2 = "never"
word3 = "is"
word4 = "i"
word1_count = Zen_of_python.count(word1)
word2_count = Zen_of_python.count(word2)
word3_count = Zen_of_python.count(word3)
word4_count = Zen_of_python.count(word4)
print(f"The word 'better' occurs {word1_count}")
print(f"The word 'never' occurs {word2_count}")
print(f"The word 'is' occurs {word3_count}")
print(f"Letter 'i' occurs {word4_count}")

print(Zen_of_python.upper)

print(Zen_of_python.replace(i old, & new))
