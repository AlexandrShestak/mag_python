from collector import Collector
from collector import Action
from collections import defaultdict
import logging as logging


class EventManager(object):
    """
    Event Manager class which stored actions. Actions can be populated by calling collect method
    which will use Collector class to register actions. Also Actions can ve registered and removed by
    register and remove_action methods.
    All actions are stored in dictionary where key it is time when action need to be executed, when action is executed
    then new key is generated (so every step only actions which are needed on current step are checked).
    """
    def __init__(self):
        self.current_index = 0
        self.events_bus = defaultdict(list)

    def __register_event__(self, event):
        if event.call_always:
            self.events_bus[self.current_index].append(event)
        elif event.every_k:
            self.events_bus[event.every_k].append(event)
        elif event.index_list:
            self.events_bus[event.index_list.pop(0)].append(event)
        else:
            raise ValueError

    def collect(self, folder_names):
        collector = Collector()
        registry = collector.collect(folder_names)
        for event in registry:
            self.__register_event__(event)

    def notify(self):
        for event in sorted(self.events_bus[self.current_index], key=lambda x: x.priority, reverse=True):
            try:
                event.func.__call__()
            except Exception as e:
                if event.is_critical:
                    raise e
                else:
                    logging.error("Error during action execution. Action name: %s" % event.name)

            if event.call_always:
                self.events_bus[self.current_index + 1].append(event)
            elif event.every_k:
                event.was_called_times += 1
                if event.max_called_times and event.was_called_times < event.max_called_times:
                    self.events_bus[self.current_index + event.every_k].append(event)
            elif event.index_list:
                self.events_bus[event.index_list.pop(0)].append(event)
        print self.current_index
        self.current_index += 1

    def register(self, func, call_always, every_k, index_list, priority=0, name='', max_called_times=0,
                 is_critical=False):
        event = Action(func, every_k, filter(lambda x: x > self.current_index, index_list), call_always, priority,
                       name if name else func.__name__, max_called_times, is_critical)
        self.__register_event__(event)

    def remove_action(self, name):
        self.events_bus =\
            defaultdict(list, {k: filter(lambda x: x.name != name, v) for k, v in self.events_bus.iteritems()})


def registered_by_hands_event():
    print 'registered_by_hands_event'


if __name__ == '__main__':
    event_manager = EventManager()
    event_manager.collect(['../lab7'])

    event_manager.notify()
    event_manager.notify()
    event_manager.notify()
    event_manager.notify()
    event_manager.notify()
    event_manager.register(registered_by_hands_event, True, None, [1], 75)
    event_manager.notify()
    event_manager.remove_action('eventWithName')
    event_manager.notify()
