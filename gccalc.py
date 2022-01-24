
# function calculates the amount of G and C in a read
def calc_gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc_count = seq.count('C') + seq.count('G')
    gc_content = gc_count / len(seq) * 100
    #print(seq.count('C'))
    #print(seq.count('G'))
    #print(len(seq))
    return gc_content

