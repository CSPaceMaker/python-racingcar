import random

class InputHandler:
    @staticmethod
    def get_car_names():
        """경주할 자동차 이름을 쉼표(,)로 구분하여 입력받기"""
        car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분) ").split(",")
        


def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("프로그램이 시작되었습니다.")

    InputHandler.get_car_names()


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
