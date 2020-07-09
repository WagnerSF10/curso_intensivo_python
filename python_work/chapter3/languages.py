languages=['python','java','c','c++','c#','VB']
print(languages[-1].lower())
print("\nI'm studing:")
print(languages[0].upper())
languages[-1]='pascal'
print(languages)
languages=['python','java','c','c++','c#','VB']
languages.append('pascal')
print(languages)
languages=['python','java','c','c++','c#','VB']
languages.insert(0,'pascal')
print(languages)
languages=['python','java','c','c++','c#','VB']
del languages[5]
del languages[4]
print(languages)
languages=['python','java','c','c++','c#','VB']
print(languages)
popped_languages=languages.pop()
print(languages)
print(popped_languages)
languages=['python','java','c','c++','c#','VB']
print(languages)
csharp=languages.pop(4)
print(languages)
print(csharp)
languages=['python','java','c','c++','c#','VB']
languages.remove('VB')
print(languages)
languages=['python','java','c','c++','c#','VB']
message=", it's a programing language!"
print(languages[0].title() + message)
print(languages[-1].title() + message)
languages=['python','java','c','c++','c#','vb']
languages.sort()
print(languages)
languages=['python','java','c','c++','c#','vb']
languages.sort(reverse=True)
print(languages)
languages=['python','java','c','c++','c#','vb']
print(sorted(languages))
print(sorted(languages,reverse=True))
