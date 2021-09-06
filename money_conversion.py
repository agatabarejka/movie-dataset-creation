import re

### function checks if numerals are present in the value and returns them as integers
def multiply(budget):
    numerals = {'million':1000000, 'thousand':1000, 'billion':1000000000}
    multiply_by = [numeral for numeral in numerals.keys() if numeral in budget]
        
    if multiply_by:
        return numerals[multiply_by[0]]

### function returns a float if money pattern is present in a value
def float_it(amount):
    money = re.findall(r'\$[0-9]+[.,]?\d*[.,]?\d*[.,]?\d*', amount)
    
    if money:
        numbers = [re.sub(r'\$', '', number) for number in money]
        # getting rid of commas to enable making a float later
        no_commas = [re.sub(',', '', amount) for amount in numbers]

        if multiply(amount):
            final = float(no_commas[0]) * multiply(amount)
        else:
            final = float(no_commas[0])
        return final

### function applies conversion to both strings and lists
def money_to_float(budget):
    if type(budget)==str:
        return float_it(budget)
    elif type(budget)==list:
        
        for index, instance in enumerate(budget):
            result = float_it(instance)
            if result: # first occurence in a list is a correct value
                return result
            elif result==None and index==len(budget)-1: # there was no correct budget value
                return None

    else:
        return None