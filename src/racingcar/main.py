import random

class InputHandler:
    @staticmethod
    def get_car_names():
        """경주할 자동차 이름을 쉼표(,)로 구분하여 입력받기"""
        car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분) ").split(",")
        
        # 이름이 5자를 초과하면 예외 발생
        for name in car_names:
            if len(name.strip()) > 5:
                raise ValueError(f"자동차 이름은 5자 이하만 가능합니다. 잘못된 이름: {name.strip()}")
        
        # 공백 제거 후 리스트 반환
        return [name.strip() for name in car_names]
    @staticmethod
    def get_attempts():
        try:
            attempts = int(input("시도할 횟수는 몇 회인가요? "))
        except ValueError:
            raise ValueError("시도 횟수는 숫자여야 합니다.")
        if attempts < 1:
            raise ValueError("시도 횟수는 1 이상이어야 합니다.")
        return attempts


def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("프로그램이 시작되었습니다.")

    InputHandler.get_car_names()
    InputHandler.get_attempts()


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
