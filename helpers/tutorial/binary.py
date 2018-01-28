#!/usr/bin/env python3

import argparse
from dotfile import Dotfile

def navigate(dotfile:Dotfile, guide:str=None, episode:str=None, mission:str=None) -> None:
    if not (guide or episode or mission):
        print('Current guide:', dotfile.guide_path)
        print('Current episode:', dotfile.episode_id)
        print('Current mission:', dotfile.mission_id)
    if guide:
        # TODO change the current guide
        pass
    if episode:
        # TODO change the current episode
        pass
    if mission:
        # TODO change the current mission
        pass

def make_args():
    parser = argparse.ArgumentParser(description='Interactive tutorial')

    parser.add_argument('-f', '--file', help='Override file location', required=False)

    commands = parser.add_subparsers(dest='command')

    init_parser = commands.add_parser('init', help='Create a new dotfile')

    navigate_parser = commands.add_parser('navigate', help='Change what guide/episode/mission you currently are')
    navigate_parser.add_argument('--guide', type=str, required=False)
    navigate_parser.add_argument('--episode', type=str, required=False)
    navigate_parser.add_argument('--mission', type=str, required=False)

    content_parser = commands.add_parser('content', help='Show info')


    solve_parser = commands.add_parser('solve', help='If you cant solve the problem yourself, use this to apply the solution')

    verify_parser = commands.add_parser('verify', help='Check if you solved the mission')


    return parser
    

def main():
    parser = make_args()
    args = parser.parse_args()

    if args.command == 'init':
        Dotfile.create()
    else:
        my_dotfile = Dotfile.read(args.file)
        if not args.command:
            navigate(my_dotfile)
        if args.command == 'navigate':
            navigate(my_dotfile, args.guide, args.episode, args.mission)
        else:
            # Ensure we have a guide, episode, mission here
            if args.command == 'content':
                pass
            elif args.command == 'solve':
                pass
            elif args.command == 'verify':
                pass
            else:
                raise Exception('unknown command')



main()
