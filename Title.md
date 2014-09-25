


#Starter - Selection Statements
These tasks are designed to refresh the reading and research you have undertaken at home prior to this lesson. If you have not completed the R&R assignment then please speak to your teacher before attempting these exercises.

##Relational and Boolean Operators
Relational and boolean operators are used to construct selection statements. Refresh your knowledge of these concepts by attempting the below tasks.

###Task 1
Match each relational operator to its description.

|Operator|Description|
|:------:|-----------|
|`==`|equal too|
|`<`|less than |
|`>`|greater than|
|`!=`|not equal too|
|`<=`|less than or equal too|
|`>=`|greater ha or equal too|

###Task 2
Look at each of the following expressions, without using a computer what would they evaluate to?

|Variable|Value|
|--------|:---:|
|`test_score`|54|
|`age`|18|

|Expression|Result|
|:--------:|:----:|
|`5 > 3`|True| |
|`test_score < 12`|False |
|`4 != test_score`| True|
|`age == 17`|False |
|`test_score > 50 and age > 12`| True|
|`not test_score > 50`|False |

##Debugging Code
Debugging code is an important skill you must develop. The below will introduce you to **syntax**, **run-time** and **logical errors** that can occur in your code.

###Task 1
The code shown below contains some errors. Annotate the code to show where the errors occur.

```python
#test grading program
test_score = int(input("Please enter your test score: "))
#int(input("please enter your test score:"))
if test_score >= 40 and test_score < 50:
    print("E grade")
elif test_score >= 50 and test_score <60:
    print("D grade")
elif test_score >= 60 and test_score < 70:
    print("C grade")
elif test_score >= 70 and test_score < 80:
    print("B grade")
elif test_score >= 80: 
    print("A grade")
else:
    print("Fail")
```

###Task 2
Now, load the `selection_errors.py` Python file and attempt to run it - note down any error messages you encounter and attempt to explain them.

Error Message|Explanation|
|-----------|-----------|
| | |
| | |

###Task 3
Assuming that you have corrected the errors in `selection_errors.py`, run the program and enter a test score which will give an A grade. For example, 94. What happens? Use the space below for your explanation.

|Explanation|
|The program gives you an A grade|
| |

There are three types of error in `selection_errors.py`:

1. Syntax errors
2. Run-time errors
3. Logical errors

In the space below develop a definition of each type and state the type of each error in Tasks Two and Three.

###Task 4
Please read page 95 of the AS Computing textbook and then use the space below for your definitions.

|Error|Definition|
|-----|----------|
|Syntax error| |
|Run-time error| |
|Logical error| |

###Task 5
Indicate whether you think the errors in **Task 2 and 3** where syntax, run-time or logical errors.

|Error|Type|
|-----|----|
|Task 2 (error message 1)| |
|Task 2 (error message 2)| |
|Task 3 error| |

##Summary
In this section you have debugged a selection statement and discovered that there are three types of errors: syntax, run-time and logical. You will encounter these errors repeatedly in your code so it is vital that you have an appreciation of the differences between them.


