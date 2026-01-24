import sys
import traceback
from PyQt6.QtCore import QRunnable, pyqtSlot

def WorkerSignals():
    raise NotImplementedError


class threadWorker(QRunnable):
    #Worker thread with signals for handling exceptions
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        
        @pyqtSlot()
        def run(self):
            #Run the function with passed args and kwargs
            try:
                result = self.fn(*self.args, **self.kwargs)
            except Exception as e:
                traceback_str = ''.join(traceback.format_tb(e.__traceback__))
                exctype, value = sys.exc_info()[:2]
                self.signals.error.emit((exctype, value, traceback_str))
            else:
                self.signals.result.emit(result)
            finally:
                self.signals.finished.emit()