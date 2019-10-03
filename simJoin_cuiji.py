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

    ### thought：
    ### length check ->

    set_len=[0]*len(dat)
    g_dict={}
    #count=0

    for r_index,r in enumerate(dat[:-1]):
        set_len[r_index]=len(set(r))
        r_length=len(r)
        g_len=threshold+1

        # split r into theo + 1 chunks
        if(r_length not in g_dict.keys()):
            r_group=[r_length//g_len] * g_len
            r_group[:r_length % g_len]= [i+1 for i in r_group[:r_length % g_len]]
            g_index=[]
            for i in range(g_len):
                g_index.append(list(range(sum(r_group[:i]),sum(r_group[:i+1]))))
            g_dict[r_length]=g_index
        else:
            g_index=g_dict[r_length]
        r_group=[]
        for index_list in g_index:
            r_group.append(r[index_list[0]:index_list[-1]+1])
         
        for s_index,s in enumerate(dat[r_index+1:]):
            s_index+=r_index+1
            s_length=len(s)


            #length filter
            if(abs(r_length-s_length)>threshold):
                continue 
            
            #set length filter:
            set_len[s_index]=len(set(s))
            if(abs((set_len[r_index]-set_len[s_index]))>threshold):
                continue

            #multi-match-aware-method
            if(not MultiMatchAware1(r,s,threshold,r_group)):
                continue
            if(not MultiMatchAware3(r,s,threshold,r_group,g_index)):
                continue


            #ED_value=EditDistance(r,s,r_length,s_length)
            ED_value=VerEditDistance(r,s,r_length,s_length,threshold)
            if(ED_value<=threshold):
                output.append([r_index,s_index,ED_value])
            #count+=1
    #print(count)

    
    ## Don't forget to apply threshold to omit unneeded string pairs!!
    ## Note that only string pairs with edit distance no larger than the threshold will be added to results. 
    ## If the edit distance between a pair of strings is larger than the threshold, it should not be added to the result set. 
    
    return output

def EditDistance(r,s,r_l,s_l):
    f=[[0]*(r_l+1) for _ in range(s_l+1)]
    for j in range(r_l+1):
        f[0][j]=j
    for i in range(1,s_l+1):
        f[i][0]=i
        for j in range(1,r_l+1):
            if(r[j-1]!=s[i-1]):
                f[i][j]=min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
            else:
                f[i][j]=min(f[i-1][j-1],f[i][j-1]+1,f[i-1][j]+1)
    return f[i][j]

# verification Edit Distance
def VerEditDistance(r,s,r_l,s_l,tau):
    f=[[tau+1]*(r_l+1) for _ in range(s_l+1)]
    for j in range(r_l+1):
        f[0][j]=j
    for i in range(1,s_l+1):
        f[i][0]=i
        for j in range(i-tau,i+tau):
            if(abs(j-i)> tau or abs(j-i)+abs(r_l-j-(s_l-i))>tau or j>r_l or j<1):
                continue
            if(r[j-1]!=s[i-1]):
                f[i][j]=min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
            else:
                f[i][j]=min(f[i-1][j-1],f[i][j-1]+1,f[i-1][j]+1)
    return f[s_l][r_l]


# Multi-match-aware method: simple "in" version
def MultiMatchAware1(r,s,threshold,group):
    credit=0
    for chunk in group:
        if (chunk not in s):
            credit+=1
        if(credit>threshold):
            return False
    return True

# Multi-match-aware method: real position approach
def MultiMatchAware2(r,s,threshold,group,g_index):
    credit=0
    delta=abs(len(r)-len(s))
    for ii in range(threshold+1):
        p_i=g_index[ii][0]
        length=len(g_index[ii])
        start_position=max( p_i-ii , p_i+delta-(threshold-ii) )
        end_position=min( p_i+ii , p_i+delta+(threshold-ii) )

        for start in range(p_i-ii,p_i+ii+1):
            #print(start,p_i)
            if(group[ii]==s[start:start+length]):
                if(abs(start-p_i)+threshold-ii)>threshold:
                    print(start,p_i)
                    return False
                break
        else:
            credit+=1
        if(credit>threshold):
            return False
    return True

# Multi-match-aware method: left-side perspective
def MultiMatchAware3(r,s,threshold,group,g_index):
    credit=0
    for ii in range(threshold+1):
        p_i=g_index[ii][0]
        length=len(g_index[ii])
        for start in range(p_i-ii,p_i+ii+1):
            if(group[ii]==s[start:start+length]):
                if(abs(start-p_i)+threshold-ii)>threshold:
                    print(start,p_i)
                    return False
                break
        else:
            credit+=1
        if(credit>threshold):
            return False
    return True