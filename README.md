# Pytardo

## Architecture

* The `Poller` class continously polls arduino to get the readings.
* Readings are logged through the `log()` method of `loggers` objects that are added to the `Poller` through the `Poller.add_logger()` method.
* Readings are checked against user-defined conditions by the `Monitor` class. Monitor objects can be added to the `Poller` through the `Poller.add_monitor()` method. 
* `Monitor` objects prepare a list of readings that meet one or more conditions (and hence might raise warnings) and pass it to `callbacks` objects, together with all the current readings, through their `react()` method. Note that `react()` is always called, even when there are no warnings. In this way `callbacks` objects can update their internal status after each reading (useful, for instance, to keep track of values oscillating around a threshold).
* Conditions are parsed and managed by ad-hoc objects that have a `is_met` method (see `conditions.py`).  

## Dependencies

* pySerial
* python-daemon
* MySQL-python