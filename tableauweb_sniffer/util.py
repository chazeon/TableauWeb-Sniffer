import json, re

def parse_multipart_content(content: str) -> list:
    '''Parse JS responses that contains multiple JSON object, each initials with
    an integer that represents the length of its content.

    :param content: The body of the JS response to be parsed
    '''
    def parse_content():
        while len(content) != 0:
            res = re.search(r"^(\d+);", content)
            length = int(res.group(1))
            content = content[res.span(0)[1]:]
            yield json.loads(content[:length])
            content = content[length:]
    return list(parse_content())
