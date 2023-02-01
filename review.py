"""
Use OpenAI GPT models to generate review comments for GitHub pull requests.

Should be able to run as a GitHub Action.
"""

import openai
from github import Github
import os

from prompt import build_prompt
from examples import fib_wrong, fib_correct

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# GitHub API key (set in GitHub Actions CI)
# https://docs.github.com/en/actions/reference/authentication-in-a-workflow
github_token = os.getenv("GITHUB_TOKEN")


def complete(prompt):
    response = openai.Completion.create(
        engine="davinci:",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["END"],
    )

    return response.choices[0].text


def review(code):
    """Review a piece of code"""
    prompt = build_prompt(code)
    print("Prompt: \n" + prompt)

    response = complete(prompt)
    correct = "yes" in response[:10].lower()
    return response, correct


def get_diff():
    """Get the diff from the GitHub API"""
    gh = Github(github_token)
    repo = gh.get_repo("ErikBjare/copilot-review")
    pull = repo.get_pull(1)
    files = pull.get_files()
    patch = files[0].patch
    return patch


def test_review_wrong():
    code = fib_wrong
    response, correct = review(code)
    print("Response:", response)
    assert correct is False
    assert False

def test_review_correct():
    code = fib_correct
    response, correct = review(code)
    print("Response:", response)
    assert correct is True


if __name__ == "__main__":
    diff = get_diff()
    review("def foo():\n    print('Hello world!')")
