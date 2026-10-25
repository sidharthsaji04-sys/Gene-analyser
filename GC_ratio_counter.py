import sequence_counter as sc

total_count={}
ncount=sc.counter('gene sequences.txt')
for gene,count in ncount:
    total_count[gene]=count

print(total_count)

nucleotide_count={}
nucount=sc.nucleotide_counter('gene sequences.txt')
nucleotide_count=nucount

print(nucleotide_count)

# you use these to count the GC content of each gene. use numpy. then create a readme and finish
# you got this bro