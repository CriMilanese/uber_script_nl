# uber_script_nl
### Python script that automates the process of calculating taxes and revenues of UberEats drivers in the Netherlands

Dependencies:
  python3 -- to run the script (download from [here]{https://www.python.org/downloads/}
    pandas -- to read csv files (install using pip)

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
      ~$ chdir Uber; chdir script; python3 tellen.py -m MONTH_NUMBER

      > for Linux and Mac users
      ~$ cd Uber; cd script; python3 tellen.py -m MONTH_NUMBER
