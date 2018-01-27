#!/usr/bin/env python3

"""
A single chapter in a guide
"""

class Guide(object):
    def get_episodes(self) -> List[Episode]:
        # TODO throw
        return []

class Episode(object):
    # Episode materials
    def show_content(self) -> None:
        # TODO throw
        return

    def get_missions(self) -> List[Mission]:
        # TODO throw
        return []


class Mission(object):
    # Print what the mission is
    def show_content(self) -> None:
        pass

    # Modify the FS (e.g.) in order for the task to be complete
    def solve(self) -> None:
        pass

    # Make sure the task is solved, e.g. by running a small unittest
    def verify(self) -> bool:
        pass

