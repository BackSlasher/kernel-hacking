#!/usr/bin/env python3

from . import objects
from typing import Optional
import subprocess
import os
import fnmatch

"""
Solves organization by using directory struct:

my_guide.py <-- mark as autoload
episodes/
    EPISODE_ID/
        content*
        missions/
            MISSION_ID/
               solve*
               content*
               verify*
"""
def _find_files(base_directory: str, glob: str, is_directory:bool = False) -> List[str]:
    # Return the first file/dir matching a glob, if there is any
    files = os.listdir(base_directory)
    matching_files = [f for f in files if os.path.isdir(f) == is_directory]
    matching_files = [f for f in matching_files if fnmatch.fnmatch(f, glob)]
    return matching_files


def _find_single_file(base_directory: str, glob: str) -> str:
    # Same as above, but only return the first
    matching_files = _find_files(base_directory=base_directory, glob=glob, is_directory=False)
    if not matching_files:
        # TODO better exception
        raise Exception("Found no matching files")
    return matching_files[0]


def _open_file(file_path: str) -> None:
    # https://ubuntuforums.org/showthread.php?t=1003198
    # http://nullege.com/codes/search/os.filestart
    # https://unix.stackexchange.com/questions/340531/launch-executable-with-xdg-open
    if os.name == 'posix':
        subprocess.Popen(['xdg-open', file_path])
    else:
        raise Exception('Not sure how to open file')

def _open_file_in_gui(base_directory: str, glob: str) -> None:
    # Execute the first match for a glob
    # If none are found, raise
    picked_file = _find_single_file(base_directory=base_directory, glob=glob)
    #TODO log
    print('opening file', picked_file)
    _open_file(picked_file)

def AutoGuide(objects.Guide):
    def __init__(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))

    def get_episodes(self) -> List[objects.Episode]:
        episode_directory = os.path.join(self.directory, 'episodes')
        return [
            AutoEpisode(d) for d
            in _find_files(
                episode_directory,
                glob='*',
                is_directory=True
            )
        ]

class AutoEpisode(objects.Episode):
    def __init__(self, directory: str):
        #Remember the directory for this episode
        self.directory = directory

    def show_content(self) -> None:
        _open_file_in_gui(self.directory, 'content*')

    def get_missions(self) -> List[objects.Mission]:
        mission_directory = os.path.join(self.directory, 'missions')
        return [
            AutoMission(d) for d
            in _find_files(
                mission_directory,
                glob='*',
                is_directory=True
            )
        ]


class AutoMission(objects.Mission):
    def __init__(self, directory: str):
        self.directory = directory

    def show_content(self) -> None:
        _open_file_in_gui(self.directory, 'content*')

    def solve(self) -> None: 
        solving_file =  _find_single_file(self.directory, 'solve*')
        subprocess.check_call(solving_file)

    def verify(self) -> bool:
        verification_file = _find_single_file(self.directory, 'verify*')
        verification_reuslt = subprocess.call(verification_file)
        return verification_result == 0

