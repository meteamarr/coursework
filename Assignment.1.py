#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# 
# * **The deadline for this assignment is due on 28 Mon, 10am.**
# * Create a new directory called `Assignment.1` in your **mp248** repository.
# * Refer to the **grading key** for guidance for what is expected. 
# * Copy this notebook to the `Assignment.1` folder in your mp248 repository. 
# * Answer Problem 1 using the terminal and Problem 2 in the copy of this notebook in your mp248 repository. This notebook is a _bash_ notebook.
# * For Problem 3 & 4 create a Python 3 notebook with the name `Assignment-python.ipnb` and make sure that it is located in the `Assignment.1` folder in your `mp248` repository.
# * Make sure that you add this notebook, the `Assignment-python.ipnb` notebook and any other files indicated below to the final commit of your homework. It is advised that you start committing and pushing once you have partial results.

# ## Problem 1
# 
# ### 1.1
# In a bash cell below download the textfile from the following url: `http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-midsummer-16.txt` containing _SHAKESPEARE: A Midsummer Night's Dream_ using a shell command. 
# 
# Using the command line editor write a shell script called `shake_analysis.sh` that analyses the file and writes out one answer per line to the following questions:
# * How many lines contain the word _Lysander_? 
# * How many lines contain the word _Lysander_ and the word _love_? (case sensitive search)
# * How many words are in the lines that contain the words _Lysander_ and the word _love_?
# * How large is the file `shakespeare-midsummer-16.txt` in `kB` (kilobyte)? The script should output only the integer number of kB.
# 
# ### 1.2
# Further add shell script code that generates the answers to the following questions
# * What is the 6th word in the line that contains both the words _passion_ and _dear_?
# * How long is that word?
# 
# Finally, the script should create a file `midsummer_dad.txt` in which all instances of _EGEUS_ and _Egeus_ are replaced with _dad_, and then report the number of times 'dad' appears in `midsummer_dad.txt`.
# 
# Add the script `shake_analysis.sh` and the file `midsummer_dad.txt` to the `Assignment.1` folder.

# #### Solution

# In[1]:


get_ipython().run_cell_magic('bash', '', '\n# 1.1:\n\n# to download the file:\nwget http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-midsummer-16.txt')


# ## Problem 2
# 
# ## 2.1
# Briefly describe the workflow of modifying files in your git repository and adding them  as a new commit. What command is used to transfer your latest git changes to the GitLab repository. 

# In[2]:


# commands after modifying files:
# git add [dirname]
# git commit   (the type something and save the file)
# git push     (this transfers the latest git changes to the respository)


# ## 2.2
# 1. Create a branch on your repository called `assign1p2`, switch to that branch and add a file called `this_is_a_file_on_my_branch.txt` with the content `Hello World!`. Make sure your branch is pushed to the remote so that it is available on the GitLab server. Once you are done switch back to the master branch and continue there. 
# 2. At this point you should still be in the `Assignment.1` folder and you should be on the master branch. Redirect the output of the `git status` command into the file `git_status_A1P2.txt` and add that file to the repository.

# #### Solution

# In[3]:


get_ipython().run_cell_magic('bash', '', '\n# 1.\ngit checkout assign1p2\ntouch this_is_a_file_on_my_branch.txt\necho "Hello World!" >> this_is_a_file_on_my_branch.txt')


# In[4]:


get_ipython().run_cell_magic('bash', '', '\n# 2.\ntouch git_status_A1P2.txt\ngit status >> git_status_A1P2.txt')


# ## Problem 3
# ### 3.1
# There are some [really long place names](https://www.worldatlas.com/articles/the-10-longest-place-names-in-the-world.html) out there!
# * Create variables that store the following strings: 
#     - `Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch` 
#     - `Pekwachnamaykoskwaskwaypinwanik`
# * Describe the slicing and string addition (concatenation) operations needed to create out of these two string variables a new variable that contains the string `airkoskwa`. This is about slicing string variables. You don't need to automatically find the slicing indices, you can just determine them manually by counting.
# * Create a three-element list that contains the above three strings. Call this list **strlist**. 
# * Create yet another list. Build this list starting from an empty list. Iterating over **strlist**, append the 5th character from each string to this new list.
# * Print the new list. 

# In[5]:


# 3.1

var1 = 'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch'
var2 = 'Pekwachnamaykoskwaskwaypinwanik'

# want to get var3 = 'airkoskwa' from these variables
# see that the bit 'air' is in var1 indices 5-7 inclusive 
# we have to add 1 to the set because it goes from [a,b) so if we want b included go from [a,b+1) (a,b integers)
air = var1[5:8] # this gives us char's from 5-7 from var1 (slicing)
#print(air)
# see that the bit 'koskwa' is in var2 indices 12-17 inclusive
koskwa = var2[12:18] # this gives us char's from 12-17 from var2 (slicing)
#print(koskwa)
var3 = air+koskwa # this combines the two strings (string addition)
#print(var3)

strlist = [var1, var2, var3]
#print(strlist)

newlist = list()
i = 0
while i < len(strlist):
    newlist.append(strlist[i][4:5])
    i = i + 1
    
print(newlist)


# ### 3.2
# * Create a list of integers called `ilist`  starting with 4, ending with 28, in steps of 6 (without manually typing the numbers, use some form of list generator).

# * Turn that list into a numpy array with name `alist` and then create a new array with name `slist` that contains the square of values in `alist`.

# * Open a file `P3.2-data.txt` and write a formatted columns of rows that contain pairwise the `alist` and `slist` elements. Make sure that there are exactly two spaces between the columns. Check the content of the `P3.2-data.txt` file and add it to the commit for this assignment. (Don't close the file yet, we will add more to it.)

# * Write a function called `fa` that takes an array of numbers and a parameter `q` as an input and returns an array that contains the elements $q \log a_\mathrm{i} + q$ where $a_\mathrm{i}$ are the elements of input array. Write the sum of the array that `fa` returns with `alist` and `q=0.5` as input in a formatted output statement into the file `P3.2-data.txt`. The formatted statement should look exactly like this:
#     ```txt
#     The sum of the output array is: i.iii
#     ```
# with 3 digits after the decimal point.

# In[8]:


# 3.2
import numpy as np

ilist = [6*x + 4 for x in range(0,5)]
alist = np.array(ilist)
slist = alist*alist

filename = "P3.2-data.txt"
file = open(filename, 'w')

i = 0
while i < len(slist):
    file.write(str(alist[i]))
    file.write(str('  '))
    file.write(str(slist[i]))
    file.write('\n')
    i = i + 1
    
def fa(a, q):
    n = len(a)
    j = 0
    newarr = list()
    while j < n:
        newarr.append((np.log10(a[j]) + 1.0)*q)
        j = j + 1
    return newarr

args = fa(alist,0.5)
j = 0
m = 0
while j < len(args):
    m = m + args[j]
    j = j + 1
   
file.write('The sum of the output array is: %.3f' %m)
file.close()


# ## 3.3

# * You are given a list of fruit. 
#     ```python
#     list_of_fruit = ['apple', 'banana', 'orange', 'tomato']
#     ```
#     Create a Python cell with loop in which the user will be asked for each fruit type how many fruits there are (say, for example, in storage), and how much each fruit costs. Save these numbers as tuples in a dictionary called `fruit_db`. Use the `input` function to implement this. The fruit names are the dictionary keys.
# * Execute that loop cell and provide some reasonable input.
# * Then print the fruit database with columns for fruit name, number and cost in a formatted table.

# In[11]:


### 3.3

list_of_fruit = ['apple', 'banana', 'orange', 'tomato']

fruit_db = {}
for x in list_of_fruit:
    fruit_db[x] = [0.0]*2
    num = input('Enter how many {} we have: '.format(x))
    cost = input('Enter how much an {} is: '.format(x))
    fruit_db[x][0] = num
    fruit_db[x][1] = cost
    
#print(fruit_db)
    


# In[12]:


form = '{0:<12}{1:<8}{2:<1}'
print(form.format('fruit name', 'number', 'cost'))
i = 0
while i < len(list_of_fruit):
    fruit = list_of_fruit[i]
    print(form.format(fruit, fruit_db[fruit][0], fruit_db[fruit][1]))
    i = i + 1


# In[ ]:




