from collector import action


@action(index_list=[1, 3])
def eventListProvided():
    print "eventListProvided"
    pass


@action(call_always=True, name='eventWithName')
def eventAlways():
    print "eventAlways eventWithName"
    pass
