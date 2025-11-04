# find_flammables.py

def read_inventory_csv(filename):
    """
    (메인 과제 1, 2)
    CSV 파일을 읽어 Python 리스트 객체로 변환합니다.
    (제약사항에 따라 'csv' 모듈을 사용하지 않고 직접 파싱합니다.)
    """
    inventory_list = []
    
    # 제약조건 2: 파일 예외 처리
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # (가정) 첫 번째 줄(Header)은 건너뜁니다.
            header = lines[0].strip()
            print(f"'{filename}' 파일 읽기 성공. 헤더: {header}")

            # 리스트 변환
            for line in lines[1:]:
                line = line.strip()  # 줄바꿈 문자 및 공백 제거
                if not line:
                    continue  # 빈 줄 건너뛰기

                try:
                    # 쉼표(,)를 기준으로 분리
                    parts = line.split(',')
                    
                    if len(parts) != 2:
                        print(f"경고: 데이터 형식이 잘못되었습니다. (건너뜀) -> {line}")
                        continue
                        
                    item_name = parts[0].strip()
                    flammability = float(parts[1].strip())  # 숫자로 변환
                    
                    inventory_list.append([item_name, flammability])
                    
                except ValueError:
                    # float 변환 실패 시 예외 처리
                    print(f"경고: 인화성 지수가 숫자가 아닙니다. (건너뜀) -> {line}")
                except Exception as e:
                    print(f"처리 중 알 수 없는 오류: {e} (건너뜀) -> {line}")

    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
        return None  # 실패 시 None 반환
    except IOError as e:
        print(f"오류: 파일 읽기 중 오류 발생. {e}")
        return None
    
    return inventory_list


def save_to_csv(filename, data_list):
    """
    (메인 과제 5)
    주어진 데이터를 CSV 포맷으로 저장합니다.
    """
    print(f"\n'{filename}' 파일로 저장 시작...")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # 헤더 작성
            f.write('Item,Flammability\n')
            
            # 데이터 작성
            for item in data_list:
                line = f"{item[0]},{item[1]}\n"
                f.write(line)
        print(f"'{filename}' 파일 저장 완료.")
    except IOError as e:
        print(f"오류: '{filename}' 파일 쓰기 중 오류 발생. {e}")


def main():
    """
    메인 실행 함수
    """
    INPUT_CSV = 'Mars_Base_Inventory_List.csv'
    DANGER_CSV = 'Mars_Base_Inventory_danger.csv'
    DANGER_THRESHOLD = 0.7
    
    # 1. CSV 읽기 (수행과제 1, 2)
    inventory = read_inventory_csv(INPUT_CSV)
    
    if inventory is None:
        print("파일 읽기에 실패하여 프로그램을 종료합니다.")
        return
        
    print("\n--- 1. 원본 데이터 (CSV) ---")
    for item in inventory:
        print(item)

    # 2. 인화성 순으로 정렬 (수행과제 3)
    # list.sort()를 사용하며, key는 리스트의 2번째 요소(index 1)를 기준으로 함.
    # reverse=True로 내림차순 (높은 순) 정렬.
    inventory.sort(key=lambda x: x[1], reverse=True)
    
    print("\n--- 2. 인화성 지수 높은 순 정렬 ---")
    for item in inventory:
        print(item)

    # 3. 인화성 지수 0.7 이상 목록 추출 (수행과제 4)
    # 리스트 컴프리헨션(List Comprehension) 사용
    dangerous_items = [
        item for item in inventory if item[1] >= DANGER_THRESHOLD
    ]
    
    print(f"\n--- 3. 인화성 지수 {DANGER_THRESHOLD} 이상 위험 물질 ---")
    for item in dangerous_items:
        print(item)

    # 4. 0.7 이상 목록을 CSV로 저장 (수행과제 5)
    save_to_csv(DANGER_CSV, dangerous_items)


# 이 스크립트가 직접 실행될 때만 main() 함수를 호출
if __name__ == '__main__':
    main()