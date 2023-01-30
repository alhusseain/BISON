from tabulate import *
def new (p,f):
    pp = 1
    At = 0
    Bt = 0
    Ct = 0
    output = []
    output_t = []
    #the truth table main elements
    headers_t = ['A', 'B', 'output']
    headers_tt = ['A', 'B', 'C', 'output']
    headers_ttt = ['A', 'B', 'C', 'D', 'output']
    t1 = [0, 0, 1, 1]
    t2 = [0, 1, 0, 1]
    tt1 = [0, 0, 0, 0, 1, 1, 1, 1]
    tt2 = [0, 0, 1, 1, 0, 0, 1, 1]
    tt3 = [0, 1, 0, 1, 0, 1, 0, 1]
    ttt1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ttt2 = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    ttt3 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    ttt4 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    if p == 2:
        n = f.replace('A', 'At').replace('B', 'Bt')
        for i in range(0, len(t1)):
            At = t1[i]
            Bt = t2[i]
            AtBt = t2[i]*t1[i]
            BtAt = t2[i]*t1[i]
            if eval(n)>1:
                n = 'pp'
            output.append(eval(n))
#to convert the output to become vertical
        for j in range(0, 4):
            converter = [t1[j], t2[j], output[j]]
            output_t.append(converter)
        return (tabulate(output_t, headers="ABF", tablefmt="fancy_grid"))

    if p == 3:
        n = f.replace('A', 'At').replace('B', 'Bt').replace('C', 'Ct')
        for i in range(0, len(tt1)):
            At = tt1[i]
            Bt = tt2[i]
            Ct = tt3[i]
            AtAt = tt1[i]*tt1[i]
            AtBt = tt1[i]*tt2[i]
            AtCt = tt1[i]*tt3[i]
            BtAt = tt2[i]*tt1[i]
            BtBt = tt2[i]*tt2[i]
            BtCt = tt2[i]*tt3[i]
            CtAt = tt3[i]*tt1[i]
            CtBt = tt3[i]*tt2[i]
            CtCt = tt3[i]*tt3[i]
            AtBtCt = tt1[i]*tt2[i]*tt3[i]
            AtCtBt = tt1[i]*tt2[i]*tt3[i]
            BtAtCt = tt1[i]*tt2[i]*tt3[i]
            BtCtAt = tt1[i]*tt2[i]*tt3[i]
            CtAtBt = tt1[i]*tt2[i]*tt3[i]
            CtBtAt = tt1[i]*tt2[i]*tt3[i]

            if eval(n)>1:
                n = 'pp'
            output.append(eval(n))
#to convert the output to become vertical
        for j in range(0, 8):
            converter = [tt1[j], tt2[j], tt3[j], output[j]]
            output_t.append(converter)
        return (tabulate(output_t, headers="ABCF", tablefmt="fancy_grid"))

    if p == 4:
        n = f.replace('A', 'At').replace('B', 'Bt').replace('C', 'Ct').replace('D', 'Dt')
        for i in range(0, len(ttt1)):
            At = ttt1[i]
            Bt = ttt2[i]
            Ct = ttt3[i]
            Dt = ttt4[i]
            AtAt = ttt1[i]*ttt1[i]
            AtBt = ttt1[i]*ttt2[i]
            AtCt = ttt1[i]*ttt3[i]
            AtDt = ttt1[i]*ttt4[i]
            BtAt = ttt2[i]*ttt1[i]
            BtBt = ttt2[i]*ttt2[i]
            BtCt = ttt2[i]*ttt3[i]
            BtDt = ttt2[i]*ttt4[i]
            CtAt = ttt3[i]*ttt1[i]
            CtBt = ttt3[i]*ttt2[i]
            CtCt = ttt3[i]*ttt3[i]
            CtDt = ttt3[i]*ttt4[i]
            DtAt = ttt4[i]*ttt1[i]
            DtBt = ttt4[i]*ttt2[i]
            DtCt = ttt4[i]*ttt3[i]
            DtDt = ttt4[i]*ttt4[i]
            AtBtCt = ttt1[i]*ttt2[i]*ttt3[i]
            AtCtBt = ttt1[i]*ttt2[i]*ttt3[i]
            BtAtCt = ttt1[i]*ttt2[i]*ttt3[i]
            BtCtAt = ttt1[i]*ttt2[i]*ttt3[i]
            CtAtBt = ttt1[i]*ttt2[i]*ttt3[i]
            CtBtAt = ttt1[i]*ttt2[i]*ttt3[i]
            AtBtCtDt = ttt1[i]*ttt2[i]*ttt3[i]*ttt4[i]

            if eval(n)>1:
                n = 'pp'
            output.append(eval(n))
        for j in range(0, 16):
            converter = [ttt1[j], ttt2[j], ttt3[j], ttt4[j], output[j]]
            output_t.append(converter)
        return (tabulate(output_t, headers="ABCDF", tablefmt="fancy_grid"))