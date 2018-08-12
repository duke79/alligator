from enum import Enum


class UserPermission(Enum):
    """Permissions defined here must be in sync with the database entries"""
    ALL = 1  # Everything permitted
