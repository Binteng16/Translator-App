# knowledge_base.py

class KnowledgeBase:
    def __init__(self):
        self.rules = {
            'en-id': ['selamat', 'pagi', 'terima kasih'],
            'en-es': ['hola', 'gracias', 'buenos'],
            'en-fr': ['bonjour', 'merci', 'bien'],
            'en-de': ['hallo', 'danke', 'gut'],
            'en-zh': ['你好', '谢谢', '早上好']
        }

    def get_language_recommendation(self, text):
        recommendations = {}
        for language, keywords in self.rules.items():
            recommendations[language] = sum(word in text for word in keywords)

        # Get language with the highest keyword match
        recommended_language = max(recommendations, key=recommendations.get)
        return recommended_language