# Pytardo

## Architecture

* The `Poller` class continously polls arduino to get the readings.
* Readings are logged through the `log()` method of `loggers` objects that are added to the `Poller` through the `Poller.add_logger()` method.
* Readings are checked against user-defined conditions by the `Monitor` class. Monitor objects can be added to the `Poller` through the `Poller.add_monitor()` method. 
* `Monitor` objects prepare a list of readings that meet one or more conditions (called warnings) and pass it to `callbacks` objects through their `react()` method.

## Dependencies

* pySerial
* python-daemon
