from http import HTTPStatus
import os

sender = os.environ['SENDER']
subject = "Mock subject"
receiver = os.environ['RECEIVER']
text = "Mock text"

def test_send_request_to_fail(client):
    data = {
        "from": sender,
        "text": text,
        "subject":subject
    }
    url = "/send"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_send_request_from_fail(client):
    data = {
       "to":receiver,
        "text": text,
        "subject":subject
    }
    url = "/send"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_send_request_text_fail(client):
    data = {
        "from": sender,
        "to":receiver,
        "subject":subject
    }
    url = "/send"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_send_request_pass(client):
    data = {
        "from": sender,
        "to":receiver,
        "text": text,
        "subject":subject
    }
    url = "/send"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK
