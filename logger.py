from mantid.kernel import Logger as lg
from mantid.kernel import amend_config
from settings import set_log_level

logger = lg("GARNET")
garnet_only = False

class Logger(lg):
    def __init__(self, name="GARNET", filter=garnet_only):
        self.logger = lg(name)
        self.garnet_only = filter
        print(f"filter: {filter}")

    def warning(self, message):
        if self.garnet_only:
            with set_log_level("warning"):
                self.logger.warning(message)
        else:
            self.logger.warning(message)

    def error(self, message):
        # error message is always shown
        self.logger.error(message)

    def debug(self, message):
        if self.garnet_only:
            with set_log_level("debug"):
                self.logger.debug(message)
        else:
            self.logger.debug(message)

    def information(self, message):
        if self.garnet_only:
            with set_log_level("information"):
                self.logger.information(message)
        else:
            self.logger.information(message)

    def notice(self, message):
        if self.garnet_only:
            with set_log_level("notice"):
                self.logger.notice(message)
        else:
            self.logger.notice(message)

    def accumulate(self, message):
        self.logger.accumulate(message)

    def flush(self):
        self.logger.flush()

    def flushDebug(self):
        self.logger.flushDebug()