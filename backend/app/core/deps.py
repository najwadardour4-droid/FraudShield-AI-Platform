from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import decode_token

security = HTTPBearer(auto_error=False)


async def get_current_user_email(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> str | None:
    if not credentials:
        return None
    return decode_token(credentials.credentials)


async def require_auth(email: str | None = Depends(get_current_user_email)) -> str:
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return email


# Re-export for routers
__all__ = ["get_db", "get_current_user_email", "require_auth", "AsyncSession"]
