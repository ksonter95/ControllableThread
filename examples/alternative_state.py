import cthread
import logging
import queue as q
import time

# Configure the logger #
logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

class AlternativeState(cthread.ControllableThread):

    def __init__(self, queue):
        # 1. Initialise ControllableThread with additional kwargs #
        cthread.ControllableThread.__init__(self,
                name="AlternativeStateThread",
                queue=queue,
                ALT1=self._alt1_callback,
                ALT2=self._alt2_callback
        )

    def _started_callback(self):
        pass

    def _active_callback(self):
        pass

    def _paused_callback(self):
        pass

    def _resumed_callback(self):
        pass

    def _killed_callback(self):
        pass

    def _alt1_callback(self):
        # 2. Add any alternative state specific code here #
        pass

    def _alt2_callback(self):
        # 2. Add any alternative state specific code here #
        pass

if __name__ == "__main__":

    queue = q.PriorityQueue()
    quickstart = AlternativeState(queue)

    quickstart.start() # Start the thread.  MUST be called first #
    time.sleep(1)

    quickstart.alt(name="ALT1") # ALT1 state #
    time.sleep(1)

    quickstart.alt(name="ALT2") # ALT2 state #
    time.sleep(1)

    quickstart.kill() # Kill the thread #