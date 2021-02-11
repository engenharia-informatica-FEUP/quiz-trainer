import json
import os


def has_correct(dic: dict) -> dict:
    """
    ## @brief   - This function checks if a dict has a key 'correct' in any depth and returns it. If it has no 'correct' key returns an empty dict 
    #  @param   - A dict representing one question option
    #  @return  - {} or {'correct': boolean}
    """

    #Iterates through the fields inside a question (there might be only one field depending on the question type) and checks recursively if there is any 'correct' parameter
    for val in dic:
        if type(dic[val]) == dict:
            has_correct(dic[val])
        else:
            if val == 'correct':    #If we find a 'correct' value, we send return the dict {'correct': boolean} directly and end the function call
                return {val:dic[val]}   
    return {}   #If, at the end of the brute force recursion we haven't found a 'correct' parameter, we return an empty dict representing the lack of the wanted parameter



def flatten(lst: list) -> list:
    """
    ## @brief   - This function parsed the 'answers' field into a list of dicts, which are either empty or contain a correct parameter
    #  @param   - The key of 'answers' field
    #  @return  - A list of dictionaries
    """

    res = []    #Initializes a list to store each question parsing

    for el in lst:
        if type(el) == dict:    #If the list element is a dict, calls an auxiliar function, which will parse it and check if it was a 'correct' parameter
            res.append(has_correct(el))
        #REMOVABLE:
        else:   #This condition is, at the moment irrelevant, but basically controls if there is a 'correct field' in the 'questions' 1st layer
            res.append({})  
    
    return res



def parser(filepath):
    """
    ## @brief   - This function parses a .json file to the format needed (a list of sublist, where each sublist represents a different question)
    #  @param   - A string containing the relative path of the .json file
    #  @return  - A list of sublists
    """

    #Opens the file and gets online the 'questions' field
    with open(file) as configs:
        quizz_configs = json.load(configs)['questions']

    #Initializes a list to store the final parsed result
    res = []

    for dic in quizz_configs:
        for param in dic: 
            if param == 'answers':  #Ignores every parameter with exception of 'answers'
                res.append(flatten(dic[param]))

    return res



#------------Function call------------#

if __name__ == "__main__":
    #input the relative path of the json file you want to parse in here
    file = os.path.expanduser("quiz.json")  


    print(parser(file))
