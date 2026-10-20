def counter(file):
    sequence={}
    current_gene=None
    with open (file) as f:
      for line in f:
        line=line.strip()
        if line.startswith('>'):
            current_gene=line.split("[gene=")[1].split("]")[0]
            sequence[current_gene]=""
        else:
            sequence[current_gene]+=line

      results=[]
      for gene,seq in sequence.items():
        results.append(( gene,len(seq)))

    return results

def nucleotide_counter(file):
   sequence={}
   current_gene=None
   with open (file) as f:
         for line in f:
           line=line.strip()
           if line.startswith('>'):
               current_gene=line.split("[gene=")[1].split("]")[0]
               sequence[current_gene]=""
           else:
               sequence[current_gene]+=line

   for gene, seq in sequence.items():
    results={}
    An = Tn = Cn = Gn = 0
    for se in seq:              
        if se == "A":
            An += 1
        elif se == "C":
            Cn += 1
        elif se == "T":
            Tn += 1
        elif se == "G":
            Gn += 1

    results['gene']=f"{gene}: adenine={An}, guanine={Gn}, thymine={Tn}, cytosine={Cn}"
   for gene, sequ in results.items:
      return gene and results 
# not working , check and fix
     
