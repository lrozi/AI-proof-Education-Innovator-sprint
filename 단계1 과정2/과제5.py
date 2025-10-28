import json # (과제 5) JSON 라이브러리를 사용 (기본 내장)
log_file_path = '/workspaces/AI-proof-Education-Innovator-sprint/단계1 과정1/mission_computer_recovery/mission_computer_main.log'
log_data_list = [] # 데이터를 저장할 빈 리스트
log_data_dict = {}

print(f"--- '{log_file_path}' 파일 읽기 시작 ---")

try:
    # 1. 파일 읽기 (과제 1)
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

    # 2. 리스트 정렬 (과제 3)
    log_data_list.sort(reverse=True)
    print("--- 3. 리스트 역순 정렬 완료 ---")

    # 3. 딕셔너리 변환 (과제 4)
    for item in log_data_list:
        timestamp_key = item[0]
        message_value = item[1]
        log_data_dict[timestamp_key] = message_value
    print("--- 4. 딕셔너리 객체로 변환 완료 ---")

    # --- 4. 사전 객체를 JSON 파일로 저장 (과제 5) ---
    output_json_path = 'mission_computer_main.json'
    print(f"\n--- 5. 사전 객체를 '{output_json_path}' 파일로 저장 ---")
    
    # 제약조건: 파일 처리 부분에 예외 처리 적용
    try:
        # 'w' (쓰기) 모드로 JSON 파일을 엽니다.
        with open(output_json_path, 'w', encoding='utf-8') as f:
            # json.dump로 딕셔너리를 파일에 JSON 형식으로 저장
            # ensure_ascii=False: 한글이 깨지지 않게 보장
            # indent=4: 파일을 예쁘게 4칸 들여쓰기 (가독성)
            json.dump(log_data_dict, f, ensure_ascii=False, indent=4)
        
        print(f"--- JSON 파일 저장 완료: {output_json_path} ---")

    except Exception as e:
        # JSON 파일 저장 중 발생할 수 있는 오류 처리
        print(f"JSON 파일 저장 중 오류 발생: {e}")


except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {log_file_path}")
except Exception as e:
    print(f"파일 읽기 중 예기치 않은 오류 발생: {e}")