from flask import jsonify

# chart = {
#     'labels': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue'],
#     'series': [2, 6, 2, 4, 0, 0, 3, 2, 1, 0, 0, 0, 3, 6, 1]
# }
t={'labels':[1,2], 'series':[2,3,4]}
print(jsonify(t))

a = {'url': 'https://api.github.com/repos/yglukhov/nimx/commits/b737dd9510d7faa1b85c4fb23bde3f05a58a34e3',
     'html_url': 'https://github.com/yglukhov/nimx/commit/b737dd9510d7faa1b85c4fb23bde3f05a58a34e3',
     'committer': {'url': 'https://api.github.com/users/yglukhov', 'html_url': 'https://github.com/yglukhov',
                   'following_url': 'https://api.github.com/users/yglukhov/following{/other_user}', 'site_admin': False,
                   'followers_url': 'https://api.github.com/users/yglukhov/followers',
                   'avatar_url': 'https://avatars.githubusercontent.com/u/6962409?v=3',
                   'subscriptions_url': 'https://api.github.com/users/yglukhov/subscriptions',
                   'starred_url': 'https://api.github.com/users/yglukhov/starred{/owner}{/repo}', 'id': 6962409,
                   'login': 'yglukhov', 'gravatar_id': '', 'type': 'User',
                   'organizations_url': 'https://api.github.com/users/yglukhov/orgs',
                   'repos_url': 'https://api.github.com/users/yglukhov/repos',
                   'gists_url': 'https://api.github.com/users/yglukhov/gists{/gist_id}',
                   'received_events_url': 'https://api.github.com/users/yglukhov/received_events',
                   'events_url': 'https://api.github.com/users/yglukhov/events{/privacy}'},
     'commit': {
        'url': 'https://api.github.com/repos/yglukhov/nimx/git/commits/b737dd9510d7faa1b85c4fb23bde3f05a58a34e3',
        'committer': {'email': 'yglukhov@users.noreply.github.com', 'name': 'Yuriy Glukhov',
                      'date': '2016-03-22T09:38:26Z'},
        'author': {'email': 'yglukhov@users.noreply.github.com', 'name': 'Yuriy Glukhov',
                   'date': '2016-03-22T09:38:26Z'}, 'comment_count': 0,
        'tree': {'url': 'https://api.github.com/repos/yglukhov/nimx/git/trees/db2098cfd0c7abe9a5aae68f9e3247711ef54b23',
                 'sha': 'db2098cfd0c7abe9a5aae68f9e3247711ef54b23'},
        'message': 'Merge pull request #78 from yglukhov/mouseover\n\nmouse over callbacks'},
     'comments_url': 'https://api.github.com/repos/yglukhov/nimx/commits/b737dd9510d7faa1b85c4fb23bde3f05a58a34e3/comments',
     'parents': [{'url': 'https://api.github.com/repos/yglukhov/nimx/commits/8707579d6201c5b6dd0e11c6280c7d6eaa76e966',
                  'html_url': 'https://github.com/yglukhov/nimx/commit/8707579d6201c5b6dd0e11c6280c7d6eaa76e966',
                  'sha': '8707579d6201c5b6dd0e11c6280c7d6eaa76e966'},
                 {'url': 'https://api.github.com/repos/yglukhov/nimx/commits/70ea945c2acaff1afc3ca629548ae2ad261126f1',
                  'html_url': 'https://github.com/yglukhov/nimx/commit/70ea945c2acaff1afc3ca629548ae2ad261126f1',
                  'sha': '70ea945c2acaff1afc3ca629548ae2ad261126f1'}],
     'sha': 'b737dd9510d7faa1b85c4fb23bde3f05a58a34e3',
     'author': {'url': 'https://api.github.com/users/yglukhov', 'html_url': 'https://github.com/yglukhov',
                'following_url': 'https://api.github.com/users/yglukhov/following{/other_user}', 'site_admin': False,
                'followers_url': 'https://api.github.com/users/yglukhov/followers',
                'avatar_url': 'https://avatars.githubusercontent.com/u/6962409?v=3',
                'subscriptions_url': 'https://api.github.com/users/yglukhov/subscriptions',
                'starred_url': 'https://api.github.com/users/yglukhov/starred{/owner}{/repo}', 'id': 6962409,
                'login': 'yglukhov', 'gravatar_id': '', 'type': 'User',
                'organizations_url': 'https://api.github.com/users/yglukhov/orgs',
                'repos_url': 'https://api.github.com/users/yglukhov/repos',
                'gists_url': 'https://api.github.com/users/yglukhov/gists{/gist_id}',
                'received_events_url': 'https://api.github.com/users/yglukhov/received_events',
                'events_url': 'https://api.github.com/users/yglukhov/events{/privacy}'}}
print(a['commit']['committer']['date'])
