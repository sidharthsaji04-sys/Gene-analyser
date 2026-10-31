import sequence_counter as sc
import numpy as np

def GC_count(file):

    nucleotide_count = sc.nucleotide_counter(file)

    GC_values = {}

    for gene, nucleotide in nucleotide_count.items():

        An = nucleotide['A']
        Tn = nucleotide['T']
        Cn = nucleotide['C']
        Gn = nucleotide['G']

        nt_contents = np.array([An, Tn, Cn, Gn])

        total_sum = np.sum(nt_contents)

        GC_content = round((Gn + Cn) / total_sum * 100, 2)

        GC_values[gene] = GC_content

    return GC_values