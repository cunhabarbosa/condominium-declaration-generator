"""Utility functions for user interaction and confirmation prompts."""

def ask_yes_no(question: str) -> bool:
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer in ["y", "yes"]
