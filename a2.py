"""CSCA08 Assignment 2, Fall 2017
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
 Date: 2017/11/20
"""


class valueerror(Exception):
    '''An error to raise when any value is wrong'''


class keyerror(Exception):
    '''An error to raise when any key is wrong'''


class typeerror(Exception):
    '''An error to raise when any type is wrong'''


class Client():
    '''A class to represent a client'''
    def __init__(self, iden):
        '''(Client, str) -> NoneType
        Initialize a Client object.
        REQ: iden is a string of numbers, representing a client's ID.
        '''
        # raise errors
        if(type(iden) != str):
            raise typeerror('The ID should be a string of numbers')
        # if no error, create some default variables
        else:
            self._id = iden
            self._pairtopostogene = {}
            self._markertopairtopos = {}
            self._markertogene = {}

    def __str__(self):
        '''(Client) -> str
        Return a string representation of a Client object.
        '''
        # create a new string
        self._str = 'I am a Client'
        # return the string
        return self._str

    def set_by_pos(self, pair, pos, gene):
        '''(Client, int, int, str) -> NoneType
        Set a pair of nucleotides given the pair and position.
        REQ: pair is an int. 0<=pair<=22.
        REQ: pos is an int. pos>=0.
        REQ: gene is a string representing a pair of nucleotides.
        '''
        # raise errors
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if(type(pos) != int):
            raise typeerror('The position number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        if(pos < 0):
            raise valueerror('The position number should be >= 0')
        if(type(gene) != str):
            raise typeerror('The nucleotides should be a string')
        if(len(gene) != 2):
            raise valueerror('The nucleotides should have a length of 2')
        # if no error
        else:
            # if the pair has been set
            if(pair in self._pairtopostogene):
                # update the nucleotides
                self._pairtopostogene[pair][pos] = gene
            # if the pair is new
            else:
                # set the nucleotides
                self._pairtopostogene[pair] = {pos: gene}

    def set_marker(self, marker, pair, pos):
        '''(Client, str, int, int) -> NoneType
        Set a marker given the pair and position.
        REQ: pair is an int. 0<=pair<=22.
        REQ: pos is an int. pos>=0.
        REQ: marker is a string representing a marker.
        '''
        # raise errors
        if(type(marker) != str):
            raise typeerror('The marker should be a string')
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if(type(pos) != int):
            raise typeerror('The position number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        if(pos < 0):
            raise valueerror('The position number should be >= 0')
        # if no error
        else:
            # set the marker to the given position
            self._markertopairtopos[marker] = [pair, pos]

    def set_by_marker(self, marker, gene):
        '''(Client, str, str) -> NoneType
        Set a pair of nucleotides given a marker.
        REQ: marker is a string representing a marker.
        REQ: gene is a string representing a pair of nucleotides.
        '''
        # raise errors
        if(type(marker) != str):
            raise typeerror('The marker should be a string')
        if(marker not in self._markertopairtopos):
            raise keyerror('The marker has not been defined')
        if(type(gene) != str):
            raise typeerror('The nucleotides should be a string')
        if(len(gene) != 2):
            raise valueerror('The nucleotides should have a length of 2')
        # if no error
        else:
            # set the pair of nucleotides to the marker
            self._markertogene[marker] = gene
            # get the position that the marker was set to
            [pair, pos] = self._markertopairtopos[marker]
            # if the pair has been set
            if(pair in self._pairtopostogene):
                # update the nucleotides
                self._pairtopostogene[pair][pos] = gene
            # if the pair is new
            else:
                # set the nucleotides
                self._pairtopostogene[pair] = {pos: gene}

    def get_by_pos(self, pair, pos):
        '''(Client, int, int) -> str
        Get a pair of nucleotides given the pair and position.
        REQ: pair is an int. 0<=pair<=22.
        REQ: pos is an int. pos>=0.
        '''
        # raise errors
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if(type(pos) != int):
            raise typeerror('The position number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        if(pos < 0):
            raise valueerror('The position number should be >= 0')
        if(pair not in self._pairtopostogene):
            raise keyerror('The pair has not been defined')
        elif(pos not in self._pairtopostogene[pair]):
            raise keyerror('The position has not been defined')
        # if no error
        else:
            # return the pair of nucleotides
            return self._pairtopostogene[pair][pos]

    def get_by_marker(self, marker):
        '''(Client, str) -> str
        Get a pair of nucleotides given a marker.
        REQ: marker is a string representing a marker.
        '''
        # raise errors
        if(type(marker) != str):
            raise typeerror('The marker should be a string')
        if(marker not in self._markertopairtopos):
            raise keyerror('The marker has not been defined')
        if(marker not in self._markertogene):
            raise keyerror('No gene has been set to this marker')
        # if no error
        else:
            # return the pair of nucleotides
            return self._markertogene[marker]

    def get_chromosome(self, pair):
        '''(Client, int) -> Chromosome
        Get a chromosome given the pair.
        REQ: pair is an int. 0<=pair<=22.
        '''
        # raise errors
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        # if no error
        else:
            # if the pair is new
            if(pair not in self._pairtopostogene):
                # create a new chromosome
                self._pairtopostogene[pair] = {}
            # let the chromosome be a new variable
            chro = Chromosome(self._pairtopostogene, pair)
            # return the chromosome
            return chro

    def set_chromosome(self, pair, chro):
        '''(Client, int, Chromosome) -> NoneType
        Set a chromosome to a client given the pair and chromosome.
        REQ: pair is an int. 0<=pair<=22.
        REQ: chro is an object of Chromosome.
        '''
        # raise errors
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        # if no error
        else:
            # set the chromosome to the given pair
            self._pairtopostogene[pair] = chro._dic

    def test(self, q):
        '''(Client, Query) -> bool
        Return the result of a query given a client and a Query object.
        REQ: q is a Query object.
        '''
        # create default variables
        result = True
        i = 0
        # list of the pairs of the client
        self._pairlist = list(self._pairtopostogene.keys())
        # list of the pairs of the Query object
        q._pairlist = list(q._pairtopostogene.keys())
        # while checking the Query pair list and the query is not rejected
        while((i < len(q._pairlist)) and (result is True)):
            # for every pair in the list
            for pair in q._pairlist:
                # if comparing against a male sex chromosome
                if((self._gender == 'male') and (pair == 22)):
                    # reject the query
                    result = False
                # if the client also has the pair
                elif(pair in self._pairlist):
                    # get lists of positions of both client and Query object
                    self._poslist = list(self._pairtopostogene[pair].keys())
                    q._poslist = list(q._pairtopostogene[pair].keys())
                    # for every position of this pair of the Query object
                    for pos in q._poslist:
                        # if this pair of the client also has this position
                        if pos in self._poslist:
                            # get the nucleotides in this position from both
                            selfgene = self._pairtopostogene[pair][pos]
                            qgene = q._pairtopostogene[pair][pos]
                            # if the nucleotides are the same
                            if(selfgene == qgene):
                                # result does not change
                                result = result
                            # if the nucleotides have any memory nucleotide
                            elif(qgene[0].isdigit() or qgene[1].isdigit()):
                                # for each of the pair of nucleotides
                                for ind in [0, 1]:
                                    # if it is a memory nucleotide
                                    if(qgene[ind].isdigit()):
                                        # if it has been set
                                        if(qgene[ind] in q._memtogene):
                                            # if it equals the previous value
                                            if(selfgene[ind] ==
                                               q._memtogene[qgene[ind]]):
                                                # result does not change
                                                result = result
                                            # if it does not equal that
                                            else:
                                                # the query is rejected
                                                result = False
                                        # if it is new
                                        else:
                                            # set the memory nucleotide
                                            q._memtogene[qgene[ind]] =\
                                                selfgene[ind]
                                            # result does not change
                                            result = result
                                    # if it is a normal nucleotide
                                    else:
                                        # if it equals the one in the client
                                        if(selfgene[ind] == qgene[ind]):
                                            # result does not change
                                            result = result
                                        # if it does not equal that
                                        else:
                                            # the query is rejected
                                            result = False
                            # if the normal nucleotides cannot pass
                            else:
                                # the query is rejected
                                result = False
                        # if unknown position
                        else:
                            # result does not change
                            result = result
                # if unknown pair
                else:
                    # result does not change
                    result = result
            # next pair in Query pair list
            i = i + 1
        # return the query result
        return result


class Query(Client):
    '''A class to represent a query'''
    def __init__(self):
        '''(Query) -> NoneType
        Initialize a query.
        '''
        # create some default variables
        self._pairtopostogene = {}
        self._markertopairtopos = {}
        self._markertogene = {}
        self._memtogene = {}

    def __str__(self):
        '''(Query) -> str
        Return a string representation of a Query object.
        '''
        # create a new string
        self._str = 'I am a Query'
        # return the string
        return self._str


class Chromosome(Client):
    '''A class to represent a chromosome'''
    def __init__(self, dic, pair):
        '''(Chromosome, dict, int) -> NoneType
        Initialize a chromosome given a dict and a key.
        '''
        # create a default dict
        self._dic = dic[pair]

    def __str__(self):
        '''(Chromosome) -> str
        Return a string representation of a Chromosome object.
        '''
        # create a new string
        self._str = 'I am a Chromosome'
        # return the string
        return self._str

    def set_by_pos(self, pos, gene):
        '''(Chromosome, int, str) -> NoneType
        Set a pair of nucleotides given the position.
        REQ: pos is an int. pos>=1.
        REQ: gene is a string representing a pair of nucleotides.
        '''
        # raise errors
        if(type(pos) != int):
            raise typeerror('The position number should be an int')
        if(pos < 0):
            raise valueerror('The position number should be >= 0')
        if(type(gene) != str):
            raise typeerror('The nucleotides should be a string')
        if(len(gene) != 2):
            raise valueerror('The nucleotides should have a length of 2')
        # if no error
        else:
            # set the pair of nucleotides to the dict
            self._dic[pos] = gene


class Male(Client):
    '''A class to represent a male client'''
    def __init__(self, iden):
        '''(Male, str) -> NoneType
        Initialize a male client given his id.
        '''
        # call the parent method
        Client.__init__(self, iden)
        # create a gender variable
        self._gender = 'male'

    def __str__(self):
        '''(Male) -> str
        Return a string representation of a Male object.
        '''
        # create a new string
        self._str = 'I am a Male'
        # return the string
        return self._str


class Female(Client):
    '''A class to represent a female client'''
    def __init__(self, iden):
        '''(Female, str) -> NoneType
        Initialize a female client given her id.
        '''
        # call the parent method
        Client.__init__(self, iden)
        # create a gender variable
        self._gender = 'female'

    def __str__(self):
        '''(Female) -> str
        Return a string representation of a Female object.
        '''
        # create a new string
        self._str = 'I am a Female'
        # return the string
        return self._str

    def procreate(self, father, binder):
        '''(Female, Male, Binder) -> Male
        Or (Female, Male, Binder) -> Female
        Produce offspring given father and a binding way.
        REQ: father is a Male object
        REQ: binder is a Binder object
        '''
        # raise the error
        if(binder._gender is None):
            raise valueerror('The gender of the offsping is unknown')
        # if no error
        else:
            # set the id of the offspring
            self._childid = self._id + father._id
            # if the binder is male
            if(binder._gender == 'male'):
                # the offspring is male
                child = Male(self._childid)
            # if the binder is female
            elif(binder._gender == 'female'):
                # the offspring is female
                child = Female(self._childid)
            # for every pair in the binder
            for pair in binder._pairtopostoway:
                # if mother and father both have this pair
                if((pair in self._pairtopostogene) and
                   (pair in father._pairtopostogene)):
                    # for every position in this pair
                    for pos in binder._pairtopostoway[pair]:
                        # if mother and father both have this position
                        if((pos in self._pairtopostogene[pair]) and
                           (pos in father._pairtopostogene[pair])):
                            # if the binder is left-maternal
                            if(binder._pairtopostoway[pair][pos] == 'LM'):
                                # get the nucleotides from mother and father
                                gene = self._pairtopostogene[pair][pos][0] +\
                                    father._pairtopostogene[pair][pos][1]
                                # if this pair has been set
                                if(pair in child._pairtopostogene):
                                    # update the nucleotides
                                    child._pairtopostogene[pair][pos] = gene
                                # if this pair is new
                                else:
                                    # set the nucleotides
                                    child._pairtopostogene[pair] = {pos: gene}
                            # if the binder is right-maternal
                            elif(binder._pairtopostoway[pair][pos] == 'RM'):
                                # get the nucleotides from mother and father
                                gene = father._pairtopostogene[pair][pos][0] +\
                                    self._pairtopostogene[pair][pos][1]
                                # if this pair has been set
                                if(pair in child._pairtopostogene):
                                    # update the nucleotides
                                    child._pairtopostogene[pair][pos] = gene
                                # if this pair is new
                                else:
                                    # set the nucleotides
                                    child._pairtopostogene[pair] = {pos: gene}
        # return the offspring
        return child


class Binder(Client):
    '''A class to represent a binding way'''
    def __init__(self):
        '''(Binder) -> NoneType
        Initialize a Binder.
        '''
        # set some default variables
        self._gender = None
        self._pairtopostoway = {}

    def __str__(self):
        '''(Binder) -> str
        Return a string representation of a Binder object.
        '''
        # create a new string
        self._str = 'I am a Binder'
        # return the string
        return self._str

    def set_by_pos(self, pair, pos, way):
        '''(Binder, int, int, str) -> NoneType
        Set a binding way given the pair and position.
        REQ: pair is an int. 0<=pair<=22.
        REQ: pos is an int. pos>=0.
        REQ: way is a string 'LM' or 'RM', representing left or right-maternal.
        '''
        # raise errors
        if(type(pair) != int):
            raise typeerror('The pair number should be an int')
        if(type(pos) != int):
            raise typeerror('The position number should be an int')
        if((pair > 22) or (pair < 0)):
            raise valueerror('Humans have 23 pairs of chromosomes from 0 ' +
                             'to 22')
        if(pos < 0):
            raise valueerror('The position number should be >= 0')
        if(type(way) != str):
            raise typeerror('The binding way should be a string')
        if(way != 'LM' and way != 'RM'):
            raise valueerror('The binding way is invalid, it should be LM or' +
                             ' RM')
        # if no error
        else:
            # if the pair has been set
            if(pair in self._pairtopostoway):
                # update the binding way
                self._pairtopostoway[pair][pos] = way
            # if the pair is new
            else:
                # set the binding way
                self._pairtopostoway[pair] = {pos: way}

    def set_sex(self, gender):
        '''(Binder, str) -> NoneType
        Set the sex of the offspring given the sex.
        REQ: gender is a string, M or F, to represent sex.
        '''
        # raise errors
        if(gender != 'M' and gender != 'F'):
            raise valueerror('The sex is invalid, it should be M or F')
        # if no error
        else:
            # if the sex is M
            if(gender == 'M'):
                # the offspring is male
                self._gender = 'male'
            # if the sex is F
            elif(gender == 'F'):
                # the offspring is female
                self._gender = 'female'
