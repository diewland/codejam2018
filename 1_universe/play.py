########## PLAY ##########

def calc_dmg(p):
    dmg = 0
    beam = 1
    for c in p:
        if c == 'C':
            beam *= 2
        else: # S
            dmg += beam
    return dmg

def hack(p):
    index = p.find('CS')
    if index == -1:
        return None
    return p.replace('CS', 'SC', 1)

def run(case_no, d, p):
    hack_times = 0

    dmg = calc_dmg(p)
    while dmg > d:
        p = hack(p)
        if p is None:
            return 'IMPOSSIBLE'
        hack_times += 1
        dmg = calc_dmg(p)

    return hack_times

########## TEMPLATE ##########

def test(case_no, line):
    data = line.split(' ')
    if len(data) != 2:
        print("Case #%s: %s" % (case_no, 0))
    else:
        d = int(data[0])
        p = data[1]
        output = run(case_no, d, p)
        print("Case #%s: %s" % (case_no, output))

# python3 play.py < input.txt
t = int(input())
for i in range(1, t + 1):
    line = input().strip()
    test(i, line)
