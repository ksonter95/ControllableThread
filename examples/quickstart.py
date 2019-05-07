import cthread
import logging
import queue as q
import time

# Configure the logger #
logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

class Quickstart(cthread.ControllableThread):

    def _started_callback(self):
        # Add any state specific code here (and remove the 'pass') #
        pass

    def _active_callback(self):
        # Add any state specific code here (and remove the 'pass') #
        pass

    def _paused_callback(self):
        # Add any state specific code here (and remove the 'pass') #
        pass

    def _resumed_callback(self):
        # Add any state specific code here (and remove the 'pass') #
        pass

    def _killed_callback(self):
        # Add any state specific code here (and remove the 'pass') #
        pass

if __name__ == "__main__":

    queue = q.PriorityQueue()
    quickstart = Quickstart(name="QuickstartThread", queue=queue)

    quickstart.start() # Start the thread.  MUST be called first #
    time.sleep(1)

    quickstart.pause() # Pause the thread. #
    time.sleep(1)

    quickstart.resume() # Resume the thread #
    time.sleep(1)

    quickstart.reset() # Reset the thread #
    time.sleep(1)

    quickstart.kill() # Kill the thread #