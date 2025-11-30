from dataclasses import dataclass

from lk_irrigation.base.AbstractTable import AbstractTable


@dataclass
class Basin(AbstractTable):
    code: str
