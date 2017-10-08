# TablePrint
Python module I threw togther for printing formatted tables, I was going to write it anyway for a seperate project, so I figured why not write it as a module so I can use it again easily if needed

## Usage
Usage for TablePrint is easy, simply feed it any number of lists with your data in it, each list being a new row and each item being a column
#### Example
Input:
```python
  from TablePrint import table
  
  good = ['Lawful Good', 'Neutral Good', 'Chaotic Good']
  neutral = ['Lawful Neutral', 'True Neutral', 'Chaotic Neutral']
  evil = ['Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
  
  table(good, neutral, evil)
```
Output:
```
-------------------------------------------------
|Lawful Good    |Neutral Good   |Chaotic Good   |
-------------------------------------------------
|Lawful Neutral |True Neutral   |Chaotic Neutral|
-------------------------------------------------
|Lawful Evil    |Neutral Evil   |Chaotic Evil   |
-------------------------------------------------
```
#### Installation
Currently there is no pip installer, but you dont really need one, just drop the TablePrint file into your project directory.
