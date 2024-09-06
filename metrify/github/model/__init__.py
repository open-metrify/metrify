"""
metrify/github/model/__init__.py

Exports Pydantic model classes for the github module
"""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class PermissionsEnum(str, Enum):
    """Github API PermissionsEnum model for deserialization"""
    # pylint: disable=invalid-name
    read = "read"
    # pylint: disable=invalid-name
    write = "write"


class RepositorySelectionEnum(str, Enum):
    """Github API RepositorySelectionEnum model for deserialization"""
    # pylint: disable=invalid-name
    all = "all"
    # pylint: disable=invalid-name
    selected = "selected"


class Permissions(BaseModel):
    """Github API Permissions model for deserialization"""
    organization_projects: PermissionsEnum
    issues: PermissionsEnum
    metadata: PermissionsEnum
    repository_projects: PermissionsEnum


class AuthResponse(BaseModel):
    """Github API AuthResponse model for deserialization"""
    token: str
    expires_at: datetime
    permissions: Permissions
    repository_selection: RepositorySelectionEnum
