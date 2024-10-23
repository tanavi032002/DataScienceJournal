import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(content):
    # Set of stop words for filtering
    stop_words_set = set(stopwords.words('english'))
    tokenized_words = word_tokenize(content.lower())

    # Remove stop words from the tokenized words
    filtered_words = [word for word in tokenized_words if word.isalpha() and word not in stop_words_set]

    # Calculate word frequencies
    word_frequency = nltk.FreqDist(filtered_words)

    # Split the text into sentences
    sentence_list = sent_tokenize(content)

    # Check if there are sentences to score
    if not sentence_list:
        return "No sentences found to summarize."

    # Dictionary to hold scores for each sentence
    sentence_score_map = {}
    for sentence in sentence_list:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequency:
                # Score sentences based on the frequency of words
                if sentence not in sentence_score_map:
                    sentence_score_map[sentence] = word_frequency[word]
                else:
                    sentence_score_map[sentence] += word_frequency[word]

    # Sort sentences by score in descending order
    if not sentence_score_map:
        return "No sentences scored for summary."

    top_sentence_list = sorted(sentence_score_map, key=sentence_score_map.get, reverse=True)[:3]  # Select top 3 sentences

    # Generate summary from the top sentences
    summary_result = ' '.join(top_sentence_list)

    # Clean up sentence endings for improved readability
    summary_result = summary_result.replace(";", ".").replace(".", ". ")

    return summary_result.strip()

# Load reviews from the specified input file
input_file_path = 'input.txt'  # Update with your actual file path
with open(input_file_path, 'r') as input_file:
    review_lines = input_file.readlines()

# Classify reviews based on simple sentiment analysis
positive_review_list = []
neutral_review_list = []
negative_review_list = []

# Basic sentiment classification
for line in review_lines:
    cleaned_review = line.strip()
    if "fantastic" in cleaned_review or "love" in cleaned_review or "great" in cleaned_review:
        positive_review_list.append(cleaned_review)
    elif "decent" in cleaned_review or "average" in cleaned_review or "okay" in cleaned_review:
        neutral_review_list.append(cleaned_review)
    else:
        negative_review_list.append(cleaned_review)

# Summarize reviews in each sentiment category
positive_reviews_combined = "\n".join(positive_review_list)
neutral_reviews_combined = "\n".join(neutral_review_list)
negative_reviews_combined = "\n".join(negative_review_list)

positive_review_summary = summarize_text(positive_reviews_combined)
neutral_review_summary = summarize_text(neutral_reviews_combined)
negative_review_summary = summarize_text(negative_reviews_combined)

# Output the summaries
print("Summary of Positive Reviews:", positive_review_summary)
print("Summary of Neutral Reviews:", neutral_review_summary)
print("Summary of Negative Reviews:", negative_review_summary)
