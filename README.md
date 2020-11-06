# OOP Tasks

## Task 1: FizzBuzz Game

Simple game to substitute:
- multiples of 3 for fizz
- multiples of 5 for buzz
- multiples of both 3, 5 for fizzbuzz

Create class with option to change fizz, buzz, and max range to count up to.


### Tasks

Core:
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz" instead of the number
* For numbers which are multiples of both three and five print "FizzBuzz".

Extra:
* make a new fizzbuzz file and make it functional
* make it so we we can decide which numbers to substitute for fizz and buzz using functions



Hint: loop, range, control flow

### Acceptance Criteria

* All core task are done
* Code works with no error



## Task 2: Restaurant Order

Menu and Order class allowing to create multiple menus and allowing customer choice of which menu to order from.

### User Stories

#### 1
**AS a User I want to be able to see the menu in a formated way, so that I can order my meal.**

#### 2
**AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten**

#### 3
**As a user, I want to have my order read back to me in formated way so I know what I ordered.**

## Task 3: Scrabble

Scrabble word score calculator, returning score for word based on scrabble letter values.


### Base Scrabble word calculator instructions 

Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided. 

```
text
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

## Task 4: Calculator

- Build a basic object Orientated Calculator
- **phase 1**: build a simple calculator class containing
- add, subtract, multiply, divide.
- **phase 2**: expand by creating:
- Divisible by method that returns true or false dependent on the outcome
- Work out and return the area of a triangle
- inch to cm converter
- NOTE -> Must be in class and method format

## Task 5: DNA String Parsing

The Problem:  
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

**Given**: A DNA string s of length at most 1000 nt.

**Return**: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:

_AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC_
Sample Output:

20 12 17 21

NOTE -> Must be in class and method format


## Task 6: Bank Account

Create an **AccountHolderDetails** class with attributes name, address, age, 

**Inherit** Account holder class into MyAccount

- Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type), balance.
- Create a constructor () with parameters: accountNumber,  balance.
- Create a Deposit() method which manages the deposit actions.
- Create a Withdrawal() method  which manages withdrawals actions.
- Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
- Create a display() method to display account details.
- Create manageAccount class and import everything from BankAccount class
call all methods in manageAccount class that have are available from parent class
- Create a display() method to display account details.
