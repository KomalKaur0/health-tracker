import pandas as pd
from symptom_class import Symptom

class User:

    def __init__(self, name, symptoms=[], data=None):
        '''
        instantiation for User class

        paramters
        ----------
        name : str
            User's name

        symptoms : list of Symptom objects (optional)
            list of what symptoms this user has logged

        data : Pandas DataFrame (optional)
            table of symptoms where the columns are symptom, 
            rows are date, and entries are intensity on a scale from 0 (none) to 5 (severe)

        returns
        ----------
        None
        '''

        #TODO: implement checking valid data type for symptoms list and data

        self.name = name
        self.symptoms = symptoms
        self.data = data
        
    def pull_data(self, datapath):
        '''
        pull data from the user's datafile

        parameters
        ----------
        datapath : str
            pathname to the data sheet where the columns are symptom, 
            rows are date, and entries are intensity on a scale from 0 (none) to 5 (severe)

        returns
        ----------
        None
        '''

        #TODO: implement warnings for invalid datapaths

        current_symptoms = [symp.name for symp in self.symptoms]
        self.data = pd.read_csv(datapath)

        # update symptoms for new ones
        for symp in self.data.columns:
            if symp not in current_symptoms:
                self.symptoms.append(Symptom(symp))

    def corr(self, symp1, symp2):
        '''
        find the correlation between two of the user's symptoms 
        and create a plot of the two together
        '''

    def plot(self, start=None, end=None):
        '''
        plot of all symptoms in time domain
        '''