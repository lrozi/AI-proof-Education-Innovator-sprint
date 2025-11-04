import numpy as np

# 분석할 파일 리스트
file_list = [
    'mars_base_main_parts-001.csv',
    'mars_base_main_parts-002.csv',
    'mars_base_main_parts-003.csv'
]
output_file = 'parts_to_work_on.csv'
# 3개의 배열을 저장할 리스트
arrays = []
try:
    for file_name in file_list:
            # np.loadtxt를 사용해 CSV 파일 로드, 구분자는 쉼표(,)
            arr = np.loadtxt(
                file_name, 
                delimiter=',', 
                skiprows=1,           # 옵션 1: 첫 번째 줄(헤더)을 건너뜀
                encoding='utf-8-sig'  # 옵션 2: BOM을 올바르게 처리
            )
            arrays.append(arr)
    
    # 리스트에 담긴 배열들을 각각 변수에 할당 (문제 요구사항)
    arr1, arr2, arr3 = arrays

except FileNotFoundError:
    print(f'오류: {file_name} 파일을 찾을 수 없습니다.')
    # 파일이 없으면 이후 코드를 실행할 수 없으므로 종료
    exit()
except Exception as e:
    print(f'파일 로딩 중 알 수 없는 오류 발생: {e}')
    exit()
# 3개의 ndarray를 하나로 합침
parts = np.concatenate((arr1, arr2, arr3))
# parts의 전체 평균값 계산
average_value = np.mean(parts)
print(f'전체 부품 데이터 평균: {average_value:.2f}')
# parts 배열에서 값이 50보다 작은 요소만 필터링
parts_to_work_on = parts[parts < 50]
print(f'보강 필요한 부품 (50 미만) 개수: {len(parts_to_work_on)}')
# 'parts_to_work_on.csv' 파일로 저장 (예외 처리 포함)
try:
    # fmt='%.2f'는 소수점 둘째 자리까지 저장하라는 의미 (데이터에 맞게 조절 가능)
    # 정수라면 fmt='%d'
    np.savetxt(output_file, parts_to_work_on, delimiter=',', fmt='%.2f')
    print(f"'{output_file}' 파일 저장 완료.")
except Exception as e:
    print(f"'{output_file}' 파일 저장 중 오류 발생: {e}")