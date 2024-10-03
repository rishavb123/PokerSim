from typing import List
from enum import Enum
import random


class Value(Enum):
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
    SPADES = "S"
    CLUBS = "C"
    DIAMONDS = "D"
    HEARTS = "H"


class Card:

    def __init__(self, value: Value, suit: Suit) -> None:
        self.value = value
        self.suit = suit

    @staticmethod
    def of_string(card_string: str) -> "Card":
        value = Value(
            int(
                card_string[:-1]
                .replace("A", "1")
                .replace("J", "11")
                .replace("Q", "12")
                .replace("K", "13")
            )
        )
        suit = Suit(card_string[-1])
        return Card(value, suit)

    def __str__(self) -> str:
        value_string = str(self.value.value)
        if value_string == "1":
            value_string = "A"
        return (
            value_string.replace("11", "J").replace("12", "Q").replace("13", "K")
            + self.suit.value
        )


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
