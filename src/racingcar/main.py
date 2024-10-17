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
        if attempts <= 1:
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
        self.distance+=1
    def get_distance(self):
        return self.distance
    def get_name(self):
        return self.name

class Race:
    def __init__(self, cars):
        self.cars = cars
    def play(self):
        for car in self.cars:
            random_number = random.randint(1, 9)
            if random_number>=4:
                car.move()
            self.print_dis(car)
            print()
        print()
        
    def get_winner(self) :
        winner = []
        max_distance = -1
        for car in self.cars:
            if car.get_distance() > max_distance :
                max_distance = car.get_distance()
        
        for car in self.cars:
            if car.get_distance() == max_distance:
                winner.append(car.get_name())
        
        return winner
    
    def print_dis(self, car) :
        print("{} : ".format(car.get_name()), end="")
        for i in range (car.get_distance()) :
            print("-", end = "")

    
def game(cars, attempts):
    race = Race(cars)

    while attempts:
        attempts-=1
        race.play()

    winner = race.get_winner()
    print(winner)

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("프로그램이 시작되었습니다.")

    try:
        car_names = InputHandler.get_car_names()
    except ValueError:
        return

    cars = []
    for car_name in car_names:
        cars.append(Car(car_name))
    
    try:
        attempts = InputHandler.get_attempts()
    except ValueError:
        return
    
    game(cars, attempts)

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
