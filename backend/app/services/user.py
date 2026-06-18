import uuid
from app.models.user import User
from app.core.security import get_password_hash, verify_password


def create_user(data, db):
    new_user = User(
        id=str(uuid.uuid4()),
        email=data.email,
        password=get_password_hash(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(data, db):
    return db.query(User).filter(User.email == data.email).first()


def authenticate_user(data, db):
    user = get_user(data, db)
    if not user:
        return None
    if not verify_password(data.password, user.password):
        return None
    return user