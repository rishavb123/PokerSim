from typing import List
from enum import Enum
import random


class Value:
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(Enum):
    SPADES = 0
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3


class Card:

    def __init__(self, value: Value, suit: Suit) -> None:
        self.value = value
        self.suit = suit


class Deck:

    ALL_CARDS = [Card(val, suit) for val in (Value) for suit in (Suit)]

    def __init__(self, cards: List[Card] | None = None) -> None:
        self.cards = Deck.ALL_CARDS if cards is None else cards

    def shuffle(self):
        random.shuffle(self.cards)

    def peek(self, n: int | None = None):
        if n is None:
            return self.cards[0]
        else:
            return self.cards[:n]

    def draw(self, n: int | None = None):
        if n is None:
            return self.cards.pop(0)
        else:
            drawn = self.cards[:n]
            self.cards = self.cards[n:]
            return drawn
