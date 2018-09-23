"""Route Searcher
"""

from typing import (
    Dict,
    NamedTuple,
)

import route.exceptions


class Station(NamedTuple):
    name: str


class Router:
    def __init__(self) -> None:
        self._routes: Dict[Station, Station] = {}

    def cross_link(self, station_a: Station, station_b: Station) -> None:
        """Register given stations cross linked.
        """
        self._routes[station_a] = station_b
        self._routes[station_b] = station_a

    def is_linked(self, from_station: Station, to_station: Station) -> bool:
        """Return True if from_station connected to to_station.
        """
        try:
            return self._routes[from_station] == to_station
        except KeyError:
            raise route.exceptions.UnknownStationError()
