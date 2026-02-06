import sys
import inspect

def monitor_memory():
    # 현재 실행 중인 함수의 스택 프레임 객체를 가져옵니다.
    frame = inspect.currentframe()
    
    print(f"--- 메모리 비교 ---")
    print(f"1. 현재 스택 프레임 자체의 크기: {sys.getsizeof(frame)} bytes")
    
    # 리스트에 정수 1개를 담았을 때
    sample_list = [1]
    print(f"2. 정수 1개가 든 리스트의 크기(Heap): {sys.getsizeof(sample_list)} bytes")
    
    # 리스트에 정수 10개를 담았을 때
    large_list = list(range(10))
    print(f"3. 정수 10개가 든 리스트의 크기(Heap): {sys.getsizeof(large_list)} bytes")

monitor_memory()
