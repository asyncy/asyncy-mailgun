# Mailgun for Asyncy

![Asyncy container](https://img.shields.io/badge/asyncy_container-ready-brightgreen.svg?style=for-the-badge)
[![Docker Build Status](https://img.shields.io/docker/build/asyncy/asyncy-mailgun.svg?style=for-the-badge)](https://hub.docker.com/r/asyncy/asyncy-mailgun/)
![Docker Stars](https://img.shields.io/docker/stars/asyncy/asyncy-mailgun.svg?style=for-the-badge)

Send emails with Mailgun

```coffee
res = mailgun send
  --to 'no-reply@domain.com'
  --from 'no-reply@domain.com'
  --subject 'Hello world'
  --text 'Congratulations, you just sent an email with Mailgun! You are truly awesome!'
```

```js
res = {
  "id": "<20180327151234.1.B3090E27FAE9FFC8@sandbox13bee1ec0d79497ba1c13733deef6fc2.mailgun.org>",
  "message": "Queued. Thank you."
}
```
