"""CSCA08 Assignment 0, Fall 2017
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
 Date: 2017/10/15
"""


def split_input(DNA):
    '''(str) -> list
    Take in a DNA sequence and return a list with three elements, the upstream
    data, the gene (if any is found, or an empty string if no gene is found),
    and the downstream data, in that order.
    REQ: DNA is a series of A, G, C, T.
    >>> split_input('ATGAAAAATGAAATGAAATG')
    ['', 'ATGAAAA', 'ATGAAATGAAATG']
    >>> split_input('GGATGGGGG')
    ['GG', 'ATGGGGG', '']
    >>> split_input('ATGCCCC')
    ['', 'ATGCCCC', '']
    >>> split_input('TTATGTTTTATGTTATGTTATG')
    ['TT', 'ATGTTTT', 'ATGTTATGTTATG']
    >>> split_input('AAAAAA')
    ['AAAAAA', '', '']
    '''
    # create a list
    newlist = []
    # check how many "ATG"s the DNA sequence has and create corresponding lists
    if(DNA.count("ATG") == 0):
        newlist = [DNA, '', '']
    elif(DNA.count("ATG") == 1):
        newlist = [DNA[0:DNA.find("ATG")], DNA[DNA.find("ATG"):len(DNA)], '']
    else:
        newlist = [DNA[0:DNA.find("ATG")],
                   DNA[DNA.find("ATG"):DNA.find("ATG", DNA.find("ATG")+3)],
                   DNA[DNA.find("ATG", DNA.find("ATG")+3):len(DNA)]]
    # return the list
    return newlist


def get_gene(DNA):
    '''(str) -> str
    Take in a DNA sequence and returns a string representation of the gene if
    one is present, or the string ERROR if no gene is present.
    REQ: DNA is a series of A, G, C, T.
    >>> get_gene('ATGAAAAATGAAATGAAATG')
    'ATGAAAA'
    >>> get_gene('AAAAAA')
    'ERROR'
    '''
    # create a new string
    newstr = ""
    # check how many "ATG"s the DNA sequence has and return corresponding gene
    if(DNA.count("ATG") == 0):
        newstr = "ERROR"
    elif(DNA.count("ATG") == 1):
        newstr = DNA[DNA.find("ATG"):len(DNA)]
    else:
        newstr = DNA[DNA.find("ATG"):DNA.find("ATG", DNA.find("ATG")+3)]
    # return the string
    return newstr


def validate_gene(gene):
    '''(str) -> bool
    Take in a string representation of a gene, and returns True iff the gene
    presented is valid.
    REQ: gene is a series of A, G, C, T.
    >>> validate_gene('ATGAAA')
    True
    >>> validate_gene('ATGAAAA')
    False
    >>> validate_gene('ATGAA')
    False
    '''
    # create a boolean value
    valid = None
    # It must start with the start codon (3 character sequence) ATG
    valid = "ATG" == gene[0:3]
    # must contain at least one codon after the start codon
    valid = valid and (len(gene)-3 >= 3)
    # It must contain only full codons (i.e., it cannot end mid-way through a 3
    # character codon)
    valid = valid and ((len(gene)-3) % 3 == 0)
    # It must never contain four consecutive identical nucleotides
    valid = valid and gene.count('AAAA') == gene.count('GGGG') ==\
        gene.count('CCCC') == gene.count('TTTT') == 0
    # return the boolean value
    return valid


def is_palindromic(gene):
    '''(str) -> bool
    Take a string representation of a gene, and returns True iff that gene is
    palindromic (reads the same forwards as backwards).
    REQ: gene is a series of A, G, C, T.
    >>> is_palindromic('ATGGTA')
    True
    >>> is_palindromic('ATGAAA')
    False
    '''
    # create a boolean value
    pal = None
    # check if the gene is palindromic or not
    if(gene == gene[::-1]):
        pal = True
    else:
        pal = False
    # return the boolean value
    return pal


def evaluate_sequence(DNA):
    '''(str) -> str
    Takes in a DNA sequence (as described above) and returns one of the
    follow-ing strings as appropriate: {No Gene Found, Invalid Gene, Valid Gene
    Found, Valid Palindromic Gene Found}.
    REQ: DNA is a series of A, G, C, T.
    >>> evaluate_sequence('AAA')
    'No Gene Found'
    >>> evaluate_sequence('GGATGGGGG')
    'Invalid Gene'
    >>> evaluate_sequence('ATGCCC')
    'Valid Gene Found'
    >>> evaluate_sequence('ATGGTA')
    'Valid Palindromic Gene Found'
    '''
    # create a new string
    new_str = ""
    # split gene from the DNA sequence
    gene = split_input(DNA)[1]
    # check if the DNA has gene or not
    if(gene == ''):
        new_str = "No Gene Found"
    # if the DNA has gene but the gene is invalid
    elif((gene != '') and (not validate_gene(gene))):
        new_str = "Invalid Gene"
    # if the DNA has gene and the gene is valid but not palindromic
    elif((gene != '') and validate_gene(gene) and (not is_palindromic(gene))):
        new_str = "Valid Gene Found"
    # if the DNA has gene and the gene is valid and palindromic
    elif((gene != '') and validate_gene(gene) and is_palindromic(gene)):
        new_str = "Valid Palindromic Gene Found"
    # return the string
    return new_str
