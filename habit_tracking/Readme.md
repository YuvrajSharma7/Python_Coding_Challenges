# Habit Tracking
 ``Pixela profile page url :- https://pixe.la/@yusharm60``

env setup
```bash
PIXELA_TOKEN= "your_token_here"
PIXELA_USERNAME= "your_username_here"
```

## Create a user profile
```bash
curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
```
## Create a graph definition
```bash
curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
```
## Browse the graph
```bash
https://pixe.la/v1/users/a-know/graphs/test-graph
https://pixe.la/v1/users/yusharm60/graphs/daily-learning 
graph_name: Tech Learning
```