from sqlalchemy import select
from app.models.roles import Role
from app.repository.role import insert_role, delete_role as delete_role_repo, fetch_role_by_id, fetch_roles, update_role
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class RoleService:
    def __init__(self, db: AsyncSession):
        self.db = db
