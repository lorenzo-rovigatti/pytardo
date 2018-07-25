# Pytardo

## Arduino setup

The Arduino board should be set up so that it prints out a line containing comma-separated readings whenever something gets written to the serial port. An output example would be:

	T1 = 20, T2 = 32, c = 0.1

## Architecture

* The `Poller` class continously polls arduino to get the readings.
* Readings are logged through the `log()` method of `loggers` objects that are added to the `Poller` through the `Poller.add_logger()` method.
* Readings are checked against user-defined conditions by the `Monitor` class. Monitor objects can be added to the `Poller` through the `Poller.add_monitor()` method. 
* `Monitor` objects prepare a list of readings that meet one or more conditions (and hence might raise warnings) and pass it to `callbacks` objects, together with all the current readings, through their `react()` method. Note that `react()` is always called, even when there are no warnings. In this way `callbacks` objects can update their internal status after each reading (useful, for instance, to keep track of values oscillating around a threshold).
* Conditions are parsed and managed by ad-hoc objects that have a `is_met` method (see `conditions.py`).

## Configuration

`pytardo.py` or `pytardod.py` expect a single argument that specifies the path of the file that contains the configuration. Example configuration files can be found in the `examples/` folder.

## Dependencies

* pySerial
* python-daemon
* MySQL-python

## Acknowledgements

* The `dummyserial.py` package is heavily based on [dummyserial](https://github.com/ampledata/dummyserial)
