# uber_script_nl
### Python script that automates the process of calculating taxes and revenues of UberEats drivers in the Netherlands

####(It does work with both Dutch and English statements)

Dependencies:
  python3 -- to run the script (download from [here]{https://www.python.org/downloads/}
    pandas -- to read csv files (install using pip)
    	`pip3 install pandas`

### usage:

  1. create a folders tree as such:

    Uber
     |
     |-> pay_statements
     |-> script

  2. clone the repository or download its content into "script"  
  3. login to [uber driver]{driver.uber.com} and under the "payment statements" tab select the "statements" section
  4. download all statements for the selected months
  5. move those files into "pay statement" local folder
  6. open a terminal and navigate into the script folder:
  7. run the script from the terminal as in the following example:

  > for Windows users

  `~$ chdir Uber`
  `~$ chdir script`
  `~$ python3 tellen.py -m YOUR_TWO DIGITS_MONTH_NUMBER`

  > for Linux and Mac users

  `~$ cd Uber`
  `~$ cd script`
  `~$ python3 tellen.py -m YOUR_TWO_DIGITS_MONTH_NUMBER`

### all options
`-m [0-1]+[0-9]+` :

monthly summary, your value must be a two digit number from 01 to 12. When a year is specified, it will return its info as you would expect. You can add an year to be more specific

`-y [YEAR]` :

yearly summary, if no value is specified the current would be taken into account, if used with a value then does what expected. When a month is specified before it, then it will return the info of the month of that year.

`-q QUARTER` :

to use on its own, it has to have a single-digit value between 1 and 4, prints the last available quarter of that index starting from January. You can be more specific by adding the year flag if you prefer

### extra info

none of these features send any information outside your computer.
