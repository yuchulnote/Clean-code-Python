class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickles, knuts로 새로운 WizCoin 객체를 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 참고: __init__() 메소드는 return문이 존재해서는 안된다.

    def value(self):
        """이 WizCoin 객체에 포함딘 모든 동전의 가치(크넛 단위)"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """그램 단위로 동전의 무게를 반환한다."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
