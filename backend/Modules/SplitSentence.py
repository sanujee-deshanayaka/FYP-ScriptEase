import re

def split_sentence(sentence):
    enter_pattern = re.compile(r'\bEnter\b\s*(?P<test_data>\w+)\s*\b(in)\b\s*(?P<element>\w+)')
    click_pattern = re.compile(r'\bClick\b\s*(?P<element>\w+)?\s')

    enter_match = enter_pattern.match(sentence)
    if enter_match:
        return 'Enter', enter_match.group('element'), enter_match.group('test_data')

    click_match = click_pattern.match(sentence)
    if click_match:
        return 'Click', click_match.group('element'), 'Null'

    return "Invalid input"
