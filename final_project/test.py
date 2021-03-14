def test(*keys):
    for i in range(len(keys)):
        print(keys[i])

test('History', 'Geography', 'Literature', 'Biology', 'Algebra', 'Drawing', 'Chemistry')

class Aa:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        bb = []
        for i in range(len(b)):
            bb.append(b[i])



obj_a = Aa(14,('Pit', 'Nina', 'Olya'))

print(obj_a.b)