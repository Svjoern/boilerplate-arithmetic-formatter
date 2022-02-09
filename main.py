# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

# print(arithmetic_arranger(["1 + 3g5"], True))  # 1st plus
#print(arithmetic_arranger(["3 + 855", "988 + 40"], True))  # 2nd minus
# print(arithmetic_arranger(["32 + 698", "3801 - 2"], True))  #3rd both
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)) # 4th all

# Run unit tests automatically
main()