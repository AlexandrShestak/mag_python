import imp
import os
import sys

registry = []


class Collector(object):
    """
    Class which will collect  events. All events must me marked with action decorator.
    Collector will scan all python file in provided folder names list.
    It will not register the same action twice (if f.e. one folder is listed two times).
    All actions will collected in current module in registry variable and then returned.
    """
    def collect(self, folder_names):
        registered_modules = set()
        for folder in folder_names:
            for subdir, dirs, files in os.walk(folder):
                for file_name in files:
                    full_file_path = os.path.join(subdir, file_name)
                    if file_name.endswith('.py') and full_file_path not in registered_modules:
                        imp.load_source("source", full_file_path)
                        registered_modules.add(full_file_path)

        return registry


class Action(object):
    """
    Action class which can be configured in different ways.
    """
    def __init__(self, func, every_k, index_list, call_always, priority, name, max_called_times, is_critical):
        self.func = func
        self.every_k = every_k
        index_list.sort()
        self.index_list = index_list
        self.call_always = call_always
        self.priority = priority
        self.name = name
        self.max_called_times = max_called_times
        self.was_called_times = 0
        self.is_critical = is_critical


def action(every_k=0, index_list=[], call_always=False, priority=0, name='', max_called_times=0, is_critical=False):
    def inner_decorator(func):
        sys.modules['collector'].registry.append(Action(func, every_k, index_list, call_always, priority,
                                                        name if name else func.__name__, max_called_times, is_critical))

        def wrapper():
            return func

        return wrapper

    return inner_decorator
