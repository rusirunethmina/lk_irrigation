import os
from functools import cached_property

from utils import Time, TimeFormat


class HasTimeMixin:
    @cached_property
    def time_str(self):
        assert self.time_ut
        return TimeFormat("%Y-%m-%d-%H-%M-%S").format(Time(self.time_ut))

    @cached_property
    def year(self):
        return self.time_str[0:4]

    @cached_property
    def year_and_month(self):
        return self.time_str[0:7]

    @cached_property
    def year_and_month_and_day(self):
        return self.time_str[0:10]

    @cached_property
    def part_dir_time(self):
        return os.path.join(
            self.year, self.year_and_month, self.year_and_month_and_day
        )
