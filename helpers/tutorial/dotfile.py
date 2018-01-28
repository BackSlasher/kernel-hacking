#!/usr/bin/env python3

from typing import Optional
import os
import json

DOTFILE_DEFAULT_NAME = '.tutorial'

def _locate_dotfile() -> str:
    root = os.path.abspath(os.sep)
    current_dir = os.getcwd()
    while current_dir != root:
        # Try and find dotfile here
        dotfile_name = os.path.join(current_dir, DOTFILE_DEFAULT_NAME)
        if os.path.exists(dotfile_name):
            return dotfile_name
        pass
        # Move one stage up
        current_dir = os.path.dirname(current_dir)
    raise Exception('Could not find a dotfile')

class Dotfile(object):
    # fields:
    # * guide py path
    # * episode ID
    # * mission ID
    def __init__(self, guide_path:str=None, episode_id:str=None, mission_id:str=None):
        self.guide_path = guide_path
        self.episode_id = episode_id
        self.mission_id = mission_id
        pass

    def to_json(self) -> str:
        return json.dumps({
            'guide_path': self.guide_path,
            'episode_id': self.episode_id,
            'mission_id': self.mission_id,
        })

    @classmethod
    def from_json(klass, json_str:str):
        dic = json.loads(json_str)
        return Dotfile(
            guide_path=dic['guide_path'],
            episode_id=dic['episode_id'],
            mission_id=dic['mission_id'],
        )

    @classmethod
    def create(klass, dotfile_path:str=None):
        dotfile_path = dotfile_path or DOTFILE_DEFAULT_NAME
        dotfile = Dotfile()
        dotfile.save(dotfile_path)

    @classmethod
    def read(klass, dotfile_path:str=None):
        dotfile_path = dotfile_path or _locate_dotfile()
        with open(dotfile_path, 'r') as f:
            data_str = f.read()
        return klass.from_json(data_str)

    def save(self, dotfile_path:str=None):
        dotfile_path = dotfile_path or _locate_dotfile()
        data_str = self.to_json()
        with open(dotfile_path, 'w') as f:
            f.write(data_str)


