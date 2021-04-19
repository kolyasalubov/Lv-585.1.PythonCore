string = \
"""Beautiful is better than ugly. 
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
Namespaces are one honking great idea -- let's do more of those!
"""
count_of_better = string.count("better")
count_of_never = string.count("never")
count_of_is = string.count("is")
Is = "is"
print("Word %s appears %d times in Zen" %("better", count_of_better))
print("Word {0} appears {1} times in Zen".format("never", count_of_never))
print(f"Word {Is} appears {count_of_is} times in Zen")
print("\n" + string.upper())
print("\n" + string.replace("i","&"))