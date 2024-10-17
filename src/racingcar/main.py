import random


class InputHandler:
    @staticmethod
    def get_car_names():
        """경주할 자동차 이름을 쉼표(,)로 구분하여 입력받기"""
        car_names = input(
            "경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분) "
        ).split(",")

        # 이름이 5자를 초과하면 예외 발생
        for name in car_names:
            if len(name.strip()) > 5:
                raise ValueError(
                    f"자동차 이름은 5자 이하만 가능합니다. 잘못된 이름: {name.strip()}"
                )

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


class Car:
    """
    입력된 이름에 맞춰 자동차 객체를 생성.
    각 자동차의 이름과 전진한 거리를 {차이름: 거리} 형태로 저장.
    """

    def __init__(self, car_name):
        self.name = car_name
        self.distance = 0

    def move(self):
        self.distance += 1

    def get_distance(self):
        return self.distance

    def get_name(self):
        return self.name


class Race:
    def __init__(self, cars):
        self.cars = cars

    def move_car(self, car):
        """자동차가 전진할지 여부를 결정하는 로직"""
        random_number = random.randint(1, 9)
        if random_number >= 4:
            car.move()

    def play_round(self):
        """한 라운드 진행"""
        for car in self.cars:
            self.move_car(car)

    def print_results(self):
        """각 자동차의 결과를 출력"""
        for car in self.cars:
            print(f"{car.get_name()} : {'-' * car.get_distance()}")

    def get_winner(self):
        """가장 멀리 간 자동차를 찾는 로직"""
        max_distance = max(car.get_distance() for car in self.cars)
        return [
            car.get_name() for car in self.cars if car.get_distance() == max_distance
        ]


def game(cars, attempts):
    """전체 게임 로직을 처리하는 함수"""
    race = Race(cars)

    while attempts:
        attempts -= 1
        race.play_round()  # 한 라운드 실행
        race.print_results()  # 결과 출력
        print()  # 라운드 간 공백 출력

    winners = race.get_winner()
    print("최종 우승자 : " + ", ".join(winners))


def main():
    """프로그램의 진입점 함수"""
    print("프로그램이 시작되었습니다.")

    car_names = InputHandler.get_car_names()
    cars = [Car(car_name) for car_name in car_names]

    attempts = InputHandler.get_attempts()

    game(cars, attempts)


if __name__ == "__main__":
    main()
