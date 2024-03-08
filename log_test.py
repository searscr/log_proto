from mantid.simpleapi import CreateSampleWorkspace
from mantid.kernel import amend_config

from logger import Logger
import settings


def test_logging():
    logger = Logger("SUB_FUNC", settings.get())
    CreateSampleWorkspace(OutputWorkspace="sample")
    logger.debug("Test Debug Statement")
    logger.information("Test Information Statement")
