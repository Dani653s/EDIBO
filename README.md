# EDIBO
EDIBO projekta elektroniskā klade
## Day 01 - Day 02
### Topics:  
- Terminal (hot-keys)
- Shell (basics)
- Git (basics)
- ASCII table  

#### ASCII table  
[ASCII table](http://www.econwin.org/ascii.htm)  

#### Terminal Online
[Terminal Online](https://cocalc.com/projects/319f978c-07db-4cdb-9c77-96e56038d25a/files/Welcome%20to%20CoCalc.term?session=default)

## Hot-keys (Terminal):fire:     
ctrl + alt + T = open terminal  
shift + ctrl + w = close terminal  
ctrl + shift + "+" = more  
ctrl + "-" = less  
ctrl + L = to clear  
tab - add text  

## Commands (Terminal):floppy_disk:      
*P.S.(?) = something/anything*

PS1 = "?" - to change user name  
echo ? - displays word  
$? + $? - to do equations  
pwd - where am I  
ls - list  
ls -l - list with info  
ls -l -a - all list of directories  
ls -lt - directories Alpha  
mkdir_? - to change the name  
rmdir_? - to remove  
cd - to change directory  
cd.. - to change directory backwards  
cd - - to go backs  
cd / - to go to the root  
cd ~ - home  
cat ? - to see text in the file; also ***tail; head; more;***  
less - to go into the file  
date - date  
cp - copy  
cal - calendar  
history - history  
whoami - who am I  
who - who is a user  
echo $0 - bash  
exit - exit  
last - who was connected last  
tree - tree of files   
man ? - shows documentation of the file  
? & - uses to do not stop work of the terminal  
VirtualBox --startum XP - starts virtual box with XP  

## Git (basic writing/formatting)  
"#" the largest heading  
"##" the second largest heading  
"######" - the smallest heading  

Use ** ** to do bold text  
Use * * to do italic text  
Use - before word to do lists  

DAY 04  
USING SHELL VARIABLES  
variable_name=variable_value    
NAME="Zara Ali" - example    
Script -    
#!/bin/sh  
  
NAME="Zara Ali"  
echo $NAME  
This script will produce -   
Zara Ali  

SPECIAL VARIABLES  
$0 - The filename of the current script.  
$n - These variables correspond to the arguments with which a script was invoked. Here n is a positive decimal number corresponding to the position of an argument (the first argument is $1, the second argument is $2, and so on).
$# - The number of arguments supplied to a script.  
$* - All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.  
$@ - All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2.  
$? - The exit status of the last command executed.  
$$ - The process number of the current shell. For shell scripts, this is the process ID under which they are executing.  
$! - The process number of the last background command.  

USING SHELL ARRAYS  
array_name[index]=value - definition  

${array_name[*]}  - all the arguments - https://unix.stackexchange.com/questions/129072/whats-the-difference-between-and/129077  
${array_name[@]}  - all the arguments  

SHELL BASIC OPERATORS  
 - Arithmetic Operators  
 - Relational Operators  
 - Boolean Operators  
 - String Operators  
 - File Test Operators  
Bourne shell uses external programs - awk, expr.  
Example in test_operators_1.sh.  
Operators: +, -, *, /, %, =, == (equality), != (not equality).  
Relational Operators - 

SHELL DECISION MAKING  
Statements: if...else, case...esac.  

SHELL LOOP TYPES  
Syntax  
while command1 ; # this is loop1, the outer loop
do
   Statement(s) to be executed if command1 is true

   while command2 ; # this is loop2, the inner loop
   do
      Statement(s) to be executed if command2 is true
   done

   Statement(s) to be executed if command1 is true
done  

SHELL LOOP CONTROL  
Example in test_loop_control_1/2/3.sh  

