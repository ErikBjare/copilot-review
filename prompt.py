def build_prompt(code: str):
    prompt = f"""
We are going to review a piece of python code.
Here is the code:
```python
{code}
```

Is the above code correct, yes or no? If not, why?

ANSWER: """.strip()
    return prompt
