from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    # list to store results
    resList = []

    # No queries, list all 
    if len(args) == 0:
        return USERS
    
    else:
        keyVals = getKeys(args)
        if 'id' in keyVals:
            # run idSearch
            res = idSearch(args[keyVals['id']], USERS)
            if res != None:
                resList.append(res)
        if 'name' in keyVals:
            # run nameSearch
            res = nameSearch(args[keyVals['name']], USERS)
            if res != None:
                for e in res:
                    if e in resList:
                        continue
                    resList.append(e)
        if 'age' in keyVals:
            # run ageSearch
            res = ageSearch(args[keyVals['age']], USERS)
            if res != None:
                for e in res:
                    if e in resList:
                        continue
                    resList.append(e) 
        if 'occupation' in keyVals:
            # run occSearch
            res = occSearch(args[keyVals['occupation']], USERS)
            if res != None:
                for e in res:
                    if e in resList:
                        continue
                    resList.append(e)
        if len(resList) > 0:
            return resList
        else:
            return 'No entry matches your query! Try again with values in the database\n(Try searching with no query to get whole database)'
        
# function for getting keys in query dict and storing into a key dict, making sure each key
# in the key dict is lower cased and each corresponding value is the key for the query dict       
def getKeys(args):
    k = args.keys()
    loweredK = {}
    for e in k:
        loweredK[e.lower()] = e
    return loweredK

# function for searching by ID, parameter (n) is str only, parameter (data) is list of 
# user dicts
def idSearch(n, data):
    for e in data:
        if e['id'] == n:
            return e
    return None

# function for searching by name, parameter (s) is str only, parameter (data) is list of
# user dicts
def nameSearch(s, data):
    resList = []
    for e in data:
        if s.lower() in e['name'].lower():
            resList.append(e)
    if len(resList) == 0:
        return None
    return resList

# function for searching by age, parameter (n) is str only, parameter (data) is list of
# user dicts
def ageSearch(n, data):
    resList = []
    ageRange = [int(n) - 1, int(n), int(n) + 1]
    for e in data:
        if e['age'] in ageRange:
            resList.append(e)
    if len(resList) == 0:
        return None
    return resList

# function for searching by occupation, parameter (s) is str only, parameter (data) is list of
# user dicts
def occSearch(s, data):
    resList = []
    for e in data:
        if s.lower() in e['occupation'].lower():
            resList.append(e)
    if len(resList) == 0:
        return None
    return resList
