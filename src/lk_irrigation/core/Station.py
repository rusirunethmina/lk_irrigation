from dataclasses import dataclass
from functools import cached_property

from lk_irrigation.base.AbstractTable import AbstractTable
from lk_irrigation.core.Location import Location
from lk_irrigation.core.River import River


@dataclass
class Station(Location, AbstractTable):
    river_name: str
    alert_level: float
    minor_flood_level_m: float
    major_flood_level_m: float
    district_id: str

    @cached_property
    def river(self):
        return River.from_name(self.river_name)

    @cached_property
    def water_level_unit(self) -> str:
        if self.name in ["Nagalagam Street"]:
            return "ft"
        return "m"
