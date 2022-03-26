import requests
from flask import Blueprint, current_app, redirect, session, request
from base64 import b64encode
MW_ENDPOINT = 'https://meta.wikimedia.org/w/index.php?title=Special:OAuth'
MW_CALLBACK = 'oob'
from requests_oauthlib import OAuth1Session

oauth = Blueprint('oauth', __name__)
@oauth.get('/login')
def login():
    consumer_key = current_app.config['CONSUMER_KEY']
    consumer_secret = current_app.config['CONSUMER_SECRET']
    oauth_session = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        callback_uri=MW_CALLBACK
    )
    request_token = oauth_session.fetch_request_token(MW_ENDPOINT + '/initiate')
    session['resource_owner_key'] = request_token.get('oauth_token')
    session['resource_owner_secret'] = request_token.get('oauth_token_secret')
    authorization_url = oauth_session.authorization_url(MW_ENDPOINT + '/authorize')
    #return session
    return redirect(authorization_url)
@oauth.get('/callback')
def callback():
    consumer_key = current_app.config['CONSUMER_KEY']
    consumer_secret = current_app.config['CONSUMER_SECRET']
    oauth_session = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        callback_uri=MW_CALLBACK
    )
    oauth_session.parse_authorization_response(request.url)
    oath_token = oauth_session.fetch_access_token(MW_ENDPOINT + '/token')
    session['access_token'] = oath_token.get('oauth_token')
    session['access_token_secret'] = oath_token.get('oauth_token_secret')
    return redirect('/')