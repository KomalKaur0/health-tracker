import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime
# from symptom_class import Symptom

class User:

    def __init__(self, name, symptoms=[], data=None):
        '''
        instantiation for User class

        parameters
        ----------
        name : str
            User's name

        symptoms : list of Symptom objects (optional)
            list of what symptoms this user has logged

        data : Pandas DataFrame (optional)
            table of symptoms where the column 0 is julian dates,
            columns 1-N are symptoms, 
            and entries are intensity on a scale from 0 (none) to 5 (severe)

        returns
        ----------
        None
        '''

        self.name = name

        # checking valid data type for symptoms list and data
        assert all(isinstance(symp, str) for symp in symptoms)
        
        self.symptoms = symptoms
            
        assert isinstance(data, pd.DataFrame)

        self.data = data
        
    def pull_data(self, datapath):
        '''
        pull data from the user's datafile and update user's symptoms

        parameters
        ----------
        datapath : str
            pathname to the data table such that column 0 is julian dates,
            columns 1-N are symptoms, 
            and entries are intensity on a scale from 0 (none) to 5 (severe)

        returns
        ----------
        None
        '''

        # warnings for invalid datapaths
        if os.path.exists(datapath):
            current_symptoms = [symp.name for symp in self.symptoms]
            self.data = pd.read_csv(datapath)

            # update symptoms for new ones
            for symp in self.data.columns:
                if symp not in current_symptoms:
                    self.symptoms.append(symp)
        else:
            print('invalid datapath, could not pull user data')

    def corr(self, symp1, symp2):
        '''
        find the correlation between two of the user's symptoms 
        and create a plot of the two together
        '''

        # check that symptoms are valid inputs and exist for the user
        assert symp1, symp2 in self.symptoms

        # get time series data for each symptom
        x = self.data[0]
        y1 = self.data[symp1]
        y2 = self.data[symp2]

        # np.correlate
        correlation = np.correlate(y1, y2)
        print(f'correlation of {symp1} and {symp2} is {correlation}')

        # plot the symptoms vs time
        fig, ax = plt.subplots()
        ax.plot(x, y1, label=symp1)
        ax.plot(x, y2, label=symp2)
        ax.set_title(f'correlation of {symp1} and {symp2} is {correlation}')
        ax.set_xlabel('time')
        ax.set_xticklabels([str(datetime.datetime.strptime(jd, '%y%j').date()) for jd in x])
        ax.set_ylabel('symptom severity')
        fig.legend(loc='best')
        plt.show()

    def plot(self, start=None, end=None):
        '''
        plot of all symptoms in time domain
        '''

        x = self.data[0]

        fig, ax = plt.subplots()
        for symp in self.symptoms:
            y1 = self.data[symp]
            ax.plot(x, y1, label=symp)

        ax.set_title('symptoms vs time')
        ax.set_xlabel('time')
        ax.set_xticklabels([str(datetime.datetime.strptime(jd, '%y%j').date()) for jd in x])
        ax.set_ylabel('symptom severity')
        fig.legend(loc='best')
        plt.show()