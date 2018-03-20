if __name__ == '__main__':
    s = input()

res = False
a = (c.isalnum() for c in s)
for i in a:
    res = res or i
print(res)

res = False
b = (c.isalpha() for c in s)
for i in b:
    res = res or i
print(res)

res = False
d = (c.isdigit() for c in s)
for i in d:
    res = res or i
print(res)

res = False
e = (c.islower() for c in s)
for i in e:
    res = res or i
print(res)

res = False
f = (c.isupper() for c in s)
for i in f:
    res = res or i
print(res)

print('---')
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(c) for c in s))

print('---')
print (any(c.isalnum() for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))
