import time


class Stopwatch:
    """A timer that you can start and stop."""

    def __init__(self):
        """Initialize a new stopwatch in the stopped state.

        Attributes:
            time_start: the time when the stopwatch was started
            time_stop: the time when the stopwatch was stopped
            state: the current state of the stopwatch

        """

        self.RUNNING = RunningState(self)
        self.STOPPED = StoppedState(self)

        self.set_state(self.STOPPED)
        self.time_start = 0
        self.time_stop = None

    def set_state(self, state):
        """change the state of the stopwatch

        Attributes:
            state: the new state of the stopwatch

        Raises:
            TypeError: if the state is not a StopwatchState
        """
        if not isinstance(state, StopwatchState):
            raise TypeError("state must be a StopwatchState")
        self.state = state

    def start(self):
        """Start the stopwatch if it is stopped. Has no effect if already running."""
        self.state.start()

    def stop(self):
        """Stop the stopwatch if it is running. No effect if already stopped."""
        self.state.stop()

    def reset(self):
        """Reset the stopwatch. Has no effect if already stopped."""
        self.state.reset()

    @property
    def running(self):
        """Get the state of the stopwatch. True if stopwatch is running.

        Returns:
            True if stopwatch is running, False otherwise
        """
        return self.state == self.RUNNING

    @property
    def elapsed(self):
        """Get the elapsed time between start and stop, or start and current time.

        Returns:
            the elapsed time in seconds, or 0 if the stopwatch is not running

        Raises:
            ValueError if the stopwatch is running
        """
        return self.state.elasped

class StopwatchState:
    def __init__(self, stopwatch: Stopwatch):
        self.stopwatch = stopwatch

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    @property
    def elasped(self):
        """Return the elasped time in seconds."""
        return 0


class RunningState(StopwatchState):
    """Behavior of the stopwatch when it is in the running state.
    The only attribute is a reference to the Stopwatch (context),
    which the state uses to get attributes of the Stopwatch.
    Do not define any other attributes here.
    """

    def start(self):
        """Start the stopwatch.
        This method should not be called in the running state.
        """

        raise RuntimeError("Stopwatch is already running")

    def stop(self):
        """Reset the stopwatch.
        This method should not be called in the stopped state.
        """

        self.stopwatch.time_stop = time.perf_counter()
        self.stopwatch.set_state(self.stopwatch.STOPPED)

    def reset(self):
        """Reset the stopwatch.
        This method should not be called in the running state.
        """
        raise RuntimeError("Stopwatch is running")

    @property
    def elasped(self):
        """Return the elapsed time in seconds.
        """
        return time.perf_counter() - self.stopwatch.time_start


class StoppedState(StopwatchState):
    """Behavior of the stopwatch when it is in the stopped state.
    The only attribute is a reference to the Stopwatch (context), 
    which the state uses to get attributes of the Stopwatch.
    Do not define any other attributes here.
    """

    def start(self):
        """Start the stopwatch.
        This method should not be called in the stopped state.
        """

        # set the state of wtopwatch to running
        self.stopwatch.time_start = time.perf_counter() - self.elasped
        self.stopwatch.set_state(self.stopwatch.RUNNING)

    def stop(self):
        """Reset the stopwatch.
        This method should not be called in the stopped state.
        """
        raise RuntimeError("Stopwatch is already stopped")

    def reset(self):
        """Reset the stopwatch.
        This method should not be called in the stopped state.
        """
        self.stopwatch.time_start = self.stopwatch.time_stop = time.perf_counter()

    @property
    def elasped(self):
        """Return the elapsed time in seconds.
        """
        try:
            return self.stopwatch.time_stop - self.stopwatch.time_start
        except Exception:
            return 0
