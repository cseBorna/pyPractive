s=input()
def capital(s):
    l = [x.capitalize() for x in s.split(" ")]
    return ' '.join(l)

print(capital(s))
