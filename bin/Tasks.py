import json


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load()

    def load(self, filepath="tasks.json"):
        """Loads tasks to Task Manager

        This method loads the JSON file storing the tasks, then converts each one to <Task> object and then finally
        appends all of them to the array attribute of the Task Manager sorted by their priority.

        :param filepath: String for path to the file where the tasks are stored.
        :type filepath: str
        :return: None
        :rtype: None
        """
        try:
            with open(filepath, "r", encoding="utf-8") as task_file:
                tasks_json = json.load(task_file)
            self.tasks = [Task(task["name"], task["priority"], task["steps"]) for task in tasks_json]
            self.sort()
        except FileNotFoundError:
            pass

    def save(self, filepath="tasks.json"):
        """Saves tasks to JSON file.

        This method saves tha tasks from the Task Manager in a <dicc> array to finally store it in a JSON file.

        :param filepath: String for path to the file where the tasks are stored.
        :type filepath: str
        :return: None
        :rtype: None
        """
        tasks_json = [task.to_dicc() for task in self.tasks]
        with open(filepath, "w", encoding="utf-8") as task_file:
            json.dump(tasks_json, task_file, ensure_ascii=False)

    def show(self):
        """Lists all the tasks loaded in the Task Manager

        :return: None
        :rtype: None
        """
        i = 0
        print()
        for task in self.tasks:
            print("\t", i + 1, ". ", task.name, "(", task.priority, ")")
            i += 1

    def sort(self):
        """Sorts the tasks

        Sorts the task object array of the Task Manager.

        :return: None
        :rtype: None
        """
        self.tasks = sorted(self.tasks, key=lambda k: k.priority, reverse=True)

    def assign(self, task=None):
        """Saves a Task

        This method saves a <Task> in the Task Manager array, updates the JSON file with it and sort the array by their
        priority.

        :param task: <Task> objetc with specified information, default value is None to ask for its info via console.
        :type task: <Task>
        :return:
        """
        if task is None:
            print("\n*** Add Task ***")
            name = input("Name of the task?: ")
            try:
                priority = int(input("Priority of the task (1-->5): "))
            except ValueError:
                priority = 1
            steps = []
            while 1:
                step = input("Add step #" + str(len(steps) + 1) + " (Enter empty to finish): ")
                if step:
                    steps.append(step)
                else:
                    break
            self.tasks.append(Task(name, priority, steps))
            self.save()
            self.sort()
            print("*"*16)
        else:
            self.tasks.append(task)
            self.save()
            self.sort()

    def delete(self, task=None):
        """Deletes a Task

        This method deletes a <Task> in the Task Manager array, updates the JSON file with it and sort the array by
        their priority.

        :param task: <Task> objetc with specified information, default value is None to ask for its info via console.
        :type task: <Task>
        :return:
        """
        if task is None:
            print("\n*** Delete Task ***\n\nSelect a task index to delete:")
            self.show()
            while 1:
                try:
                    i = int(input("\nIndex? (0 to cancel): ")) - 1
                    if i >= 0:
                        print("Deleted task \"" + self.tasks.pop(i).name + "\".")
                        self.save()
                    elif i == -1:
                        print("Deletion canceled. ")
                    else:
                        raise IndexError
                    break
                except (ValueError, IndexError) as e:
                    print("\n\"" + str(i+1) + "\" is not a valid task index.", type(e))
            print("*"*19)
        else:
            pass

    def action(self, option):
        """Derives the action for the selected option

        Derives the action for the selected option.

        :param option: String containing the option selected by the user.
        :type option: Str
        :return: None
        :rtype: None
        """
        try:
            i = int(option) - 1
            try:
                task = self.tasks[i]
                print("\n*** Steps for", task.name, "P" + str(task.priority), "***")
                s = 0
                for step in task.steps:
                    s += 1
                    print("\t", s, ". ", step)
                    input()
                print("*********************" + len(task.name)*"*")
            except IndexError as e:
                print("\n\"" + str(i) + "\" is not a valid task index.", type(e))
        except ValueError:
            if option in (":A", "A"):
                self.assign()
            elif option in (":D", "D"):
                self.delete()
            elif option in (":Q", "Q"):
                pass
            else:
                print("\n\"" + option + "\" is not a valid option.")


class Task:
    def __init__(self, name="def", priority=1, steps=["steps here", "steps there"]):
        self.name = name
        self.priority = priority
        self.steps = steps

    def to_dicc(self):
        """Turns the task object into a dictionary

        :return: The dictionary containing all attributes of the task.
        :rtype: Dicc
        """
        return {"name": self.name, "priority": self.priority, "steps": self.steps}
