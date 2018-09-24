"""CSCA08 Assignment 1, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Xinzheng Xu
 UtorID: xuxinzhe
 Student Number: 1004050661
 Date: 2017/11/05
"""


def pair_genes(gene1, gene2):
    '''(str, str) -> bool
    Takes in two strings representing genes, and returns True iff the two genes
    can pair. Genes can be paired together by allowing the nucleotides from one
    gene to pair-bond with the nucleotides from another. Interestingly, G will
    pair with C, and A will pair with T, but other combinations will not pair.
    REQ: The input should be two strings representing genes.
    >>> pair_genes('TCAG', 'AGTC')
    True
    >>> pair_genes('TCAG', 'CTGA')
    True
    >>> pair_genes('TCAG', 'CTGG')
    False
    '''
    # create a new bool value
    pair = None
    # check the two strings if they can pair or not
    pair = frontpair(gene1, gene2) or backpair(gene1, gene2)
    # whether can or cannot pair, return
    return pair


def frontpair(g1, g2):
    '''(str, str) -> bool
    Given two strings representing two genes, check if they can pair in
    positive sequence.
    >>> frontpair('TCAG', 'AGTC')
    True
    >>> frontpair('TCAG', 'CTGA')
    False
    '''
    # create a new bool value
    fpair = None
    # check the two strings if they can pair or not
    for i in range(len(g1)):
        if (g1[i] == 'G') and (g2[i] == 'C'):
            fpair = True
        elif (g1[i] == 'C') and (g2[i] == 'G'):
            fpair = True
        elif (g1[i] == 'A') and (g2[i] == 'T'):
            fpair = True
        elif (g1[i] == 'T') and (g2[i] == 'A'):
            fpair = True
        # if cannot pair, return False immediately
        else:
            fpair = False
            return fpair
    # if lengths are different, then False
    if(len(g1) != len(g2)):
        fpair = False
    # if can pair, return True
    return fpair


def backpair(g1, g2):
    '''(str, str) -> bool
    Given two strings representing two genes, check if they can pair in
    negative sequence.
    >>> backpair('TCAG', 'AGTC')
    False
    >>> backpair('TCAG', 'CTGA')
    True
    '''
    # create a new bool value
    bpair = None
    # check the two strings if they can pair or not
    for i in range(len(g1)):
        back = -1-i
        if (g1[i] == 'G') and (g2[back] == 'C'):
            bpair = True
        elif (g1[i] == 'C') and (g2[back] == 'G'):
            bpair = True
        elif (g1[i] == 'A') and (g2[back] == 'T'):
            bpair = True
        elif (g1[i] == 'T') and (g2[back] == 'A'):
            bpair = True
        # if cannot pair, return False immediately
        else:
            bpair = False
            return bpair
    # if lengths are different, then False
    if(len(g1) != len(g2)):
        bpair = False
    # if can pair, return True
    return bpair


def zip_length(gene3):
    '''(str) -> int
    Takes in a string representing a gene, and returns the maximum number of
    nucleotide pairs that this gene can zip. Zipping happens when the
    nucleotides at either end of a gene form a pair bond, which may in turn
    allow the next nucleotides in from those genes to bond. This process
    continues until a pair of nucleotides do not form a bond.
    REQ: The input should be a string representing genes.
    >>> zip_length('AGTCTCGCT')
    2
    >>> zip_length('TCAGTACTGA')
    5
    >>> zip_length('TCAGTACTGC')
    0
    '''
    # create a integer for counting pairs
    l = 0
    # check the pairs in the gene
    half = int(len(gene3)/2)
    for i in range(half):
        back = -1-i
        if (gene3[i] == 'G') and (gene3[back] == 'C'):
            l = l + 1
        elif (gene3[i] == 'C') and (gene3[back] == 'G'):
            l = l + 1
        elif (gene3[i] == 'A') and (gene3[back] == 'T'):
            l = l + 1
        elif (gene3[i] == 'T') and (gene3[back] == 'A'):
            l = l + 1
        # if cannot pair, return the number found immediately
        else:
            return l
    # return the zip length
    return l


def splice_gene(source, dest, startan, endan):
    '''(list, list, str, str) -> NoneType
    Takes 2 list representations of genes (each element of the list will
    contain a single character string representing one nucleotide) which we
    will call source and destination (in that order) along with a string
    representing the start and end anchor strings. Splices the subsequence of
    source between the anchor strings into destination between the anchor
    strings. If an anchor occurs more than once in a string, the first and
    shortest sequence should be used. If the anchors do not appear in order in
    both strings, no changes should be made to the genes.
    REQ: source and dest are lists representing genes, startan and endan are
    strings representing start and end anchors.
    >>> splice_gene(['x', 'x', 'T', 'G', 'x', 'y', 'z', 'C', 'A', 'C', 'a',\
    'a', 'a', 'G', 'T', 'a', 'a'], ['o', 'o', 'A', 'C', '.', '.', '.', '.',\
    '.', '.', '.', '.', '.', 'G', 'T', 'o', 'o'], 'AC', 'GT')
    '''
    # create a series of bool values to show how anchors exist in the source
    # and the destination
    sourcefrontok = None
    sourcebackok = None
    destfrontok = None
    destbackok = None
    sourceok = None
    destok = None
    # convert the source and the destination into strings
    sourcestr = ''.join(source)
    deststr = ''.join(dest)
    # get the length of the source and the destination
    sourcelen = len(sourcestr)
    destlen = len(deststr)
    # get reversed start anchor and reversed end anchor
    revstartan = startan[::-1]
    revendan = endan[::-1]
    # check if the source has both anchors
    if((startan in sourcestr) and (endan in sourcestr)):
        # get the index of the beginning of the subsequence that will be
        # spliced
        sstartind1 = sourcestr.find(startan)
        # check if the end anchor is after the start anchor
        if(endan in sourcestr[(sstartind1 + len(startan)):sourcelen]):
            # get the index of the end of the subsequence that will be spliced
            sendind1 = sourcestr[(sstartind1 + len(startan)):sourcelen].\
                find(endan) + len(endan) + sstartind1 + len(startan)
            # we can find the subsequence when reading the source from left to
            # right
            sourcefrontok = True
        else:
            # we cannot find the subsequence when reading the source from left
            # to right
            sourcefrontok = False
    # check if the source has both reversed anchors
    if((revstartan in sourcestr) and (revendan in sourcestr)):
        # get the index of the beginning of the subsequence that will be
        # spliced
        sstartind2 = sourcestr.find(revendan)
        # check if the reversed start anchor is after the reversed end anchor
        if(revstartan in sourcestr[(sstartind2 + len(startan)):sourcelen]):
            # get the index of the end of the subsequence that will be spliced
            sendind2 = sourcestr[(sstartind2 + len(startan)):sourcelen].\
                find(revstartan) + len(revstartan) + sstartind2 + len(startan)
            # we can find the subsequence when reading the source from right to
            # left
            sourcebackok = True
        else:
            # we cannot find the subsequence when reading the source from right
            # to left
            sourcebackok = False
    # check if we can find the subsequence when reading the source from both
    # left to right and right to left
    if(sourcefrontok and sourcebackok):
        # if the beginning of the positive subsequence is before the beginning
        # of the negative subsequence
        if(sstartind1 <= sstartind2):
            # source is ok
            sourceok = True
            # the positive subsequence will be spliced
            sourcepos = True
            # get the string of spliced subsequence
            sourceout = sourcestr[sstartind1:sendind1]
            # get the string of the source after being spliced
            sourceleft = sourcestr[0:sstartind1] +\
                sourcestr[sendind1:sourcelen]
        # if the beginning of the negative subsequence is before the beginning
        # of the positive subsequence
        elif(sstartind1 > sstartind2):
            # source is ok
            sourceok = True
            # the negative subsequence will be spliced
            sourcepos = False
            # get the string of spliced subsequence
            sourceout = sourcestr[sstartind2:sendind2]
            # get the string of the source after being spliced
            sourceleft = sourcestr[0:sstartind2] +\
                sourcestr[sendind2:sourcelen]
    # check if we can find the subsequence only when reading the source from
    # left to right
    elif(sourcefrontok):
        # source is ok
        sourceok = True
        # the positive subsequence will be spliced
        sourcepos = True
        # get the string of spliced subsequence
        sourceout = sourcestr[sstartind1:sendind1]
        # get the string of the source after being spliced
        sourceleft = sourcestr[0:sstartind1] +\
            sourcestr[sendind1:sourcelen]
    # check if we can find the subsequence only when reading the source from
    # right to left
    elif(sourcebackok):
        # source is ok
        sourceok = True
        # the negative subsequence will be spliced
        sourcepos = False
        # get the string of spliced subsequence
        sourceout = sourcestr[sstartind2:sendind2]
        # get the string of the source after being spliced
        sourceleft = sourcestr[0:sstartind2] +\
            sourcestr[sendind2:sourcelen]
    # check if the destination has both anchors
    if((startan in deststr) and (endan in deststr)):
        # get the index of the beginning of the subsequence that will be
        # spliced
        dstartind1 = deststr.find(startan)
        # check if the end anchor is after the start anchor
        if(endan in deststr[(dstartind1 + len(startan)):destlen]):
            # get the index of the end of the subsequence that will be spliced
            dendind1 = deststr[(dstartind1 + len(startan)):destlen].\
                find(endan) + len(endan) + dstartind1 + len(startan)
            # we can find the subsequence when reading the destination from
            # left to right
            destfrontok = True
        else:
            # we cannot find the subsequence when reading the destination from
            # left to right
            destfrontok = False
    # check if the destination has both reversed anchors
    if((revstartan in deststr) and (revendan in deststr)):
        # get the index of the beginning of the subsequence that will be
        # spliced
        dstartind2 = deststr.find(revendan)
        # check if the reversed start anchor is after the reversed end anchor
        if(revstartan in deststr[(dstartind2 + len(startan)):destlen]):
            # get the index of the end of the subsequence that will be spliced
            dendind2 = deststr[(dstartind2 + len(startan)):destlen].\
                find(revstartan) + len(revstartan) + dstartind2 + len(startan)
            # we can find the subsequence when reading the destination from
            # right to left
            destbackok = True
        else:
            # we cannot find the subsequence when reading the destination from
            # right to left
            destbackok = False
    # check if we can find the subsequence when reading the destination from
    # both left to right and right to left
    if(destfrontok and destbackok):
        # if the beginning of the positive subsequence is before the beginning
        # of the negative subsequence
        if(dstartind1 <= dstartind2):
            # destination is ok
            destok = True
            # the positive subsequence will be spliced
            destpos = True
            # get the part of destination before the subsequence
            dest1 = deststr[0:dstartind1]
            # get the part of destination after the subsequence
            dest2 = deststr[dendind1:destlen]
        # if the beginning of the negative subsequence is before the beginning
        # of the positive subsequence
        elif(dstartind1 > dstartind2):
            # destination is ok
            destok = True
            # the negative subsequence will be spliced
            destpos = False
            # get the part of destination before the subsequence
            dest1 = deststr[0:dstartind2]
            # get the part of destination after the subsequence
            dest2 = deststr[dendind2:destlen]
    # check if we can find the subsequence only when reading the destination
    # from left to right
    elif(destfrontok):
        # destination is ok
        destok = True
        # the positive subsequence will be spliced
        destpos = True
        # get the part of destination before the subsequence
        dest1 = deststr[0:dstartind1]
        # get the part of destination after the subsequence
        dest2 = deststr[dendind1:destlen]
    # check if we can find the subsequence only when reading the destination
    # from right to left
    elif(destbackok):
        # destination is ok
        destok = True
        # the negative subsequence will be spliced
        destpos = False
        # get the part of destination before the subsequence
        dest1 = deststr[0:dstartind2]
        # get the part of destination after the subsequence
        dest2 = deststr[dendind2:destlen]
    # if the source and the destination are both ok
    if(sourceok and destok):
        # convert the string of the source after being spliced, to a list
        sleftlist = list(sourceleft)
        # mutate the source list. Let it equal our new list
        source[:] = sleftlist
        # if the positive subsequences are spliced from both the source and the
        # destination, or the negative subsequences are spliced from both the
        # source and the destination
        if(sourcepos == destpos):
            # the string of the new destination consists of the part before the
            # subsequence in the original destination, the subsequence spliced
            # from the source, and the part after the subsequence in the
            # original destination
            deststr = dest1 + sourceout + dest2
        # if positive from source and negative from destination, or negative
        # from source and positive from destination
        else:
            # the string of the new destination consists of the part before the
            # subsequence in the original destination, the reversed subsequence
            # spliced from the source, and the part after the subsequence in
            # the original destination
            deststr = dest1 + sourceout[::-1] + dest2
        # mutate the destination list. Let it equal the list form of the string
        # of the new destination
        dest[:] = list(deststr)


def match_mask(gene4, mask1):
    '''(str, str) -> int
    Takes in a string representation of a gene and a mask and returns the index
    of the first nucleotide in the sequence that is matched by the mask. (If
    the mask matches multiple sequences, return the one with the lowest index)
    or -1 if the mask does not match anywhere in the gene.
    REQ: gene4 is a string representing a gene.
    REQ: mask1 is a string representing a mask.
    >>> match_mask('TTATCAATTACT', 'A[AG]T')
    0
    '''
    # use the write() to get a list and check the pairing
    # to be continued


def write(m):
    '''(str) -> list
    Takes in a string representation of a mask and return a list to show how
    the mask can expand.
    REQ: m is a string representation of a mask.
    >>> write('A[AG]T')
    ['A', 'AG', 'T']
    '''
    new = []
    i = 0
    ind = 0
    while(0 <= i <len(m)):
        if(m[i] == '['):
            while((ind < len(m)) and (m[ind] != ']')):
                ind = ind + 1
            new.append(m[i+1:ind])
            i = i + ind
            ind = ind + 1
        elif(m[i].isdigit()):
            if(m[i-1] == ']'):
                for a in range(0, len(m[i])):
                    new.append(new[-1])
                i = i + 1
            else:
                for a in range(0, len(m[i])):
                    new.append(m[i-1])
                i = i + 1
        elif(m[i] == '*'):
            new.append('*')
            i = i + 1
        else:
            new.append(m[i])
            i = i + 1
    return new


def process_gene_file(file_h, gene5, mask2):
    '''(io.TextIOWrapper, str, str) -> tuple
    Takes in a file handle for a file containing one gene per line, a string
    representing a gene and a string representing a mask. Returns a tuple
    (p, m, z) where p equals the first gene that can pair with the input gene
    string, m equals the first gene that matches the mask, and z equals the
    longest gene zip found up in any gene up to and including the point where
    both p and m were found. If no genes match the given gene or mask, -1 is
    returned in place of p or m.
    REQ: file_h is a file handle for a file containing one gene per line.
    REQ: gene5 is a string representing a gene.
    REQ: mask2 is a string representing a mask.
    '''
