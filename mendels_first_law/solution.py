k = 16 #homozygous dominant organisms in a population
m = 18 #heterozygous organisms in a population
n = 16 #homozygous recessive organisms in a population

# Function calculating probablility any two random organisms mate and produce an offspring with a dominant allele
def prob_dominant(k,m,n):
    sum = k + m + n #Total population of organisms
    
    #Probabilities of two organisms producing offspring with dominant allele
    prob_kk = ((k/sum) * ((k-1) / (sum-1))) * 1
    prob_km = ((k/sum) * ((m) / (sum-1))) * 1
    prob_kn = ((k/sum) * ((n) / (sum-1))) * 1
    prob_mm = ((m/sum) * ((m-1) / (sum-1))) * .75
    prob_mn = ((m/sum) * ((n) / (sum-1))) * .5
    prob_mk = ((m/sum) * ((k) / (sum-1))) * 1
    prob_nk = ((n/sum) * ((k) / (sum-1))) * 1
    prob_nm = ((n/sum) * ((m) / (sum-1))) * .5
    prob_nn = ((n/sum) * ((n-1) / (sum-1))) * 0
    
    prob_dom_allele = prob_kk + prob_km + prob_kn + prob_mm + prob_mn + prob_mk + prob_nk + prob_nm + prob_nn
    #Totaling probabilities
    return prob_dom_allele

# %%
print(prob_dominant(k,m,n))


