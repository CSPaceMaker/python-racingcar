import random

class Race:
    def create_cars(car_names, self):
        """
        입력된 이름에 맞춰 자동차 객체를 생성.
        각 자동차의 이름과 전진한 거리를 {차이름: 거리} 형태로 저장.
        """
        self.cars = {name: 0 for name in car_names}  # 차이름을 키, 0(거리)을 값으로 저장
        return self.cars

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("프로그램이 시작되었습니다.")


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
