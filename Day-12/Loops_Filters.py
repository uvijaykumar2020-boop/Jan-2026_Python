"""
Types of loops
For loop - Iterate over sequences (lists, tuples, dictionaries, strings, etc
While Loops - Keep Executing as long as condition is True
"""
numbers = [29, 85, 69, 96, 999, 36, 19, 30]
for i in numbers:
    print(f" Your Lucky Number is ==> {i}")

# Filtering
Comments = ['AI is Awesome', 'Hate Programming', 'Love Programming', 'AI is Future', 'Love to Learn', 'AI is Bad']
for i in Comments:
    if 'Love' in i or "Awesome" in i or 'Future' in i:
        print(f" Valuable Comments of AI - {i}")
else:
    print(f" Bad Comments of AI - {i}")
    