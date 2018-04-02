def apriori_prune(ck, min_support):
    L = []
    for i in ck:
        if ck[i] >= min_support:
            L.append(i)

    return sorted(L)


def apriori_generate(itemset, length):
    candidate = []
    for i in range(0, length):
        element = str(itemset[i])
        for j in range(i + 1, length):
            element1 = str(itemset[j])
            if element[0:(len(element) - 1)] == element1[0:(len(element1) - 1)]:
                unionset = element[0:(len(element) - 1)] + element1[len(element1) - 1] + element[len(element) - 1]
                # Combine (k-1)-Itemset to k-Itemset
                unionset = ''.join(sorted(unionset))
                candidate.append(unionset)
    return candidate


def apriori_Count_Subset(candidate,candidate_length):
    lk=dict()
    file=open('data.txt')
    for l in file:
        l=str(l.split())#each line in string
        count=0;
        for i in range(0,candidate_length):
            key=str(candidate[i])
            if key not in lk:
                lk[key]=0
            flag =True
            for k in key:
                if k not in l:
                    flag=False
            if flag:
                lk[key]+=1
    file.close()
    return lk

min_support=3
c1={}
file=open('data.txt')
for line in file:
    for item in line.split(','):
        if item in c1:
            c1[item]+=1

        else:
            c1[item]=1
file.close()
c1.keys().sort()
L1=apriori_prune(c1,min_support)
L=apriori_generate(L1,len(L1))
print'frequent 1 item sets are', L1
print('')
print'combination is  :', L
k=2
while  L!=[]:
    c=dict()
    c=apriori_Count_Subset(L,len(L))
    frequent_itemsets=[]
    frequent_itemsets=apriori_prune(c,min_support)
    print('')
    print'frequent ',k,'- item sets are ',frequent_itemsets
    L=apriori_generate(frequent_itemsets,len(frequent_itemsets))
    print'combination is  :', L
    k=k+1



















