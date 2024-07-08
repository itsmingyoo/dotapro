from django.shortcuts import render
from social_core.backends.steam import SteamOpenId

# https://github.com/python-social-auth/social-core/blob/master/social_core/backends/steam.py
    # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/open_id.py
        # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/base.py


# This an example with google oauth
# @psa("social:complete")
# def ajax_auth(request, backend):
#     """AJAX authentication endpoint"""
#     if isinstance(request.backend, BaseOAuth1):
#         token = {
#             "oauth_token": request.REQUEST.get("access_token"),
#             "oauth_token_secret": request.REQUEST.get("access_token_secret"),
#         }
#     elif isinstance(request.backend, BaseOAuth2):
#         token = request.REQUEST.get("access_token")
#     else:
#         raise HttpResponseBadRequest("Wrong backend type")
#     user = request.backend.do_auth(token, ajax=True)
#     login(request, user)
#     data = {"id": user.id, "username": user.username}
#     return HttpResponse(json.dumps(data), mimetype="application/json")
