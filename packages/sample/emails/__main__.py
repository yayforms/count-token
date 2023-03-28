import tiktoken

def main(args):
    enc = tiktoken.get_encoding("cl100k_base")
    assert enc.decode(enc.encode("hello world")) == "hello world"
    return {
        "statusCode": 200,
        "body": "no twilio verified phone numbers provided"
    }