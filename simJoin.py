#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Implement SimilarityJoinED()
    You can add supplement function, but it is not allowed
    to modify the function name and parameters
"""
partition_dict = {}
substring_index = r_position = s_position = substring_length = 0

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
            result = doCompare(i, j, dat[i], dat[j], threshold, delta)
            if result is not None:
                output.append(result)
    # print(output)
    return output

def doCompare(index1, index2, string1, string2, threshold, delta):
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    partition_index = doPartition(string1, threshold)
    doVerification = doSelection(string1, string2, threshold, delta, partition_index)
    if doVerification:
        global substring_index, r_position, s_position, substring_length
        r_left, r_right = string1[:r_position], string1[r_position + substring_length:]
        s_left, s_right = string2[:s_position], string2[s_position + substring_length:]
        if r_left == "":
            ed = Verification(r_right, s_right, threshold)
            if ed <= threshold:
                return [index1, index2, ed]
        if r_right == "" or r_right == s_right:
            ed = Verification(r_left, s_left, threshold)
            if ed <= threshold:
                return [index1, index2, ed]
        # special case: so_jin_kang sinjun_kang
        threshold_left = substring_index - 1
        threshold_right = threshold + 1 - substring_index
        ed_left = Verification(r_left, s_left, threshold_left)
        if ed_left > threshold_left:
            return
        ed_right = Verification(r_right, s_right, threshold_right)
        if ed_right > threshold_right:
            return
        return [index1, index2, ed_left + ed_right]
    # if doVerification:
    #     ed = Verification(string1, string2, threshold)
    #     if ed <= threshold:
    #         return [index1, index2, ed]
    return

def doPartition(dat, threshold):
    global partition_dict
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
            partition_index.append(index)
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

def doSelection(string1, string2, threshold, delta, partition_index):
    # print(string1, partition_index)
    substrings = []
    index_number = len(partition_index)
    for i in range(index_number):
        if i == index_number - 1:
            substrings.append(string1[partition_index[i]:])
            continue
        substrings.append(string1[partition_index[i]:partition_index[i + 1]])
    # print(substrings)
    for i, position in enumerate(partition_index):
        leftBound = max(position - (i + 1 - 1), position + delta - (threshold + 1 - i - 1))
        rightBound = min(position + (i + 1 - 1), position + delta + (threshold + 1 - i - 1))
        # print(leftBound, rightBound)
        selectionLength = len(substrings[i])
        selections = []
        for j in range(leftBound, rightBound + 1):
            selection = string2[j:j + selectionLength]
            if substrings[i] == selection:
                global substring_index, r_position, s_position, substring_length
                substring_index, r_position, s_position, substring_length = i + 1, position, j, selectionLength
                return True
            # selections.append(string2[j:j + selectionLength])
        # print(selections)
        # if substrings[i] in selections:
        #     return True
    return False

def Verification(string1, string2, threshold):
    len1 = len(string1)
    len2 = len(string2)
    matrix = [[float("inf") for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(len1 + 1):
        matrix[0][i] = i
    for j in range(len2 + 1):
        matrix[j][0] = j
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if abs(i - j) > threshold:
                continue
            if string1[j - 1] == string2[i - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    # print(matrix)
    # print("---------------")
    return matrix[len2][len1]
