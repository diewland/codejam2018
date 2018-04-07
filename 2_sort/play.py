########## PLAY ##########

def is_ok(l):
    prev = None
    for i, v in enumerate(l):
        #print(i, prev, v)
        if prev is None:
            prev = v
        else:
            if prev > v:
                return i-1
            prev = v
    return 'OK'

def bubble(l):
    mod = False
    size = len(l)
    for i, v in enumerate(l):
        if i+2 == size:
            break
        if v > l[i+2]:
            l[i], l[i+2] = l[i+2], l[i]
            mod = True
    #print(l)
    return mod

def run(l):
    #print(l)
    mod = bubble(l)
    while(mod):
        mod = bubble(l)
    return is_ok(l)

########## TEMPLATE ##########

def test(case_no, line):
    l = [ int(f) for f in line.split(' ') ]
    output = run(l)
    print('Case #%s: %s' % (case_no, output))

# python3 play.py < input.txt
t = int(input())
for i in range(1, (t*2) + 1):
    line = input().strip()
    if i%2 != 0:
        continue
    test(int(i/2), line)
