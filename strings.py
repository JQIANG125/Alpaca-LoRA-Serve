TITLE = "Jiatai Alpaca Playground"

ABSTRACT = """
Demo 13B Alpaca Model
"""

BOTTOM_LINE = """

Cleaned data used for the training
"""

DEFAULT_EXAMPLES = [
    {
        "title": "Tell me about UOB.",
        "examples": [
            ["1", "What is UOB?"],
            ["2", "Explain more about UOB"],
            ["3", "When is UOB founded"],
            ["4", "Talk more about UOB"],
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
