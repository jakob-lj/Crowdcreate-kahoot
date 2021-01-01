# Crowdcreate-kahoot

We always have a kahoot each christmas evening. However, this year, noone had prepered a kahoot. Therefor, we wanted to easily create a kahoot fast and also create one that everyone could participate in. 

Therefor, i created this simple I/O terminal interface in order to generate JSON-body for kahoot /drafts-endpoint. 

Simply change questions: [], to the result after running both inp.py and formatter.py. Haven't cleaned the code as it was written in a hurry at christmas eve. 

Kahoot endpoint: https://create.kahoot.it/rest/drafts

Sample body: 
```
{"kahoot":{"cover":"Sample Kahoot","description":"","folderId":"","introVideo":"","language":"Norsk (Bokmål)","metadata":{"resolution":"","moderation":{"flaggedTimestamp":0,"timestampResolution":0},"duplicationProtection":false},"questions":[], "quizType":"quiz","resources":"","title":"Enter kahoot title…","type":"quiz","visibility":0,"creator_username":"","lobby_video":{"youtube":{"id":"","fullUrl":"","startTime":0}},"themeId":null},"kahootExists":false}


```
