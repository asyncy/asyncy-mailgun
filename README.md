# Mailgun as a microservice

Send emails with Mailgun

```coffee
microserive.guide exec -e API_KEY=<KEY> microservice/mailgun send \
  to:'no-reply@domain.com' \
  from:'no-reply@domain.com' \
  subject:'Hello world' \
  text:'Congratulations, you just sent an email with Mailgun! You are truly awesome!'

{
  "id": "<20180327151234.1.B3090E27FAE9FFC8@sandbox13bee1ec0d79497ba1c13733deef6fc2.mailgun.org>",
  "message": "Queued. Thank you."
}
```
