#String converter?
#Austin Cefaratti 1/16/19
#modifies each etry in a string by converting it into a number

def toNumbers(strLists):
    strLists[0] = '1'
    strLists[1] = '2'
    strLists[2] = '3'
    strLists[3] = '4'
    strLists[4] = '5'
    return strLists
def main():
    print("This program converts word strings into numbers")
    strLists = ["one","two","three","four","five"]
    print()
    print("The original list was: ",strLists)
    print()
    print("The returning list is: " ,toNumbers(strLists))
    print()
    print("Created and owned by the Combobert Corperration")
main()
