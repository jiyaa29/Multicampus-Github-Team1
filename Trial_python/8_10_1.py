# [workshop] 통장 만들기
# 우리가 흔히 쓰는 통장을 클래스로 만들고 여기에 돈을 넣어다 빼본다
# 우선 통장 클래스를 만들고 그 통장 클래스를 테스트할 수 있는 테스트 클래스를 만드는 순서로 진행반다.
# 본 워크샵에는 클래스를 생성할 때 잠조할 수 있는 클래스 다이어그램을 제공한다.

from ast import main


class Account(object):
    def __init__(self, custId, custName, accountNumber, balance):
        self.custId = custId
        self.custName = custName
        self.accountNumber = accountNumber
        self.balance = balance
    def addBalance(self, balance):
        print("{}원을 입금합니다.".format(balance))
        if balance <=0:
            print("입금할 금액이 없습니다.")
        else:
            self.balance += balance
            print("{}원이 입금되었습니다.".format(balance))
            print("잔액: {}".format(self.balance))

    def substractBalance(self, balance):
        print("{}원을 출금합니다.".format(balance))
        if balance <=0:
            print("출금할 금액이 없습니다.")
        elif self.balance < balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= balance
            print("{}원이 출금되었습니다.".format(balance))

    def printAccount(self):
        print("고객 아이디: {}".format(self.custId))
        print("고객 이름: {}".format(self.custName))
        print("고객 계좌번호: {}".format(self.accountNumber))
        print("잔액: {}".format(self.balance))

    def getMenuItem(self):
        print("1. 입금")
        print("2. 출금")
        print("9. 프로그램 종료")
        return input("메뉴를 선택하세요: ")

    def getAccount(self):
        return self.accountNumber

    def __str__(self) -> str:
        return "고객 아이디: {}\n고객 이름: {}\n고객 계좌번호: {}\n잔액: {}".format(self.custId, self.custName, self.accountNumber, self.balance)

    @staticmethod
    def getAccount():
        return int(input("금액을 입력하세요: "))
