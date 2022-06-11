from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security import HTTPAuthorizationCredentials
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND

from .. import models
from ..auth import AuthHandler
from ..db import session

users_router = APIRouter(
    prefix="/users",
    tags=['Users']
)
auth_handler = AuthHandler()

# USER REGISTRATION / SIGUNP
@users_router.post("/signup",  )
def registerUser():
    NotImplemented

# USER LOGIN RETURNS AN ACCESS TOKEN
@users_router.post("/login",  )
def login():
    NotImplemented

# RETURNS EVERY USER IN DB 
@users_router.get("/all",  )
def getUsers():
    NotImplemented

# RETURNS ONE USER (NOT EXPOSING SENSITIVE DATA)
@users_router.get('/',  )
def getUserByEmail():
    NotImplemented

# RETURNS EVERY ADDRESS FOR A GIVEN USER (email as query param)
@users_router.get('/addresses',  )
def getUserAddresses():
    NotImplemented

# FOR USERS TO ADD AN ADDRESS TO THEIR PROFILE
@users_router.post('/addresses',  )
def addAddress():
    NotImplemented
    
# FOR ADMINS TO BAN SOME USER
@users_router.patch("/ban",  )
def banUserByUsername():
    NotImplemented
    
# FOR ADMINS TO RESTORE PERMISSIONS
@users_router.patch("/restore",  )
def restoreUserByUsername():
    NotImplemented