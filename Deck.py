import json

from Card import Card


class Deck:
    def __init__(self, title):
        self.title = title
        self.cards = []

    def addCard(self, question, answer):
        card = Card(question, answer)
        self.cards.append(card)

    def train(self):
        if not self.cards:
            print("Колода пуста!")
            return
        for idx, val in enumerate(self.cards):
            print(f"Вопрос номер {idx + 1}: {val.question}")
            print("Ваш ответ: ", end="")

            answer = input().strip().lower()
            corr_answer = val.answer.strip().lower()
            if answer == corr_answer:
                print("👏🏼 Совершенно верно")
                val.success_rate += 1
                continue
            print("🙅🏻 Неправильно")

    def toDict(self):
        return {"title": self.title, "cards": [card.toDict() for card in self.cards]}

    @staticmethod
    def fromDict(data):
        deck = Deck(data["title"])
        deck.cards = [Card.fromDict(c) for c in data["cards"]]
        return deck
