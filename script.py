def register_user():
    # 사용자 정보 입력
    user_id = input("ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    gender = input("성별을 입력하세요 (남/여): ")
    birthday = input("생일을 입력하세요 (YYYY-MM-DD): ")

    # 사용자 정보 저장
    with open("user_data.txt", "a", encoding="utf-8") as file:
        file.write(f"{user_id},{password},{name},{age},{gender},{birthday}\n")
    print("회원가입이 완료되었습니다!")

def login_user():
    # 로그인 정보 입력
    user_id = input("ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    # 사용자 정보 확인
    try:
        with open("user_data.txt", "r", encoding="utf-8") as file:
            users = file.readlines()
            for user in users:
                stored_id, stored_pw, _, _, _, _ = user.strip().split(",")
                if user_id == stored_id and password == stored_pw:
                    print("로그인 성공!")
                    return True
            print("ID 또는 비밀번호가 틀렸습니다.")
            return False
    except FileNotFoundError:
        print("등록된 사용자가 없습니다. 먼저 회원가입을 해주세요.")
        return False

def main():
    while True:
        print("\n1. 회원가입")
        print("2. 로그인")
        print("3. 종료")
        choice = input("선택하세요: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
