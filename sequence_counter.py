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
