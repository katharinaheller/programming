"""The Cards for the UNO game."""
from __future__ import annotations
from typing import Union
from enum import Enum
import logging

log = logging.getLogger(__name__)

class CardType(Enum):
	"""Types of a card."""
	NUMBER0 = ":zero:"
	NUMBER1 = ":one:"
	NUMBER2 = ":two:"
	NUMBER3 = ":three:"
	NUMBER4 = ":four:"
	NUMBER5 = ":five:"
	NUMBER6 = ":six:"
	NUMBER7 = ":seven:"
	NUMBER8 = ":eight:"
	NUMBER9 = ":nine:"

	SKIP = ":track_next:"
	REVERSE = ":arrows_counterclockwise:"
	DRAW = ":new:"
	
	WILD = ":white_large_square::rainbow_flag:"
	WILD_DRAW = ":white_large_square::new:"

	def __str__(self):
		return str(self.value)

	def __repr__(self) -> str:
		return f"<CardType object: {self.name} {self.value}>"

class CardColour(Enum):
	"""Colours of a card."""
	RED = ":red_square:"
	YELLOW = ":yellow_square:"
	GREEN = ":green_square:"
	BLUE = ":blue_square:"

	def __str__(self):
		return str(self.value)

	def __repr__(self) -> str:
		return f"<CardColour object: {self.name} {self.value}>"

class Card:
	"""A UNO Card."""
	def __init__(
		self,
		card_type: CardType,
		card_colour: Union[CardColour, None] = None
	):
		self.type = card_type
		self.colour = card_colour
	
	def __str__(self):
		if self.colour == None:
			return str(self.type)
		return str(self.colour) + str(self.type)

	def __repr__(self):
		col = self.colour.name if self.colour else 'None'
		return f"<Card object: {self.type.name} {col}>"

	def playable(self, other: Card, drawcache: bool = False) -> bool:
		"""Check if this card can be played onto the other card."""
		log.debug(f"Tried playing {repr(self)} onto {repr(other)}")
		if drawcache:
			return (
				self.type == CardType.DRAW and
				other.type == CardType.DRAW or
				other.type == CardType.WILD_DRAW and
				self.colour == other.colour and
				self.type == CardType.DRAW
			)
		return (
			self.colour == other.colour or  # Same colour
			(self.type == other.type and  # not wild on wild
			other.type != CardType.WILD and
			other.type != CardType.WILD_DRAW) or
			(self.type in {CardType.WILD, CardType.WILD_DRAW} and
			not (other.type in {CardType.WILD, CardType.WILD_DRAW}))
		)