from mantid.kernel import ConfigService
from contextlib import contextmanager

def init():
    global garnet_only
    garnet_only = False

def update(update_value: bool):
    global garnet_only
    garnet_only = update_value
    print(f"filter: {garnet_only}")

def get():
    global garnet_only
    return garnet_only

@contextmanager
def set_log_level(level: str):
    config = ConfigService.Instance()
    current_level = config["logging.loggers.root.level"]
    config.setLogLevel(level, True)
    
    try:
        yield
    finally:
        config.setLogLevel(current_level, True)

    