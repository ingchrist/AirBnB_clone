#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class wzqCity(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    wzqstate_id = ""
    wzqname = ""
