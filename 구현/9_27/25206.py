grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

hap = 0
isu =0
for i in range(20):
    a,b,c = input().split()
    b= float(b)
    if c == 'P':
        continue
    hap += b*grade[c]
    isu += b

print(hap/isu)