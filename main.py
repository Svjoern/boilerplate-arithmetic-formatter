# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

(arithmetic_arranger(["32 + 698"],True))
(arithmetic_arranger(["32 + 698"]))
# print(arithmetic_arranger(["32 + 698"]))  # 1st plus
# print(arithmetic_arranger(["3801 - 2"]))  # 2nd minus
# print(arithmetic_arranger(["32 + 698", "3801 - 2"]))  #3rd both
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) # 4th all


# Run unit tests automatically
# main()
