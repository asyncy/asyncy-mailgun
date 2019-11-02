# _Mailgun_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
[![Build Status](https://travis-ci.com/omg-services/mailgun.svg?branch=master)](https://travis-ci.com/omg-services/mailgun)
[![codecov](https://codecov.io/gh/omg-services/mailgun/branch/master/graph/badge.svg)](https://codecov.io/gh/omg-services/mailgun)
Send emails with Mailgun

## Direct usage in [Storyscript](https://storyscript.io/):

##### Send Mail
```coffee
>>> mailgun send to:"receiverEmail" from:"senderEmail" subject:"emailSubject" text:"messageBody"
{"id": "operationID","message": "Queued. Thank you."}
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Send Mail
```shell
$ oms run send -a to=<RECEIVER_EMAIL> -a from=<SENDER_EMAIL> -a subject=<EMAIL_SUBJECT> -a text=<MESSAGE_BODY> -e API_KEY=<API_KEY> -e DOMAIN=<DOMAIN>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/mailgun/blob/master/LICENSE).

