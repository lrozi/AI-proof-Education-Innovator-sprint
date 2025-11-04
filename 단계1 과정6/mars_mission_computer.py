# mars_mission_computer.py

# 1. random 라이브러리 사용 (제약사항에서 허용)
import random

# 2. DummySensor 클래스 생성
class DummySensor:
    """
    화성 기지 환경 값을 랜덤으로 생성하는 더미 센서 클래스
    """
    
    # 3. 생성자(__init__)에서 멤버 변수(env_values) 초기화
    def __init__(self):
        """
        클래스 인스턴스화 시 env_values 딕셔너리를 초기화합니다.
        """
        # 수행과제 2: 멤버로 env_values 사전 객체 추가
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0,
        }
        print('DummySensor가 초기화되었습니다.')

    # 4. set_env() 메서드 추가
    def set_env(self):
        """
        (수행과제 3, 4)
        주어진 범위 안의 랜덤 값으로 env_values를 업데이트합니다.
        """
        print('센서 값을 랜덤으로 생성합니다...')
        
        # 정수형 범위 값 생성
        self.env_values['mars_base_internal_temperature'] = random.randint(18, 30)
        self.env_values['mars_base_external_temperature'] = random.randint(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.randint(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)
        
        # 실수형 범위 값 생성 (uniform 사용)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4.0, 7.0)
    
    # 5. get_env() 메서드 추가
    def get_env(self):
        """
        (수행과제 5)
        현재 env_values 딕셔너리를 반환합니다.
        """
        print('현재 센서 값을 반환합니다.')
        return self.env_values


# 6. 메인 실행 부분
if __name__ == '__main__':
    
    # 7. DummySensor 클래스를 ds라는 이름으로 인스턴스화 (수행과제 6)
    print('--- 미션 컴퓨터 시뮬레이터 시작 ---')
    ds = DummySensor()

    # 8. set_env()와 get_env() 차례로 호출 (수행과제 7)
    
    # 값 설정하기
    ds.set_env()
    
    # 값 가져오기
    current_env = ds.get_env()
    
    # 9. 결과 확인
    print('\n--- 현재 화성 기지 환경 값 ---')
    # 딕셔너리를 보기 좋게 출력
    for key, value in current_env.items():
        # 실수 값은 소수점 3자리까지만 포맷팅
        if isinstance(value, float):
            print(f'{key}: {value:.3f}')
        else:
            print(f'{key}: {value}')
            
    print('---------------------------------')