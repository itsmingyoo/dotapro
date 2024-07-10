from django.shortcuts import render, redirect
from django.contrib.auth import login
from social_core.backends.steam import SteamOpenId, USER_INFO
# from social_django.views import auth_backend
from social_django.utils import load_strategy, psa
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# https://github.com/python-social-auth/social-core/blob/master/social_core/backends/steam.py
    # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/open_id.py
        # https://github.com/python-social-auth/social-core/blob/master/social_core/backends/base.py


# Login URL: https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?
    # Requires:
        # key=api-key
        # steamid=user_steam_id

# https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=<api-key>&steamids=<player steam id>
# returns response object with user information
# {
    # response: {
        # players: [
            # {
                # steamid: "76561197994850438",
                # communityvisibilitystate: 3,
                # profilestate: 1,
                # personaname: "jaded",
                # profileurl: "https://steamcommunity.com/id/cfoouwu/",
                # avatar: "https://avatars.steamstatic.com/e6093c98aedef51d75262f810131923931120337.jpg",
                # avatarmedium: "https://avatars.steamstatic.com/e6093c98aedef51d75262f810131923931120337_medium.jpg",
                # avatarfull: "https://avatars.steamstatic.com/e6093c98aedef51d75262f810131923931120337_full.jpg",
                # avatarhash: "e6093c98aedef51d75262f810131923931120337",
                # lastlogoff: 1720443496,
                # personastate: 1,
                # realname: "いただきます",
                # primaryclanid: "103582791430030342",
                # timecreated: 1197332104,
                # personastateflags: 0,
                # loccountrycode: "JP"
            # }
        # ]
    # }
# }

# @api_view(['GET'])
def steam_login(request):
    """
    The function `steam_login` redirects the user to the Steam authentication page.

    fetch link as included in the main config/urls.py: http://localhost:8000/steam_login/

    :param request: The `request` parameter in the `steam_login` function is typically an object that
    represents the HTTP request made by a client to the server. It contains information about the
    request such as headers, method, user data, and more. In this context, the `request` parameter is
    likely being used
    :return: A redirect to the social authentication process for the Steam backend.
    """
    print('🙂😶🙄😏🙂 STEAM_LOGIN FN: ARE WE HITTING THIS?')
    return redirect('social:begin', backend='steam')

@psa('social:complete')
def steam_complete(request, backend):
    print(request, backend)



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

# # psa decorator defintion
# def psa(redirect_uri=None, load_strategy=load_strategy):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(request, backend, *args, **kwargs):
#             uri = redirect_uri
#             if uri and not uri.startswith("/"):
#                 uri = reverse(redirect_uri, args=(backend,))
#             request.social_strategy = load_strategy(request)
#             # backward compatibility in attribute name, only if not already
#             # defined
#             if not hasattr(request, "strategy"):
#                 request.strategy = request.social_strategy

#             try:
#                 request.backend = load_backend(
#                     request.social_strategy, backend, redirect_uri=uri
#                 )
#             except MissingBackend:
#                 raise Http404("Backend not found")
#             return func(request, backend, *args, **kwargs)

#         return wrapper

#     return decorator
