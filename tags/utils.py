from kiwipiepy import Kiwi
from collections import Counter

kiwi = Kiwi()

emotion_lexicon = ['기쁜', '슬픈', '화나는', '불안한', '행복한', '차분하게', '우울한', '좌절스런', '짜증나는', '분노', '절망스러운', "속상한"]

def extract_keywords(text, n=3):
    try:
        text = text.strip()
        analysis = kiwi.analyze(text)

        emotions = [word.form for word in analysis[0][0] if word.form in emotion_lexicon]

        if not emotions:
            return []

        counter = Counter(emotions)
        most_common_emotions = counter.most_common(n)
        keywords = [emotion for emotion, _ in most_common_emotions]

        return keywords
    except Exception as e:
        print(f"Error extracting emotion keywords: {e}")
        return []
