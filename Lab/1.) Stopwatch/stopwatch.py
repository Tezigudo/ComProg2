import time


class Stopwatch:
    """A timer that you can start and stop."""

    def __init__(self):
        """Initialize a new stopwatch in the stopped state.

            Attributes:
                running: True if the stopwatch is running, False otherwise
                time_start: the time when the stopwatch started
                time_stop: the time when the stopwatch stopped

        """
        self._running = False
        self.time_start = 0
        self.time_stop = None

    @property
    def running(self):
        """Get the state of the stopwatch. True if stopwatch is running.

        Returns:
            True if stopwatch is running, False otherwise
        """
        return self._running

    def start(self):
        """Start the stopwatch if it is stopped. Has no effect if already running."""
        if not self.running:
            self._running = True  # set the state of wtopwatch to running
            self.time_start = time.perf_counter()

    def stop(self):
        """Stop the stopwatch if it is running. No effect if already stopped."""
        if self.running:
            self._running = False  # set the state of wtopwatch to stopped
            self.time_stop = time.perf_counter()

    @property
    def elapsed(self):
        """Get the elapsed time between start and stop, or start and current time.

        Returns:
            the elapsed time in seconds, or 0 if the stopwatch is not running

        Raises:
            ValueError if the stopwatch is running
        """
        if self.running:
            return time.perf_counter() - self.time_start
        try:
            return self.time_stop - self.time_start
        except AttributeError:
            raise ValueError('Stopwatch is not running')
