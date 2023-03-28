import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def main(args):
    tokens = num_tokens_from_string("tiktoken is great!", "cl100k_base")

    return {
        "statusCode": 200,
        "body": tokens
    }