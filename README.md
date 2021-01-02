## PyTests Three Exercises
### Created on 2020-12-29
## Last updated: 2021-01-02
###### Version: 1.1 

## Functions
##### PyOne
A function that given 2 vectors of integers finds the first repeated number

----
##### PyTwo
A function that given a path of the file system finds the first file that meets the
following requirements
- a. The file owner is admin
- b. The file is executable
- c. The file has a size lower than 14*2^20
------------

##### PyThree


A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. 
For example, given the sequence 0,1,1,0 
how many changes are needed so that the result is 0,1,0,1

----

###### Requirements
 - to have installed python3.x.x

##### Run Test Coverage
 Install pip if you don't have it  and then:
 
`cd PyThreeTest`

`python3 -m venv .env`

`source .env/bin/activate`

`pip3 install -r requirements.txt`
 
` python3 -m pytest tests/ -v --cov command`

###### Deactivate the virtual env

`deactivate`

