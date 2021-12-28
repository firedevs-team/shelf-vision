from utils.annotations import txt2list


def layer1_events(old, new):
    old_list = txt2list(old)
    new_list = txt2list(new)

    # * events = ['not moved', 'appeared', 'disappeared']
    
    return old_list, new_list