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
            rows are date, and entries are intensity on a scale from 1 to 5

        returns
        ----------
        None
        '''

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
            rows are date, and entries are intensity on a scale from 1 to 5
        '''

        # TODO: implement something that can check if things are up to date
        # TODO: implmenet something to check if the symptoms list matches the dataframe's columns