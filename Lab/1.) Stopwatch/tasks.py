from fractions import Fraction
from stopwatch import Stopwatch
from money import Money


class Task:
    """Task to run in parallel"""
    def __init__(self, size: int) -> None:
        """
        Arguments:
            size {int} -- size of the task
        """

        self.limit = size

def tasktimer(task):
    '''Print the message and the time taken by the function'''

    def run():

        print(f'Task {task}')
        stopwatch = Stopwatch()
        stopwatch.start()
        result = task.run()
        stopwatch.stop()
        print('Finished')
        print(f'The sum is {result}')
        print(f'Elapsed time: {stopwatch.elapsed*1000:.6f} ms')
    return run


class Task1(Task):
    """add integger from 1 to n (include)"""

    def __repr__(self) -> str:
        """Return a string representation of the task"""

        return f'Summing integers from 1 to {self.limit:,}'
    __str__ = __repr__  # make an string to same as represent method

    @tasktimer
    def run(self) -> int:
        """Run the task"""
        return sum(range(1, self.limit + 1))


class Task2(Task):
    """add money from 1 Baht to n Baht"""

    def __repr__(self) -> str:
        """Return a string representation of the task"""

        return f'Summing money from 1 Baht to {self.limit:,} Baht'
    __str__ = __repr__

    @tasktimer
    def run(self) -> Money:
        """Run the task"""

        summation = Money(0, 'Baht')
        for i in range(1, self.limit + 1):
            summation += Money(i, 'Baht')
        return summation


class Task3(Task):
    """add the first n th term of harmonic series"""

    def __repr__(self) -> str:
        """Return a string representation of the task"""

        return f'Summing 1/1 + 1/2 + ... + 1/{self.limit:,}'

    @tasktimer
    def run(self) -> float:
        """Run the task"""

        return sum(1/i for i in range(1, self.limit + 1))


class Task4(Task):
    '''add the first n th term of harmonic series
       using Fraction class'''

    def __repr__(self) -> str:
        """Return a string representation of the task"""

        return f'Summing 1/1 + 1/2 + ... + 1/{self.limit:,}'
    __str__ = __repr__

    @tasktimer
    def run(self) -> float:
        """Run the task"""

        summation = sum(Fraction(1, i) for i in range(1, self.limit + 1))
        return float(summation)



Task1(1_000_000).run()


# if __name__ == '__main__':
#     all_task = [Task1(1_000_000), Task2(1_000_000), Task3(1_000_000), Task4(10_000)]

#     print()
#     for i, task in enumerate(all_task):
#         print(f'Doing Task{i+1}..')
#         tasktimer(task)
#         print()
