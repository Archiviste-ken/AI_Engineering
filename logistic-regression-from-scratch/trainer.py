
from dataset import X, y
from model import LogisticRegression
from loss import binary_cross_entropy


class Trainer:

    def __init__(self):
        self.model = LogisticRegression()

    def train(self):

        for epoch in range(100):

            for x, actual in zip(X, y):

                prediction = self.model.predict(x[0])

                loss = binary_cross_entropy(
                    actual,
                    prediction
                )

                print(loss)