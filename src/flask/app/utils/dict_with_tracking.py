import sys

_NUL = object()  # unique object

if sys.version_info[0] > 2:
    def iterkeys(d, **kw):
        return iter(d.keys(**kw))
else:
    def iterkeys(d, **kw):
        return d.iterkeys(**kw)


class TrackingDict(dict):
    """ Dict subclass which tracks all changes in a _changelist attribute.
    Ref: https://stackoverflow.com/q/5903720/973425
    """

    def __init__(self, *args, **kwargs):
        super(TrackingDict, self).__init__(*args, **kwargs)
        self.clear_changelist()
        for key in sorted(iterkeys(self)):
            self._changelist.append(AddKey(key, self[key]))

    def clear_changelist(self):  # additional public method
        self._changelist = []

    def __setitem__(self, key, value):
        modtype = ChangeKey if key in self else AddKey
        super(TrackingDict, self).__setitem__(key, value)
        self._changelist.append(modtype(key, self[key]))

    def __delitem__(self, key):
        super(TrackingDict, self).__delitem__(key)
        self._changelist.append(RemoveKey(key))

    def clear(self):
        deletedkeys = self.keys()
        super(TrackingDict, self).clear()
        for key in sorted(deletedkeys):
            self._changelist.append(RemoveKey(key))

    def update(self, other=_NUL, **kwargs):
        if other is not _NUL:
            otherdict = dict(other)  # convert to dict if necessary
            changedkeys = set(k for k in otherdict if k in self)
            super(TrackingDict, self).update(other)
            for key in sorted(iterkeys(otherdict)):
                if key in changedkeys:
                    self._changelist.append(ChangeKey(key, otherdict[key]))
                else:
                    self._changelist.append(AddKey(key, otherdict[key]))

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default  # will append an AddKey to _changelist
        return self[key]

    def pop(self, key, default=_NUL):
        if key in self:
            ret = self[key]  # save value
            self.__delitem__(key)
            return ret
        elif default is not _NUL:  # default specified
            return default
        else:  # not there & no default
            var = self[key]  # allow KeyError to be raised

    def popitem(self):
        key, value = super(TrackingDict, self).popitem()
        self._changelist.append(RemoveKey(key))
        return key, value


# change-tracking record classes

class DictMutator(object):
    def __init__(self, key, value=_NUL):
        self.key = key
        self.value = value

    def __repr__(self):
        return '%s(%r%s)' % (self.__class__.__name__, self.key,
                             '' if self.value is _NUL else ': ' + repr(self.value))


class AddKey(DictMutator): pass


class ChangeKey(DictMutator): pass


class RemoveKey(DictMutator): pass


if __name__ == '__main__':
    import traceback
    import sys

    td = TrackingDict({'one': 1, 'two': 2})
    print('changelist: {}'.format(td._changelist))

    td['three'] = 3
    print('changelist: {}'.format(td._changelist))

    td['two'] = -2
    print('changelist: {}'.format(td._changelist))

    td.clear()
    print('changelist: {}'.format(td._changelist))

    td.clear_changelist()

    td['newkey'] = 42
    print('changelist: {}'.format(td._changelist))

    td.setdefault('another')  # default None value
    print('changelist: {}'.format(td._changelist))

    td.setdefault('one more', 43)
    print('changelist: {}'.format(td._changelist))

    td.update(zip(('another', 'one', 'two'), (17, 1, 2)))
    print('changelist: {}'.format(td._changelist))

    td.pop('newkey')
    print('changelist: {}'.format(td._changelist))

    try:
        td.pop("won't find")
    except KeyError:
        print("KeyError as expected:")
        traceback.print_exc(file=sys.stdout)
    print('...and no change to _changelist:')
    print('changelist: {}'.format(td._changelist))

    td.clear_changelist()
    while td:
        td.popitem()
    print('changelist: {}'.format(td._changelist))
