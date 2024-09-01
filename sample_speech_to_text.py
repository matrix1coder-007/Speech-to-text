import os
import pyttsx3

# max attempts allowed for trials
MAX_TRIAL_ATTEMPTS = 3  

# folder location
TEST_CWD = os.getcwd()

# test_dataset
TEST_DATASET_FOLDER_LOC = os.path.join('input_data', 'test_dataset_samples') # first-level folder
TEST_SAMPLE_FILE_LOC = os.path.join(TEST_DATASET_FOLDER_LOC, 'trial_input.txt')  # second-level folder


# user_input_dataset
USER_INPUT_FOLDER_LOC = os.path.join('input_data', 'user_input_samples') # first-level folder
USER_INPUT_FILE_LOC = os.path.join(USER_INPUT_FOLDER_LOC, 'user_input.txt')  # second-level folder



# class
class Class_Speech_to_Text:

    def __init__(self):
        """
        Description: Create folders required to test trial samples and/or input samples 
            by calling helper functions.
        Arguments: -
        Returns:   -     
        """


        # folder creation segment
        print('Folder creation initiation and completion defines a True/False value.\n Sample messages:')
        print('SUCCESS:--> SUCCESS: Folder creation: {folder-name}')
        print('FAILURE:--> FAILURE: Folder creation: {folder-name}')
        
        INPUT_DATA_NAME = 'input_data'        
        self.create_folder_location(TEST_CWD, INPUT_DATA_NAME)

        TEST_DATASET_SAMPLES_NAME = 'test_dataset_samples'
        self.create_folder_location(TEST_DATASET_FOLDER_LOC, TEST_DATASET_SAMPLES_NAME)
        
        USER_INPUT_SAMPLES_NAME = 'user_input_samples'
        self.create_folder_location(TEST_DATASET_FOLDER_LOC, USER_INPUT_SAMPLES_NAME)



        # take trial or continue choice
        print('Are you a new user? You have 2 choices on how to proceed: ')
        print('1. Do you want to take the trial?')
        print('2. Do you want to continue without the trial?')

        choice_to_proceed = 0
        while choice_to_proceed != 1 or choice_to_proceed != 2:
            choice_to_proceed = int(input('Please enter a valid choice: 1 or 2'))
        
        if choice_to_proceed == 1:
            self.take_trial()
        elif choice_to_proceed == 2:
            self.ask_for_input()
    


    def create_folder_location(folder_location, folder_name) -> None:
        """
        Description: Create folders required to test trial samples and/or input samples.
        Arguments: 
            1. folder_location: os.path()
            2. folder_name: str
        Returns: -     
        """

        # folder creation initiated
        print('Folder creation initiated.', folder_check)

        final_folder_location = os.path.join(folder_location, folder_name)

        folder_outer_creation_trials = 0
        folder_outer_bool = False
        while folder_outer_creation_trials < MAX_TRIAL_ATTEMPTS and not folder_outer_bool:
            try:
                os.makedirs(final_folder_location)
                folder_outer_bool = True
            except FileExistsError:
                print('Folder already exists.', folder_check)
            
            if folder_outer_bool:
                break
            folder_outer_creation_trials += 1



        # folder creation completed
        if folder_outer_bool:
            print('SUCCESS:--> SUCCESS: Folder creation:', folder_check)
        else:
            if folder_outer_creation_trials >= MAX_TRIAL_ATTEMPTS:
                print('FAILURE:--> FAILURE: Folder creation after maximum attempts of {MAX_TRIAL_ATTEMPTS}:', folder_check)
            else:
                print("FAILURE:--> FAILURE: Folder creation couldn't complete maximum attempts of {MAX_TRIAL_ATTEMPTS}:", folder_check)



    def take_trial(self):
        """
        Description: Call this function to state the sample text and play the speech
        Arguments: -
        Returns:   -     
        """

        # sample text played     
        sample_text = "Hi! How are you? I'm fine. Thank you!"
        print('We are beginning the trial now!\nThe sample text is: ', sample_text)
        self.play_speech(sample_text)



    def ask_for_user_input(self):
        """
        Description: Call this function to ask the user input format
        Arguments: -
        Returns:   -     
        """

        # choice of input format    
        print('How do you want to enter the input?: ')
        print('1. Write the input in the text-box?')
        print('2. Take the input from a file?')

        choice_of_input = 0
        while choice_of_input != 1 or choice_of_input != 2:
            choice_of_input = int(input('Please input the choice as 1 or 2.'))
        
        if choice_of_input == 1:
            self.take_user_input()

        elif choice == 2:
            print()
            print('The file for user-input is placed right in the folder named -- input_data --> user_input_samples')

    
    
    def take_user_input(self) -> str:
        """
        Description: Call this function to ask the user input for text-box
        Arguments: -
        Returns:   -     
        """

        # take user input
        input_str = input('Please enter the text: ')
        print('We are beginning the speech conversion now!') 
        self.play_speech(input_str)

    

    def play_speech(self, input_text):
        """
        Description: Call this function to ask the user input format
        Arguments: 
            1. input_text: str
        Returns:   -     
        """

        speech_to_text_engine = pyttsx3.init()
        speech_to_text_engine.say(input_text)

        speech_to_text_engine.runAndWait()





