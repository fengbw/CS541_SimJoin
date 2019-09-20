# README for Assignment 1

### Requirements

Implement `SimilarityJoinED()`.  You can add your own auxiliary function in `simJoin.py`

Read and Write functions are provided in `main.py`.  Please DO NOT modify `main.py` (But you might want to change the input filenames while testing.)

### Submission

Submit your `simJoin.py` via Canvas We will use our own main.py and grading script to test your code.

## Note for grade and test
When you finish your implementation, running `python main.py` should gives your output as a csv file (`out.csv` by default). Example testsets and their outputs with corresponding threshold tau are provided in `./testset/`.

Be careful about the datatype in each column (ID and E-distance are all int, do not print something looks like 0.0, 1.0, etc.) as well as output format.

We will grade using `diff` in Linux. 

Example: `diff sample_test1.csv out.csv`

### Final large test Set 

We will use a large dataset with less than 1 million strings, each string with length at least 10 characters and at most 200 characters for final evaluation.

---

## SimilarityJoinED()
1. Number of Parameters: 2
	* dat: A list generated from input file (each element is a line in the input file)
	* threshold: tau
2. Input data format
	* one string per line
	* ID is not recorded in the file, but please see the line index as the ID for each string. Note: START FROM 0!
	
3. Output
	* You should output an csv file WITHOUT HEADER, dimension is  `n by 3`, where n is the number of combination that fits for the threshold requirements. Since output function has already provided, you should generate a list of list of 3 tuple`<ID1,ID2,Edistance>` (all of them are int)  in Python and pass it to `WriteResults()` 
	* Note about order of the tuples: Lexicographical order of <ID1, ID2>. Ascendant to ID1; If ID1 is the same, ascendant to ID2.

## Example: self-joint with threshold = 1:

* Run
```
python main.py
```

* Input file `sample_test1.txt` (4 lines, with index 0 ,1, 2, 3)
```
hello
hell
hella
hallo
```
* Expected output `out.csv`

```
0,1,1
0,2,1
0,3,1
1,2,1

```

### Output Format Note
1. Contains 3 columns `<ID1,ID2,Edistance>`, separated with `,`.
2. Do not write headers and index
