class FailedDependencyException(Exception):
    def __init__(self, message: str = 'Failed to fetch data from the external service'):
        super().__init__(message)
        self.message = message
