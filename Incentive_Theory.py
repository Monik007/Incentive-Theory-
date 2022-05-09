# Monik Malik
# Price Discrimination of Airline Industry


a = int(input("economy seats: "))
b = int(input("1st class seats: "))
CT = [a, b]

print("   ")
TE = int(input("tourists with economy seat profit :"))
BE = int(input("business traveller with economy seat profit :"))
print("   ")
T1 = int(input("tourists with 1st class seat profit :"))
B1 = int(input("business traveller with 1st class seat profit :"))


R = [[TE, BE], [T1, B1]]

print("Cost of Airlines")
types= ["Economy  ", "1st Class"]
for i in range(len(CT)):
    print(types[i], " ", CT[i])

print("     ")



def RT(coa,pp):
    resTable = [[], []]
    x = 0
    y = 0
    tempx = 0
    tempy = 0
    for j in pp:
        t = pp.index(j)
        if j[0] >=x:
            tempx = j[0]+coa[t]
            x = j[0]
        if j[1] >=y:
            tempy = j[1]+coa[t]
            y = j[1]
        resTable[t].append(j[0]+coa[t])
        resTable[t].append(j[1]+coa[t])
    return resTable, tempx, tempy


def tempper(res_t):
    Ul = 0
    Ll = 0
    for i in res_t:
        Ul = abs(i[1] - Ul)
        Ll = abs(i[0] - Ll)
    return Ul, Ll





def P(coa,pp):
    resT,x, y = RT(coa,pp)
    print("with maximum profit actual charge of economy should be <=", x)
    print("with maximum profit actual charge of 1st class should be <=", y)
    print("   ")
    print("The reservation prices are as follows: ")
    print(*resT)
    print("   ")
    ans1, ans2 = tempper(resT)
    print("the cost of 1st class should be ", ans2, " to ", ans1, " more than economy")


P(CT, R)