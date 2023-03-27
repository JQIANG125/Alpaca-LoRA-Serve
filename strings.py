TITLE = "Jiatai Alpaca Playground"

ABSTRACT = """
Demo 13B Alpaca Model
"""

BOTTOM_LINE = """

Cleaned data used for the training
"""

DEFAULT_EXAMPLES = [
    {
        "title": "Tell me about Alpacas.",
        "examples": [
            ["1", "Tell me about alpacas in two sentences"],
            ["2", "What other animals are living in the same area?"],
            ["3", "Are they the same species?"],
            ["4", "Write a Python program to return those species"],
        ],
    },
    {
        "title": "Write a Python program that prints the first 10 Fibonacci numbers.",
        "examples": [
            ["1", "Write a Python program that prints the first 10 Fibonacci numbers."],
            ["2", "Could you explain how the code works?"],
            ["3", "What is recursion?"],
        ]
    }
]

SPECIAL_STRS = {
    "continue": "continue.",
    "summarize": "summarize our conversations so far in three sentences."
}