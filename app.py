import os
import sys
import json
import requests


class Mailgun:
    @staticmethod
    def send(cls, *args):
        print('a', args)
        print('b', args[::2])
        print('c', args[1::2])
        query = dict(zip(map(lambda a: a[2:], args[::2]), args[1::2]))
        print(query)

        res = requests.post(
            'https://api.mailgun.net/v3/%s/messages' % os.getenv('DOMAIN'),
            auth=('api', 'key-%s' % os.getenv('API_KEY')),
            data=query
        )

        try:
            res.raise_for_status()
        except:
            sys.stderr.write(res.text)
            raise
        else:
            return res.text


if __name__ == '__main__':
    sys.stdout.write(getattr(Mailgun, sys.argv[1])(*sys.argv[1:]))
