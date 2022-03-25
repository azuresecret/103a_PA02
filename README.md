# CS103a Spring 22

# PA02: tracker.py and the Transaction class

a. Pytest:
pa02/test_category.py::test_to_cat_dict PASSED                           [ 12%]
pa02/test_category.py::test_add PASSED                                   [ 25%]
pa02/test_category.py::test_delete PASSED                                [ 37%]
pa02/test_category.py::test_update PASSED                                [ 50%]
pa02/test_transaction.py::test_select_all PASSED                         [ 62%]
pa02/test_transaction.py::test_add PASSED                                [ 75%]
pa02/test_transaction.py::test_delete PASSED                             [ 87%]
pa02/test_transaction.py::test_summarize PASSED                          [100%]

b. Pylint:
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:114:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:60:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:61:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
tracker.py:60:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:60:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:60:0: R0915: Too many statements (51/50) (too-many-statements)
tracker.py:120:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:138:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:142:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:145:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:146:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:149:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:150:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:36:0: W0611: Unused import sys (unused-import)
tracker.py:36:0: C0411: standard import "import sys" should be placed before "from transactions import Transaction" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.93/10 (previous run: 6.59/10, +1.34)

************* Module transactions
transactions.py:10:0: C0301: Line too long (103/100) (line-too-long)
transactions.py:29:0: C0301: Line too long (106/100) (line-too-long)
transactions.py:57:0: C0301: Line too long (113/100) (line-too-long)
transactions.py:73:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:4:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:37:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:57:16: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
transactions.py:58:24: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
transactions.py:66:24: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------------------------------------
Your code has been rated at 7.69/10 (previous run: 7.69/10, +0.00)

************* Module test_transaction
test_transaction.py:39:0: C0325: Unnecessary parens after 'assert' keyword (superfluous-parens)
test_transaction.py:47:0: C0325: Unnecessary parens after 'assert' keyword (superfluous-parens)
test_transaction.py:54:0: C0325: Unnecessary parens after 'assert' keyword (superfluous-parens)
test_transaction.py:58:0: C0325: Unnecessary parens after 'assert' keyword (superfluous-parens)
test_transaction.py:16:13: W0621: Redefining name 'dbfile' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:18:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:23:13: W0621: Redefining name 'empty_db' from outer scope (line 16) (redefined-outer-name)
test_transaction.py:37:20: W0621: Redefining name 'small_db' from outer scope (line 23) (redefined-outer-name)
test_transaction.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:42:13: W0621: Redefining name 'small_db' from outer scope (line 23) (redefined-outer-name)
test_transaction.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:50:16: W0621: Redefining name 'small_db' from outer scope (line 23) (redefined-outer-name)
test_transaction.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:57:19: W0621: Redefining name 'small_db' from outer scope (line 23) (redefined-outer-name)
test_transaction.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 5.45/10 (previous run: 2.42/10, +3.03)

************* Module test_category
test_category.py:16:13: W0621: Redefining name 'dbfile' from outer scope (line 10) (redefined-outer-name)
test_category.py:18:4: C0103: Variable name "db" doesn't conform to snake_case naming style (invalid-name)
test_category.py:23:13: W0621: Redefining name 'empty_db' from outer scope (line 16) (redefined-outer-name)
test_category.py:38:11: W0621: Redefining name 'small_db' from outer scope (line 23) (redefined-outer-name)
test_category.py:43:8: C0103: Variable name "s" doesn't conform to snake_case naming style (invalid-name)
test_category.py:60:4: C0103: Variable name "a" doesn't conform to snake_case naming style (invalid-name)
test_category.py:68:13: W0621: Redefining name 'med_db' from outer scope (line 38) (redefined-outer-name)
test_category.py:84:16: W0621: Redefining name 'med_db' from outer scope (line 38) (redefined-outer-name)
test_category.py:105:16: W0621: Redefining name 'med_db' from outer scope (line 38) (redefined-outer-name)

------------------------------------------------------------------
Your code has been rated at 8.50/10 (previous run: 7.67/10, +0.83)

c. Output:
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 5
adding transcations
transaction number: 1
transaction amount: 100
category: food
date:19940412
description baby food
> 5
adding transcations
transaction number: 2
transaction amount: 100
category: food
date:19940413
description baby food
> 4
showing transcations


item #     amount     category   date       description                   
----------------------------------------
1          100        food       19940412    baby food                    
2          100        food       19940413    baby food                    
> 7
summarizing by date
[('12', 1, 100.0), ('13', 1, 100.0)]
[('12', 1, 100.0), ('13', 1, 100.0)]
> 8
summarizing by month
[('04', 2, 100.0)]
[('04', 2, 100.0)]
> 9
summarizing by year
[('1994', 2, 100.0)]
[('1994', 2, 100.0)]
> 10
summarizing by category
[('food', 2, 100.0)]
[('food', 2, 100.0)]
> 6
deleting a transaction
transaction number: 1
> 4
showing transcations


item #     amount     category   date       description                   
----------------------------------------
2          100        food       19940413    baby food                    
> 6
deleting a transaction
transaction number: 2
> 4
showing transcations
no items to print
> 

