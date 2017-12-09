from lab7.collector import action


@action(call_always=True, priority=50)
def eventFromInnerFolder1():
    print "eventFromInnerFolder (priority 50)"


@action(call_always=True, priority=100)
def eventFromInnerFolder2():
    print "eventFromInnerFolder (priority 100)"


@action(every_k=2, max_called_times=1)
def eventFromInnerFolder3():
    print "every 2  (max_called_times = 1)"


@action(index_list=[3])
def eventFromInnerFolder4():
    print "non critical action"
    raise ValueError


# @action(index_list=[4], is_critical=True)
# def eventFromInnerFolder4():
#     print "critical error"
#     raise ValueError
