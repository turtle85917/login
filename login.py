import os.path

try:
    main = int(input("1. 로그인\n2. 회원가입"))
    if main == 2:
        id=input("ID를 입력해주세요")
        if os.path.isfile(f"./{id}.txt"):
            print("있는 ID입니다.")
        else:
            password = input("비밀번호를 입력해주세요")
            f = open(f"./{id}.txt", "w")
            f.write(password)
            f.close()
    elif main == 1:
        id=input("ID를 입력해주세요")
        if os.path.isfile(f"./{id}.txt"):
            with open(f"./{id}.txt") as file_object:
                p = file_object.read()
                password = input("비밀번호를 입력해주세요")
                if p == password:
                    print("로그인 성공!")
                else:
                    print("로그인 실패.. 비밀번호가 잘 못 됬네요..")
        else:
            print("없는 ID입니다.")
    else:
        print("1, 2번 중에 골라주세요")
except Exception as e: print(e)
