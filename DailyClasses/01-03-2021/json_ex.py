import json

x = '''{
  "login": "vipulshah31120",
  "id": 75607031,
  "node_id": "MDQ6VXNlcjc1NjA3MDMx",
  "avatar_url": "https://avatars.githubusercontent.com/u/75607031?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/vipulshah31120",
  "html_url": "https://github.com/vipulshah31120",
  "followers_url": "https://api.github.com/users/vipulshah31120/followers",
  "following_url": "https://api.github.com/users/vipulshah31120/following{/other_user}",
  "gists_url": "https://api.github.com/users/vipulshah31120/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/vipulshah31120/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/vipulshah31120/subscriptions",
  "organizations_url": "https://api.github.com/users/vipulshah31120/orgs",
  "repos_url": "https://api.github.com/users/vipulshah31120/repos",
  "events_url": "https://api.github.com/users/vipulshah31120/events{/privacy}",
  "received_events_url": "https://api.github.com/users/vipulshah31120/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 3,
  "public_gists": 0,
  "followers": 0,
  "following": 0,
  "created_at": "2020-12-07T07:56:51Z",
  "updated_at": "2021-02-02T18:34:27Z"
}'''

vipulDictionary = json.loads(x)
print(type(vipulDictionary))
print(vipulDictionary['avatar_url'])


vipulJson = json.dumps(vipulDictionary)
print(type(vipulJson))
print(vipulJson)