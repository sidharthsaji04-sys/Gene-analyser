import sequence_counter as sc

result=sc.counter('gene sequences.txt')
for results in result:
    print(results)

r=sc.nucleotide_counter('gene sequences.txt')
for result,sequence_count in r.items():
  print(f'{result}- {sequence_count}')
