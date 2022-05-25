"""Start the stopwatch application. """

from stopwatch import Stopwatch
from stopwatch_ui import StopwatchUI


if __name__ == '__main__':
    stopwatch = Stopwatch()
    stopwatch_ui = StopwatchUI(stopwatch)
    stopwatch_ui.run()
