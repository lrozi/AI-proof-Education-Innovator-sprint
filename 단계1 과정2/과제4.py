log_file_path = '/workspaces/AI-proof-Education-Innovator-sprint/단계1 과정1/mission_computer_recovery/mission_computer_main.log'
log_data_list = [] # 데이터를 저장할 빈 리스트
log_data_dict = {} # (과제 4) 딕셔너리 객체 생성

print(f"--- '{log_file_path}' 파일 읽기 시작 ---")

try:
    with open(log_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue
            if ',' in clean_line:
                parts = clean_line.split(',', 1)
                timestamp = parts[0].strip()
                message = parts[1].strip()
                log_data_list.append([timestamp, message])
                
    print("--- 1. 리스트 변환 완료 ---")

    # (과제 3) 리스트 역순 정렬
    log_data_list.sort(reverse=True)
    print("--- 3. 리스트 역순 정렬 완료 ---")

    # --- 4. 리스트 객체를 사전(Dict) 객체로 전환 (과제 4) ---
    # 정렬된 리스트를 순회합니다.
    for item in log_data_list:
        # item[0] (날짜)를 Key로, item[1] (메시지)를 Value로 사용
        timestamp_key = item[0]
        message_value = item[1]
        log_data_dict[timestamp_key] = message_value
    
    print("\n--- 4. 사전(Dict) 객체로 변환 완료 ---")
    
    # 딕셔너리 내용 5개만 확인
    print("--- 변환된 딕셔너리 객체 확인 (일부) ---")
    count = 0
    # .items()로 딕셔너리의 (Key, Value) 쌍을 순회합니다.
    for key, value in log_data_dict.items():
        print(f"'{key}': '{value}'")
        count += 1
        if count >= 5: # 5개만 출력하고 중지
            break

except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {log_file_path}")
except Exception as e:
    print(f"파일 읽기 중 예기치 않은 오류 발생: {e}")