# 1. 파일 경로 설정
log_file_path = '/workspaces/AI-proof-Education-Innovator-sprint/단계1 과정1/mission_computer_recovery/mission_computer_main.log'
log_data_list = [] # 데이터를 저장할 빈 리스트

print(f"--- '{log_file_path}' 파일 읽기 시작 ---")

try:
    # 2. 파일 읽기 (과제 1)
    with open(log_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue

            # --- !!! 여기가 수정되었습니다 !!! ---
            # '문제2' 설명에 따라 콤마(,)를 기준으로 분리합니다.
            # .split(',', 1)은 콤마를 기준으로 "최대 1번만" 나눕니다.
            if ',' in clean_line:
                parts = clean_line.split(',', 1) # '] ' 대신 ',' 사용
                
                # parts[0] = 날짜/시간
                # parts[1] = 로그 내용
                # (양쪽 공백을 제거해줍니다)
                timestamp = parts[0].strip()
                message = parts[1].strip()
                
                # 3. 리스트 객체로 전환 (과제 1)
                log_data_list.append([timestamp, message])
            # ------------------------------------
                
    print("--- 1. 로그 파일 읽기 및 리스트 변환 완료 ---")

    # 4. 리스트 객체 화면에 출력 (과제 2)
    print("\n--- 2. 변환된 리스트 객체 출력 ---")
    for item in log_data_list:
        print(item)

except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {log_file_path}")
except Exception as e:
    print(f"파일 읽기 중 예기치 않은 오류 발생: {e}")