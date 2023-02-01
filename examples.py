"""Code-review examples used to finetune a model."""

import csv

fib_correct = """def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)"""
fib_correct_response = """Yes, this is correct."""

fib_wrong = """def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 3)"""
fib_wrong_response = """No, this is incorrect. The recursive call should be to fib(n - 2) instead of fib(n - 3)."""


type_correct = """def mul(a: int, b: int) -> int:
    return a * b"""
type_correct_response = """Yes, this is correct."""

type_wrong = """def mul(a: int, b: int) -> int:
    return a * b + 0.5"""
type_wrong_response = """No, this is incorrect. The return type should be int instead of float, and the functions name is misleading given the +0.5, which should perhaps be removed."""

ALL = [
    (fib_correct, fib_correct_response),
    (fib_wrong, fib_wrong_response),
    (type_correct, type_correct_response),
    (type_wrong, type_wrong_response)
]

endsep_prompt = "\n\n###\n\n"
endtoken = "END"

if __name__ == "__main__":
    print("Writing examples to examples.csv")
    with open("examples.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["prompt", "completion"])
        writer.writerows([[code + endsep_prompt, " " + response.strip() + " " + endtoken] for code, response in ALL])
