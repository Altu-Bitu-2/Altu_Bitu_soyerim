#2776 암기왕 ver1
import sys  #파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline  #input변수에 문자열을 받음

# ver1) 셋을 이용한 풀이입니다.


t = int(input())  #t를 int()를 이용하여 정수로 형변환을 하고 개행문자를 없앰

for _ in range(t):  #테스트케이스의 개수만큼 반복함
    # 입력
    n = int(input())  #'수첩1'에 적어놓은 정수의 개수를 입력으로 받는다
    note1 = set(map(int, input().split()))  #여러개의 정수를 입력받아 set 자료형으로 저장한다(set 자료형: 중복x, 순서x)
    m = int(input())   #'수첩2'에 적어놓은 정수의 개수를 입력으로 받는다
    note2 = list(map(int, input().split()))  #여러개의 정수를 입력받아 리스트 자료형으로 저장한다(list: 중복ㅇ, 순서ㅇ)

    # note2에 있는 숫자를 하나씩 꺼내 note1에 있는지 비교합니다.
    for num in note2: #'수첩2'에 적힌 정수 개수만큼 반복한다
        if num in note1:  #만약 '수첩2'에 적힌 수가 '수첩1'에 있으면 1을 프린트한다
            print(1)  #프린트1
        else:     #만약 '수첩2'에 적힌 수가 '수첩1'에 없으면 0을 프린트한다
            print(0)  #프린트0
