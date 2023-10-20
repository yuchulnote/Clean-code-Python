"""하노이 탑, 작성자: 유철 GitHub: https://github.com/yuchulnote
원판 더미를 움직이는 퍼즐 게임"""

import copy
import sys

TOTAL_DISKS = 5  # 원판이 많을수록 퍼즐은 더 어려워진다

# A탑에 모든 원판이 놓인 상태로 시작한다
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """하노이 탑 게임을 실행한다."""
    print(
        """하노이 탑, 작성자: 유철 GitHub: https://github.com/yuchulnote
        
탑이 쌓인 원판을 한 번에 하나씩 다른 탑으로 이동한다.
큰 원판은 작은 원판 위에 놓일 수 없다.

추가 정보는 https://en.wikipedia.org/wiki/Tower_of_Hanoi 를 참고한다.
"""
    )

    """towers 딕셔너리 키 "A", "B", "C" 와 탑에 쌓인 원판을 표현하는 리스트
    형태의 값을 갖고 있다. 리스트는 다양한 크기와 원판을 표현하는 정수를 포함하며,
    리스트 [5, 4, 3, 2, 1]가 완성된 탑을 표현한다.
    리스트 []는 탑에 쌓인 원판이 없음을 나타낸다. 리스트 [1,3]은 작은 원판 위에
    큰 원판이 있으며, 유효하지 않은 구성이다. 리스트[3,1]이 허용되는 이유는
    작은 원판이 큰 원판 상단에 올라갈 수 있기 때문이다."""
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}
