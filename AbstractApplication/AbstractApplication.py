from abc import ABCMeta, abstractmethod


class AbstractApplication(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def each_should_implement(self):
        pass

    def foo(self):
        return 'fff'
