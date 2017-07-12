from AndroidApplication.AndroidApplication import AndroidApplication
from AndroidApplication.AndroidServices import AndroidServices

App= AndroidApplication()
App.each_should_implement()

service =AndroidServices()
service.service_foo()