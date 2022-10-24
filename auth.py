from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException

from config import secret


def encode_token(username):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
        'iat': datetime.utcnow(),
        'scope': 'access_token',
        'sub': username
    }
    return jwt.encode(
        payload,
        secret,
        algorithm='HS256'
    )


def decode_token(token):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        if payload['scope'] == 'access_token':
            return payload['sub']
        raise HTTPException(status_code=401, detail='Scope for the token is invalid')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


def encode_refresh_token(username):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=0, hours=10),
        'iat': datetime.utcnow(),
        'scope': 'refresh_token',
        'sub': username
    }
    return jwt.encode(
        payload,
        secret,
        algorithm='HS256'
    )


def decode_refresh_token(refresh_token):
    try:
        payload = jwt.decode(refresh_token, secret, algorithms=['HS256'])
        if payload['scope'] == 'refresh_token':
            username = payload['sub']
            new_token = encode_token(username)
            return new_token
        raise HTTPException(status_code=401, detail='Invalid scope for token')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Refresh token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid refresh token')