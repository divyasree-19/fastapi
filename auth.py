# When you go to /auth/register/ → you join the school
# When you go to /auth/login/ → you get your ID card (token)


from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta,timezone
from models.author_model import Author

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Password hashing helpers
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        author_id = payload.get("id")
        if author_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await Author.get(id=author_id)
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# Route: Register user
@router.post("/register/")
async def register_user(name: str, age: int, password: str):
    hashed_pw = get_password_hash(password)
    user = await Author.create(name=name, age=age, password=hashed_pw)
    return {"msg": "User registered successfully", "id": user.id}

# Route: Login user
@router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await Author.get_or_none(name=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
