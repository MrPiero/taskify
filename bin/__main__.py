#!/usr/bin/env python

from bin.Tasks import TaskManager


def main():
    manager = TaskManager()
    print("=== WELCOME TO TASKIFY ALPHA===")
    option_menu = ""
    while option_menu not in (":Q", "Q"):
        if manager.tasks:
            manager.show()
            print("\n\t[#].  Print steps of task #.")
            print("\t[:a]. Add task")
            print("\t[:d]. Delete task")
            print("\t[:q]. Exit")
            option_menu = input("\nChoose your option: ").upper()
            manager.action(option_menu)
        else:
            print("\nYou have no tasks saved. Add new tasks to start.")
            manager.assign()
    print("\nFinished Taskify, bye!\n")


if __name__ == '__main__':
    main()
