from dataclasses import dataclass
from functools import cached_property

from lk_irrigation.base.AbstractTable import AbstractTable
from lk_irrigation.core.Basin import Basin


@dataclass
class River(AbstractTable):
    basin_name: str
    location_names: list[str]

    @cached_property
    def basin(self):
        return Basin.from_name(self.basin_name)
