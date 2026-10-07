"""Local quote catalog — no network calls."""

from typing import TypedDict


class Quote(TypedDict):
    text: str
    author: str


QUOTES: list[Quote] = [
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
    },
    {
        "text": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein",
    },
    {
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle",
    },
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
    },
    {
        "text": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
    },
    {
        "text": "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        "author": "Benjamin Franklin",
    },
    {
        "text": "The best time to plant a tree was 20 years ago. The second best time is now.",
        "author": "Chinese proverb",
    },
    {
        "text": "Simplicity is the ultimate sophistication.",
        "author": "Leonardo da Vinci",
    },
    {
        "text": "Not all those who wander are lost.",
        "author": "J.R.R. Tolkien",
    },
    {
        "text": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama",
    },
    {
        "text": "The only impossible journey is the one you never begin.",
        "author": "Tony Robbins",
    },
]
