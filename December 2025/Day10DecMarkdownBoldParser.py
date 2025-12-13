import re

def parse_bold(markdown):
    # No espacios después del delimitador de apertura
    # No espacios antes del delimitador de cierre
    pattern = r'(\*\*|__)(\S(?:.*?\S)?)\1'
    return re.sub(pattern, r'<b>\2</b>', markdown)

print(parse_bold("__This is also bold __"))