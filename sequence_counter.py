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

   results={}
   for gene, seq in sequence.items():
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
        results[gene]={'A':An,'C':Cn,'G':Gn,'T':Tn}

   return results
     
