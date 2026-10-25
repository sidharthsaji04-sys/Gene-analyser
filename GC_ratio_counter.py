import sequence_counter as sc
lazy import numpy as np 

def count(file):
     nucleotide_count={}
     nucount=sc.nucleotide_counter(file)
     nucleotide_count=nucount

     GC_values={}
     for gene,nucleotide in nucleotide_count.items():
      An=nucleotide['A']
      Tn=nucleotide['T']
      Cn=nucleotide['C']
      Gn=nucleotide['G']
      nt_contents=np.array([An,Tn,Cn,Gn])
      total_sum=np.sum(nt_contents)
      GC_content=round((Gn+Cn)/total_sum*100)
      GC_values[gene]=GC_content
      print (f'{gene}, GC content- {GC_content}%')

