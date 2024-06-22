import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    ''' 
    since fave_numbers cannot contain duplicates, calculating
    the difference between the length of 
    fave_numbers_1 and the length of the set containing 
    fave_numbers_1 and fave_numbers_2 can determine the match

    i.e [1, 2, 3, 4], [2, 3] into a set would just be [1, 2, 3, 4]
    which is the length of the first list
    '''
    allFave = set(fave_numbers_1 + fave_numbers_2)
    if len(fave_numbers_1) == len(allFave):
        return True
    return False

    '''
    ORIGINAL CODE

    for number in fave_numbers_2:
        if number not in fave_numbers_1:
            return False

    return True
    
    '''