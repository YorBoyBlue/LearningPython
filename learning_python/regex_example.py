import re

# MATCH CHARACTERS
#   .       - Any Character except new line
#   \d      - Digit (0-9)
#   \D      - Not a digit (0-9)
#   \w      - Word character (a-z, A-Z, 0-9, _)
#   \W      - Not a word character (a-z, A-Z, 0-9, _)
#   \s      - Whitespace (space, tab, newline)
#   \S      - Not whitespace (space, tab, newline)

# ANCHORS (INVISIBLE POSITIONS BEFORE OR AFTER CHARACTERS)
#   \b      - Word boundary (NOT IN the middle or end of a WORD)
#   \B      - Not a word boundary (IN the middle or end of a WORD)
#   ^       - Beginning of a STRING
#   $       - End of a STRING

#
#   []      - Matches one of the characters in the set (in brackets)
#   [^ ]    - Matches one of the characters NOT in the set (NOT in brackets)
#   |       - Either Or
#   ()      - Group

# QUANTIFIERS
#   *       - 0 or more
#   +       - 1 or more
#   ?       - 0 or 1
#   {3}     - Exact number
#   {3,4}   - Range of numbers (Min, Max)


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

ablue.com

321-555-4321
123.555.1234
123*555*1234
800-555-4321
900-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-123-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

print('\nBasic Usage', '=' * 100, '\n')  # ====================================

# Create a pattern to search for (we use a raw string to exclude escape
# characters operations for returned result
pattern = re.compile(r'abc')

# Search for a match using the pattern and pass in the search string
matches = pattern.finditer(text_to_search)

# Print all found matches
for match in matches:
    print(match)

# Print the match result directly from the search string to confirm the result
print(text_to_search[1:4])

print('\nSearching for MetaCharacters', '=' * 83, '\n')  # ====================

# Search for MetaCharacters. Must be escaped in the search because . has a
# special meaning in regex
pattern = re.compile(r'\.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[113:140])

print()

pattern = re.compile(r'ablue\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[142:151])

print('\nSearching for Patterns', '=' * 89, '\n')  # ==========================

# Searching for Patterns using pattern expressions.
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

# Only (800) or (900) numbers
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

# All 3 letter words that end in 'at' but do NOT start with a 'b' (bat)
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('\nSearching for a Range of Chars', '=' * 81, '\n')  # ==================

# Range of characters with the -
pattern = re.compile(r'[1-2]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

pattern = re.compile(r'[^a-zA-Z\s]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# Same as above but with quantifiers
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

print('\nUsing Quantifiers', '=' * 94, '\n')  # ===============================

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

# Same as above but using quantifiers
pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

pattern = re.compile(r'Mr\.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print()

print('\nSearching for emails', '=' * 91, '\n')  # ============================

pattern = re.compile(r'[a-zA-Z0-9.\-]+@[a-zA-Z\-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

print()

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9_.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

print()

print('\nSearching for urls', '=' * 93, '\n')  # ============================

# Find urls
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Substitute out the domain name and top level domain ( something.com )
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls.lstrip())

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(2) + match.group(3))

print()

print('\nOther methods then finditer()', '=' * 82, '\n')  # ===================

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Substitute out the domain name and top level domain ( something.com )
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls.lstrip())

# findall() Returns a list of all matches if no groups are used and a list of
# tuples for each match where each tuple value is a group from the match/search
# pattern
matches = pattern.findall(urls)
for match in matches:
    print(match)

print()

pattern = re.compile(r'Start')

# match() Returns the first match only or None if nothing is found
# It will only search for matches at the beginning of a string
match = pattern.match(sentence)
print(match)

print()

pattern = re.compile(r'sentence')

# search() Returns the first match only or None if nothing is found
# It will search for matches in the entire string
match = pattern.search(sentence)
print(match)

print()

print('\nUsing flags', '=' * 100, '\n')  # ====================================

# Matching patterns that are case insensitive
pattern = re.compile(r'start', re.IGNORECASE)

match = pattern.match(sentence)
print(match)

print()

# Matching patterns that are case insensitive
pattern = re.compile(r'start', re.I)

match = pattern.match(sentence)
print(match)

print()
