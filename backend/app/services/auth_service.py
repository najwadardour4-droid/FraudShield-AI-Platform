from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password, verify_password
from app.models.user import User

DEFAULT_USERS = [
    {"email": "admin@fraudshield.ai", "password": "admin123", "full_name": "Platform Admin", "role": "admin"},
    {"email": "najwa@fraudshield.ai", "password": "admin123", "full_name": "Najwa — Credit Card", "role": "analyst"},
    {"email": "ferdaouss@fraudshield.ai", "password": "admin123", "full_name": "Ferdaouss — Phishing", "role": "analyst"},
    {"email": "alae@fraudshield.ai", "password": "admin123", "full_name": "Alae — Document", "role": "analyst"},
]


async def seed_users(db: AsyncSession) -> None:
    for u in DEFAULT_USERS:
        existing = await db.execute(select(User).where(User.email == u["email"]))
        user = existing.scalar_one_or_none()
        if user:
            # Update password and role if already exists to match DEFAULT_USERS
            user.hashed_password = hash_password(u["password"])
            user.role = u["role"]
            user.full_name = u["full_name"]
            continue
        db.add(
            User(
                email=u["email"],
                full_name=u["full_name"],
                hashed_password=hash_password(u["password"]),
                role=u["role"],
            )
        )
    await db.commit()


async def authenticate(db: AsyncSession, email: str, password: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email, User.is_active.is_(True)))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
