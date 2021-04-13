philosophy = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
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

print("\n1. Find the number of occurrences of the words (better, never, is) in a given string:\n")
word1 = "better"
word2 = "never"
word3 = "is"
word1_count = philosophy.count(word1)
word2_count = philosophy.count(word2)
word3_count = philosophy.count(word3)
print(f"The word 'better' occurs {word1_count} times in the string.")
print(f"The word 'never' occurs {word2_count} times in the string.")
print(f"The word 'is' occurs {word3_count} times in the string.")

print("\n2. Display all text in uppercase:\n")
print(philosophy.upper())

print("\n3. Change all occurrences of the character 'i' to '&':\n")
print(philosophy.replace("i", "&"))
