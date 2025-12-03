feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

extra = int(input())
current_sno = len(feedback_data['S_No']) + 1

for _ in range(extra):
    name = input()
    fb = input()
    rating = int(input())
    feedback_data['S_No'].append(current_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(fb)
    feedback_data['Rating'].append(rating)
    current_sno += 1

cleaned_feedbacks = []
punct = ".,!?"

for fb in feedback_data['Feedback']:
    for p in punct:
        fb = fb.replace(p, " ")
    fb = " ".join(fb.split())
    fb = fb.lower()
    cleaned_feedbacks.append(fb)

feedback_data['Feedback'] = cleaned_feedbacks

def count_word_in_feedbacks(word):
    count = 0
    for fb in feedback_data['Feedback']:
        if word.lower() in fb:
            count += 1
    return count

print(count_word_in_feedbacks("good"))
print(count_word_in_feedbacks("poor"))
print(count_word_in_feedbacks("excellent"))

print(feedback_data)

avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(round(avg_rating, 2))

word_counts = [len(fb.split()) for fb in feedback_data['Feedback']]
max_index = word_counts.index(max(word_counts))

print(feedback_data['S_No'][max_index])
print(feedback_data['Name'][max_index])
print(feedback_data['Feedback'][max_index])

unique_words = set()
for fb in feedback_data['Feedback']:
    unique_words.update(fb.split())

print(sorted(unique_words))

combined = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))

sorted_data = sorted(combined, key=lambda x: x[3], reverse=True)

for entry in sorted_data:
    print(entry)
