from dataclasses import dataclass


@dataclass
class Answer:
    answer: float
    n: int
    is_diverge: bool
