"""
Read command-line arguments.
Check the number of arguments.
Use arguments to perform tasks (in this case, simple operations like addition and multiplication).
Access the Python version and the list of paths where Python modules are searched.


git commit -m "some commit info"

            0           1  2 3
python3 sys_example.py add 2 2
python3 sys_example.py multiply 3 5
python3 sys_example.py
"""

import sys

# Check the number of arguments
if len(sys.argv) < 4 or sys.argv[1] == '--help':
    print("Usage: python3 sys_example.py operaion num1 num 2")
    print("operation can be 'add' or 'multiply'")
    sys.exit(1) # exit the script with an error



# Read the operation and number from cmd
operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if operation == 'add':
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is {result}")
elif operation == 'multiply':
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is {result}")
else:
    print("Invalid operation. Please use 'add' or 'multiply'")