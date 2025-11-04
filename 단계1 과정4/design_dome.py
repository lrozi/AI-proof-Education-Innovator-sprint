# 1. 상수 정의
# math 라이브러리를 사용하지 않기 위해 원주율(PI)을 직접 정의합니다.
PI = 3.14159

# 재질별 밀도 (단위를 g/cm³에서 kg/m³로 통일)
# 1 g/cm³ = 1000 kg/m³
DENSITIES = {
    '유리': 2.4 * 1000,      # 2400 kg/m³
    '알루미늄': 2.7 * 1000,   # 2700 kg/m³
    '탄소강': 7.85 * 1000    # 7850 kg/m³
}

# 화성의 중력 비율 (지구 대비 약 37.9%)
MARS_GRAVITY_RATIO = 0.379

# 2. 전역 변수 초기화
# 계산 결과를 저장할 전역 변수를 선언합니다.
g_material = ''
g_diameter = 0.0
g_thickness = 0.0
g_area = 0.0
g_weight = 0.0


def sphere_area(diameter, material='유리', thickness=1.0):
    """
    반구형 돔의 면적과 화성에서의 무게를 계산합니다.

    Args:
        diameter (float): 돔의 지름 (m 단위)
        material (str, optional): 재질 ('유리', '알루미늄', '탄소강'). 기본값 '유리'.
        thickness (float, optional): 두께 (cm 단위). 기본값 1.0.
    """
    
    # 3. 계산 로직
    
    # 3-1. 면적 (Area) 계산
    # 지름(m)을 이용해 반지름(m) 계산
    radius_m = diameter / 2
    # 반구의 겉넓이 (m²) = 2 * PI * r²
    area_m2 = 2 * PI * (radius_m ** 2)

    # 3-2. 부피 (Volume) 계산
    # 두께(cm)를 미터(m) 단위로 변환
    thickness_m = thickness / 100.0
    # 부피 (m³) = 면적 (m²) * 두께 (m)
    volume_m3 = area_m2 * thickness_m

    # 3-3. 질량 (Mass) 및 무게 (Weight) 계산
    # 재질에 맞는 밀도(kg/m³) 가져오기
    # .get()을 사용하여, 만약 정의되지 않은 재질이 들어오면 기본값 '유리'의 밀도를 사용
    density = DENSITIES.get(material, DENSITIES['유리'])
    
    # 질량 (kg) = 부피 (m³) * 밀도 (kg/m³)
    mass_kg = volume_m3 * density
    
    # 화성에서의 무게 (kg) = 지구 질량 (kg) * 화성 중력 비율
    weight_mars_kg = mass_kg * MARS_GRAVITY_RATIO

    # 4. 전역 변수 업데이트
    # global 키워드를 사용하여 이 함수가 전역 변수를 수정함을 명시
    global g_material, g_diameter, g_thickness, g_area, g_weight
    
    g_material = material
    g_diameter = diameter
    g_thickness = thickness  # 입력받은 cm 단위를 그대로 저장
    g_area = area_m2
    g_weight = weight_mars_kg


def main():
    """
    메인 실행 함수. 사용자 입력을 받고 sphere_area 함수를 호출합니다.
    """
    print('--- 화성 기지 돔 복구 시뮬레이터 ---')

    # 5. 반복 실행 루프 (제약사항 3)
    while True:
        # 6. 사용자 입력 (지름)
        input_diameter_str = input("돔의 지름(m)을 입력하세요 (종료하려면 '종료'): ")

        # 6-1. 종료 조건 확인 (제약사항 5)
        if input_diameter_str == '종료':
            print('계산을 종료합니다.')
            break

        # 7. 입력값 유효성 검사 (지름) - (보너스 과제 + 제약사항 2)
        try:
            diameter = float(input_diameter_str)
        except ValueError:
            print('! 오류: 지름은 숫자로 입력해야 합니다. 다시 시도하세요.\n')
            continue  # 루프의 처음으로 돌아감

        if diameter <= 0:
            print('! 오류: 지름은 0보다 커야 합니다. 다시 시도하세요.\n')
            continue  # 루프의 처음으로 돌아감

        # 8. 사용자 입력 (재질) - 기본값 처리
        input_material = input("재질을 입력하세요 (유리, 알루미늄, 탄소강) [기본: 유리]: ")
        
        if not input_material:
            material = '유리'  # 기본값 사용
        elif input_material not in DENSITIES:
            print(f"! 경고: '{input_material}'은(는) 알 수 없는 재질입니다. '유리'로 대체합니다.")
            material = '유리'
        else:
            material = input_material

        # 9. 사용자 입력 (두께) - 기본값 + 유효성 검사 (보너스 과제)
        input_thickness_str = input("두께(cm)를 입력하세요 [기본: 1]: ")
        
        if not input_thickness_str:
            thickness = 1.0  # 기본값 사용
        else:
            try:
                thickness = float(input_thickness_str)
                if thickness <= 0:
                    print('! 경고: 두께는 0보다 커야 합니다. 1.0cm로 대체합니다.')
                    thickness = 1.0
            except ValueError:
                print('! 경고: 두께는 숫자로 입력해야 합니다. 1.0cm로 대체합니다.')
                thickness = 1.0

        # 10. 함수 호출
        # 기본값이 아닌 입력값을 명시적으로 전달
        sphere_area(diameter, material, thickness)

        # 11. 결과 출력 (제약사항 4 - 소수점 3자리)
        # f-string의 ':.3f' 형식을 사용하여 소수점 3자리까지 출력
        print('\n--- 계산 결과 ---')
        print(f'재질 =⇒ {g_material}, 지름 =⇒ {g_diameter:.3f}, 두께 =⇒ {g_thickness:.3f}, 면적 =⇒ {g_area:.3f}, 무게 =⇒ {g_weight:.3f} kg')
        print('-------------------\n')


# Python 스크립트가 직접 실행될 때만 main() 함수를 호출
if __name__ == '__main__':
    main()