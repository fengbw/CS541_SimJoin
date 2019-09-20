#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Implement SimilarityJoinED()
    You can add supplement function, but it is not allowed
    to modify the function name and parameters
"""
def SimilarityJoinED(dat, threshold):
    """
        @filename: String containing the path of the File
        @threshold: tau
        
        ======> See README.md for details
    """
    
    output = []
    #### ==== Main algorithm to calculate Edistance ====

    ## Hint:
    # 1. Index from 0 - (len(lines)-1)
    # 2. Filters: Get the candidates (e.g. length check & multi-match etc.)
    # 3. Verify the candidates (can be interleaved with 2.)
    # 4. Output format: List of list of 3 tuples [ID1, ID2, Edistance]


    # ...Code here...
    
    ## Don't forget to apply threshold to omit unneeded string pairs!!
    ## Note that only string pairs with edit distance no larger than the threshold will be added to results. 
    ## If the edit distance between a pair of strings is larger than the threshold, it should not be added to the result set. 
    
    return output