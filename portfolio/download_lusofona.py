import requests
import json
import os

schoolYear = '202526'

courses = {
    260: "LEI",          # Licenciatura em Engenharia Informática
    457: "MEISI",
    1504: "DI",
    12: "LIG",
    # podes adicionar os outros depois
}

# Cria a pasta onde vão ser guardados os JSONs
os.makedirs('data/lusofona', exist_ok=True)

for course_code, course_name in courses.items():
    print(f"\nA baixar dados do curso: {course_name} (código {course_code})")

    for language in ['PT', 'ENG']:
        # 1. Dados gerais do curso
        url_course = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
        payload = {
            'language': language,
            'courseCode': course_code,
            'schoolYear': schoolYear
        }
        headers = {'content-type': 'application/json'}

        response = requests.post(url_course, json=payload, headers=headers)
        
        if response.status_code != 200:
            print(f"Erro ao baixar curso {course_code} - {language}: {response.status_code}")
            continue

        data_course = response.json()

        filename_course = f"data/lusofona/ULHT{course_code}-{language}.json"
        with open(filename_course, "w", encoding="utf-8") as f:
            json.dump(data_course, f, indent=4, ensure_ascii=False)

        print(f"   ✓ Curso guardado: {filename_course}")

        # 2. Dados de cada UC do curso
        for uc in data_course.get('courseFlatPlan', []):
            uc_code = uc.get('curricularIUnitReadableCode')
            if not uc_code:
                continue

            url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
            payload_uc = {
                'language': language,
                'curricularIUnitReadableCode': uc_code,
            }

            response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
            
            if response_uc.status_code == 200:
                data_uc = response_uc.json()
                filename_uc = f"data/lusofona/{uc_code}-{language}.json"
                
                with open(filename_uc, "w", encoding="utf-8") as f:
                    json.dump(data_uc, f, indent=4, ensure_ascii=False)
                
                print(f"      ✓ UC guardada: {uc_code} - {language}")
            else:
                print(f"      ⚠ Erro na UC {uc_code} - {language}")

print("\nDownload concluído!JSONs -> data/lusofona/")