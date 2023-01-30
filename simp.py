import mainfunctions
import numpy as np

#**********************************************************************************************************************************************************
def extract_tobe_simplified(minterms):
    simplified=[]
    found=False
    for i in range(len(minterms)):
        if found==False:
            for j in range(i+1,len(minterms)):
                diff=mainfunctions.difference(minterms[i],minterms[j])
                if minterms[i] in simplified:break
                if diff:
                    simplified.append(minterms[i])
                    simplified.append(minterms[j])
                    found=True
                    break
        else:found=False
    remaining=list(np.setdiff1d(minterms,simplified))
    return simplified,remaining

#***************************************************************************************************************************************************************************
def common_factor_simplification(simplified):
    simplified=mainfunctions.join_with_apos(simplified)
    factors=[]
    i=0
    done=[]
    read=[]
    while i<len(simplified)-1:
            different=list(np.setdiff1d(simplified[i],simplified[i+1]))+list(np.setdiff1d(simplified[i+1],simplified[i]))
            simplified[i].remove(different[0])
            try:string='({}+{})'.format(different[0],different[1])
            except:string=''
            done.append(simplified[i])
            read.append(''.join(simplified[i])+string)
            i+=2
    for simple in range(len(done)):
        done[simple]=''.join(done[simple])
    return done,read

#*************************************************************************************************************************************************

def simplification(minterms):
    simplified,remaining=extract_tobe_simplified(minterms)
    done,read=common_factor_simplification(simplified)
    it_before=' + '.join(minterms)+'\n'
    it_after=' + '.join(read+remaining)
    count=len(simplified)
    #print(it_before)
    #print(it_after)
    #print(remaining+done)
    return it_before,it_after,remaining+done,count
    #if count>2:
     #   simplification(remaining+done)

def simplification2(minterms):
    i=0
    read_bracket=[]
    remaining=[]
    simplified=[]
    after_simp=[]
    while i<len(minterms)-1:
            found=False
            for j in range(i+1,len(minterms)):
                aposed=mainfunctions.join_with_apos([minterms[i],minterms[j]])
                common=list(set(aposed[0]).intersection(aposed[1]))
                common=mainfunctions.sort_it(common)
                if len(common)!=0 and (minterms[i] not in simplified) and (minterms[j] not in simplified):
                    found=True
                    aposed_uncommon=mainfunctions.get_common(aposed,common)
                    print(aposed_uncommon)
                    k,changed=mainfunctions.dashed_simplification(aposed_uncommon)
                    print(k)
                    print(changed)
                    if changed==True:
                        simplified.append(minterms[i])
                        simplified.append(minterms[j])
                        aposed_uncommon=mainfunctions.get_common(aposed,common)
                        before_simp=''.join(common)+'({}'.format(''.join(aposed_uncommon[0])+'+{})'.format(''.join(aposed_uncommon[1])))
                        read_bracket.append(before_simp)
                        dashed,changed=mainfunctions.dashed_simplification(aposed_uncommon)
                        first=dashed[0] ; second=dashed[1]
                        after_simp.append(''.join(common+first))
                        after_simp.append(''.join(common+second))
                    break
            if not found:
                remaining.append(minterms[i])
            i+=1
    count=len(simplified)
    it_before='+'.join(minterms)
    it_after='+'.join(read_bracket+remaining)
    #print('after simp:', after_simp)
    #print('remaining:', remaining)
    #print('+'.join(remaining+after_simp
    return it_before,it_after,remaining+after_simp,count
