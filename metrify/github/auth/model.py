from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class PermissionsEnum(str, Enum):
    read = "read"
    write = "write"


class RepositorySelectionEnum(str, Enum):
    all = "all"
    selected = "selected"


class Permissions(BaseModel):
    organization_projects: PermissionsEnum
    issues: PermissionsEnum
    metadata: PermissionsEnum
    repository_projects: PermissionsEnum


class AuthResponse(BaseModel):
    token: str
    expires_at: datetime
    permissions: Permissions
    repository_selection: RepositorySelectionEnum
