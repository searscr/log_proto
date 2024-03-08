rst
.. _log-levels-guide:

=============================
Log Levels and Best Practices
=============================

Logging is a crucial aspect of software development for tracking and troubleshooting issues. 
Different log levels provide a hierarchy of severity to help developers identify and address problems effectively. 
Below are common log levels and guidelines on when to use them:

Fatal
-----
- **Description:** The most severe log level, indicating a critical error that leads to application termination.
- **When to Use:**
  - Use `fatal` when the application cannot proceed due to a catastrophic failure.
  - Examples include unrecoverable system errors or critical resource unavailability.

Error
-----
- **Description:** Signifies a significant error condition that does not require immediate application termination.
- **When to Use:**
  - Use `error` for unexpected errors that impact the application's functionality but can be handled gracefully.
  - Examples include database connection failures, file not found errors, or invalid user input.

Warning
-------
- **Description:** Indicates potential issues or situations that might lead to errors in the future.
- **When to Use:**
  - Use `warning` for conditions that may cause problems but do not necessarily disrupt the application.
  - Examples include deprecated API usage, low disk space warnings, or non-critical configuration issues.

Notice
------
- **Description:** Provides information about normal, but significant, application events.
- **When to Use:**
  - Use `notice` for noteworthy events that may be of interest but are not considered errors.
  - Examples include successful startup messages, important configuration changes, or periodic system checks.

Information
------------
- **Description:** General information that can be useful for tracking the application's behavior.
- **When to Use:**
  - Use `information` to log routine events, status updates, or informational messages.
  - Examples include user authentication, external API interactions, or state changes within the application.

Debug
-----
- **Description:** Detailed information useful for debugging and troubleshooting during development.
- **When to Use:**
  - Use `debug` for low-level details, variable values, or function call traces.
  - Include `debug` statements during development and testing to identify and resolve issues.

.. code-block:: python

    from logger import Logger

    logger = Logger("FUNCTION_NAME", settings.get())

    # Log a debug message
    logging.debug('This is a debug message')

    # Log an informational message
    logging.information('This is an informational message')

    # Log a warning message
    logging.warning('This is a warning message')

    # Log an error message
    logging.error('This is an error message')

    
