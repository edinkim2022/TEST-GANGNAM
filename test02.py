# 사용자 정보와 작업 데이터를 파일로 저장 및 관리
USER_FILE = "user_data.txt"
TASK_FILE = "tasks.txt"

# 사용자 등록 함수
def register_user():
    user_id = input("ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    gender = input("성별을 입력하세요 (남/여): ")
    birthday = input("생일을 입력하세요 (YYYY-MM-DD): ")

    with open(USER_FILE, "a", encoding="utf-8") as file:
        file.write(f"{user_id},{password},{name},{age},{gender},{birthday}\n")
    print("회원가입이 완료되었습니다!")

def login_user():
    # 로그인 정보 입력
    user_id = input("ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    # 사용자 정보 확인
    try:
        with open(USER_FILE, "r", encoding="utf-8") as file:
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

# 작업 데이터 읽기
def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task_data = line.strip().split(",")
                tasks.append({
                    "name": task_data[0],
                    "description": task_data[1],
                    "start_date": task_data[2],
                    "end_date": task_data[3],
                    "assignee": task_data[4],
                    "status": task_data[5],
                })
    except FileNotFoundError:
        pass  # 파일이 없으면 빈 리스트 반환
    return tasks

# 작업 데이터 저장
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['description']},{task['start_date']},{task['end_date']},{task['assignee']},{task['status']}\n")

# 작업 만들기
def create_task(tasks, users):
    print("\n[작업 만들기]")
    name = input("작업 이름: ")
    description = input("작업 설명: ")
    start_date = input("시작 날짜(YYYY-MM-DD): ")
    end_date = input("종료 날짜(YYYY-MM-DD): ")
    assignee = input("작업자 이름: ")

    # 작업자가 사용자 목록에 있는지 확인
    valid_user = False
    with open(USER_FILE, "r", encoding="utf-8") as file:
        for line in file:
            _, _, stored_name, _, _, _ = line.strip().split(",")
            if stored_name == assignee:
                valid_user = True
                break

    if not valid_user:
        print("존재하지 않는 작업자입니다.")
        return

    tasks.append({
        "name": name,
        "description": description,
        "start_date": start_date,
        "end_date": end_date,
        "assignee": assignee,
        "status": "해야 할 일",
    })
    save_tasks(tasks)
    print("작업이 성공적으로 추가되었습니다.")

# 작업 수정하기
def modify_task(tasks):
    print("\n[작업 수정하기]")
    task_name = input("수정할 작업 이름: ")
    for task in tasks:
        if task["name"] == task_name:
            print(f"현재 작업 상태: {task['status']}")
            task["name"] = input(f"작업 이름 ({task['name']}): ") or task["name"]
            task["description"] = input(f"작업 설명 ({task['description']}): ") or task["description"]
            task["start_date"] = input(f"시작 날짜 ({task['start_date']}): ") or task["start_date"]
            task["end_date"] = input(f"종료 날짜 ({task['end_date']}): ") or task["end_date"]
            task["assignee"] = input(f"작업자 ({task['assignee']}): ") or task["assignee"]
            task["status"] = input(f"작업 상태 (해야 할 일, 진행중, 완료) ({task['status']}): ") or task["status"]
            save_tasks(tasks)
            print("작업이 성공적으로 수정되었습니다.")
            return
    print("작업을 찾을 수 없습니다.")

# 작업 보기
def view_tasks(tasks, status_filter=None):
    print("\n[작업 보기]")
    filtered_tasks = [task for task in tasks if not status_filter or task["status"] == status_filter]
    if not filtered_tasks:
        print("작업이 없습니다.")
        return

    for task in filtered_tasks:
        print(f"작업 이름: {task['name']}")
        print(f"  설명: {task['description']}")
        print(f"  시작 날짜: {task['start_date']}")
        print(f"  종료 날짜: {task['end_date']}")
        print(f"  작업자: {task['assignee']}")
        print(f"  상태: {task['status']}")
        print()

# 로그인 후 작업 메뉴
def task_menu(user_name):
    tasks = load_tasks()

    while True:
        print("\n[작업 관리]")
        print("1. 작업 만들기")
        print("2. 작업 수정하기")
        print("3. 현재 해야 할 일 보기")
        print("4. 현재 진행중 보기")
        print("5. 현재 완료 보기")
        print("6. 로그아웃")
        choice = input("선택: ")

        if choice == "1":
            create_task(tasks, user_name)
        elif choice == "2":
            modify_task(tasks)
        elif choice == "3":
            view_tasks(tasks, status_filter="해야 할 일")
        elif choice == "4":
            view_tasks(tasks, status_filter="진행중")
        elif choice == "5":
            view_tasks(tasks, status_filter="완료")
        elif choice == "6":
            print("로그아웃합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 함수
def main():
    while True:
        print("\n1. 회원가입")
        print("2. 로그인")
        print("3. 종료")
        choice = input("선택하세요: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                # 로그인 성공 후 작업 메뉴로 이동
                print("로그인 후 작업 관리 메뉴로 이동합니다.")
                task_menu("user")  # 현재 로그인한 사용자 이름을 전달
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
