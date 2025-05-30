class Card:
    def __init__(self, question, answer, success_rate=0):
        self.question = question
        self.answer = answer
        self.success_rate = success_rate

    def toDict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "success_rate": self.success_rate,
        }

    @staticmethod
    def fromDict(data):
        return Card(data["question"], data["answer"], data["success_rate"])
