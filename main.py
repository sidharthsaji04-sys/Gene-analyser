import sequence_counter as sc
import GC_ratio_counter as gc

result=sc.counter('gene sequences.txt')
print('Total no of nucleotides in each gene')
for results in result:
    print(results)

r=sc.nucleotide_counter('gene sequences.txt')
print('No of each nucleotides')
for result,sequence_count in r.items():
  print(f'{result}- {sequence_count}')

print('Guanine-cytosine ratio of each gene')
Gc=gc.count('gene sequences.txt')
print(Gc)