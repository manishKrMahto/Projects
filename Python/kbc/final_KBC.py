import random

countList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def get_random_number():
    temp = random.choice(countList)
    countList.remove(temp)
    return temp


# format [[question,option 1 , option 2 , option 3 , option 4 , currect answer]]
questionList = [
    (
        "Identify the correct extension of the user-defined header file in C++ ",
        ".cpp",
        ".hg",
        ".h",
        ".hf",
        ".h",
    ),
    (
        "Identify the incorrect constructor type",
        "friend constructor",
        "default constructor",
        "parameterized constructor",
        "copy constructor",
        "friend constructor",
    ),
    (
        "C++ uses which approach",
        "right-left",
        "top-dowm",
        "left-right",
        "bottom-up",
        "bottom-up",
    ),
    (
        "Which of the following data type is supported in C++ but not in C",
        "int",
        "bool",
        "double",
        "float",
        "bool",
    ),
    (
        "Identify the correct syntax for declaring arrays in C++",
        "array arr[10]",
        "array[10]",
        "int arr[10]",
        "int arr",
        "int arr[10]",
    ),
    (
        "Size of wchat_t is",
        "2",
        "4",
        "2 or 4",
        "depends on number of bits in system",
        "depends on number of bits in system",
    ),
    (
        "Which of the following is “address of operator”",
        "*",
        "&",
        "[]",
        "&&",
        "&",
    ),
    (
        "Identify the correct example for a pre-increment operator",
        "++n",
        "n++",
        "--n",
        "+n",
        "++n",
    ),
    (
        "Which of the following loops is best when we know the number of iterations",
        "while loop",
        "do while",
        "for loop",
        "all of the above",
        "for loop",
    ),
    (
        "Identify the scope resolution operator",
        ":",
        "::",
        "?",
        "none",
        "::",
    ),
    (
        "goto can be classified into",
        "label",
        "variable",
        "operator",
        "function",
        "label",
    ),
    (
        "identify the correct definition of '*' operator in pointer",
        "address of operator",
        "value of address operator",
        "multiplication operator",
        "all of the above",
        "value of address operator",
    ),
    (
        "by which of the following can the if-else statement be replaced",
        "bitwise operator",
        "logical operator",
        "conditional operator",
        "arithmetic operator",
        "conditional operator",
    ),
    (
        "choose the correct default return value of function",
        "int",
        "void",
        "char",
        "float",
        "int",
    ),
    (
        "using which of the following data type can 19.54 be represented",
        "void",
        "double",
        "int",
        "node",
        "double",
    ),
    (
        "when can an inline function be expanded",
        "runtime",
        "compile time",
        "never gets expanded",
        "all of the above",
        "compile time",
    ),
    (
        "choose the correct option which is mandatory in a function",
        "return_type",
        "parameter",
        "function_name",
        "both a and c",
        "both a and c",
    ),
    (
        "The constants in C++ are also known as?",
        "pre-processor",
        "litrals",
        "const",
        "none",
        "litrals",
    ),
    (
        "Using which of the following keywords can an exception be generated",
        "threw",
        "throws",
        "throw",
        "catch",
        "throw",
    ),
    (
        "identify the size of int datatype in c++",
        "1 byte",
        "2 bypes",
        "4 bytes",
        "depends on the compiler",
        "depends on the compiler",
    ),
]

prizeList = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    7500000,
    10000000,
    70000000,
]

wining_amount = 0

save_level_amount = (
    False  # if player give 10 answer then he/she will win atleast this amount
)


i = 0  # to iterate prizelist

wrong = False
for _ in range(17):
    index = get_random_number()

    print(
        f"Question for {prizeList[i]}/- \nQ. {questionList[index][0]} ? \n  1. {questionList[index][1]} \n  2. {questionList[index][2]} \n  3. {questionList[index][3]} \n  4. {questionList[index][4]}  \n\nenter right answer's option number : ",
        end="",
    )

    ans = int(input())

    if questionList[index][ans] == questionList[index][5]:
        print(f"\nright answer \nYOU WON {prizeList[i]}", end="\n\n")
        amount = prizeList[i]

        if amount == 320000:
            save_level_amount = True
    else:
        wrong = True
        break
    i = i + 1

if wrong == False:
    print("\nyour final wining amount is :", amount)
elif save_level_amount == True and wrong == True:
    print("\nyour final wining amount is : 320000")
else:
    print("\nyour final wining amount is : 0")
