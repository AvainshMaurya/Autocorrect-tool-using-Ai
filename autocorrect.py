from textblob import TextBlob

print("=== AI Autocorrect Tool ===")

text = input("Enter Text: ")

blob = TextBlob(text)

corrected = blob.correct()

print("\nCorrected Text:")
print(corrected)
