#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Implement SimilarityJoinED()
    You can add supplement function, but it is not allowed
    to modify the function name and parameters
"""
partition_dict = {}

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
    len_dat = len(dat)
    for i in range(len_dat - 1):
        for j in range(i + 1, len_dat):
            delta = abs(len(dat[i]) - len(dat[j]))
            if delta > threshold:
                continue
            result = doCompare(dat[i], dat[j], threshold, delta)
            output.append(result)

    return output

def doCompare(string1, string2, threshold, delta):
    partition_index = doPartition(string1, threshold)
    print(partition_index)
    return

def doPartition(dat, threshold):
    global partition_dict
    print(partition_dict)
    len1 = len(dat)
    if len1 in partition_dict:
        return partition_dict[len1]
    segement_number = threshold + 1
    segement_base = len1 // segement_number
    segement_more = len1 % segement_number
    partition_index = []
    index = 0
    if segement_more == 0:
        for i in range(segement_number):
            paritition_index.append(index)
            index += segement_base
    else:
        base_number = segement_number - segement_more
        for i in range(base_number):
            partition_index.append(index)
            index += segement_base
        for i in range(segement_more):
            partition_index.append(index)
            index += segement_base + 1
    partition_dict[len1] = partition_index
    return partition_index
