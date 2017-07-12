from abc import ABCMeta, abstractmethod

class AbstractServices(object):

    @abstractmethod
    def each_should_implement(self):
        pass

    def service_foo(self):
        print('service foo')
        return 'service foo'

