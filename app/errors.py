class TaskFlowError(Exception):
    """Base class for app errors."""


class ValidationError(TaskFlowError):
    pass


class TaskNotFoundError(TaskFlowError):
    pass
