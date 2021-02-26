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
  6. run the script from the terminal as in the following example:

  > for Windows users

  `~$ chdir Uber; chdir script; python3 tellen.py -m YOUR_MONTH_NUMBER`

  > for Linux and Mac users

  `~$ cd Uber; cd script; python3 tellen.py -m YOUR_MONTH_NUMBER`

### other options

`-y YEAR` :
yearly summary, if not used the current is implied. When a month is specified with it, then it will return its info as you would expect

`-q QUARTER` :
to use on its own, with a value between 1 and 4, prints the last available quarter of that index starting from January

### extra info

none of these features send any information outside your computer.
