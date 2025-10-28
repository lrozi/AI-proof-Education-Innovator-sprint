log_file_path = '/workspaces/AI-proof-Education-Innovator-sprint/단계1 과정1/mission_computer_recovery/mission_computer_main.log'
log_data_list = [] # 데이터를 저장할 빈 리스트

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
                
    print("--- 1. 로그 파일 읽기 및 리스트 변환 완료 ---")

    # (과제 2) 원본 리스트 확인 (출력이 너무 기니 5개만)
    print("\n--- 2. 원본 리스트 객체 출력 (상위 5개) ---")
    for item in log_data_list[:5]:
        print(item)

    # --- 3. 리스트 객체를 시간의 역순으로 정렬 (과제 3) ---
    # log_data_list의 첫 번째 요소(날짜)를 기준으로 역순(내림차순) 정렬합니다.
    log_data_list.sort(reverse=True)
    
    print("\n--- 3. 역순 정렬된 리스트 객체 출력 (상위 5개) ---")
    # 정렬된 리스트의 상위 5개 (즉, 가장 최신 로그)를 출력합니다.
    for item in log_data_list[:5]:
        print(item)

except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {log_file_path}")
except Exception as e:
    print(f"파일 읽기 중 예기치 않은 오류 발생: {e}")