log_file_name = 'mission_computer_main.log'

try:
    # 파일을 'r' (읽기) 모드와 'utf-8' 인코딩으로 엽니다.
    with open(log_file_name, 'r', encoding='utf-8') as f:
        print(f'--- Start reading {log_file_name} ---')

        # 파일의 모든 내용을 한 줄씩 읽어 화면에 출력합니다.
        for line in f:
            # print() 함수는 기본적으로 줄바꿈이 있으므로,
            # line에 포함된 줄바꿈 문자(\n)를 .strip()으로 제거해 이중 줄바꿈을 방지합니다.
            print(line.strip())

        print(f'--- End reading {log_file_name} ---')

except FileNotFoundError:
    # 파일을 찾을 수 없을 때 발생하는 예외 처리
    print(f"Error: The file '{log_file_name}' was not found.")

except Exception as e:
    # 그 외 다른 모든 예외 처리 (파일 읽기 권한 문제 등)
    print(f"An unexpected error occurred: {e}")