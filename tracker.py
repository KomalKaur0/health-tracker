class User:
    def __init__(self, name, symptoms=[]):
        '''
        instantiation for User class

        paramters
        ----------
        name : str
            User's name

        symptoms : list of Symptom objects

        '''
        self.name = name
        self.symptoms = symptoms

class Symptom:
    def __init__(self, name):
        self.name = name


def corr(symp1, symp2):
    '''
    find the correlation between two symptoms. also create a graph of the two on the same plot

    parameters
    ----------
    symp1 : 
        
    '''