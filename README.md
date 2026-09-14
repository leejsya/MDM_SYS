# MDM_SYS

이는 MDM(Medical Data Management) 시스템으로, 
Django REST Framework로 구축한 환자 정보를 등록하고 의료 데이터를 관리하는 간단한 API 서버이다.


## 주요 기능
1. 환자의 정보를 등록하고 patient id로 구분하여 정보를 관리할 수 있다.
2. 환자의 Chest X-ray 결과 이미지를 환자별로 업로드하고 관리할 수 있다.


이 백엔드 애플리케이션의 model, serializer, view 구성은 다음과 같다.

## *models.py*
1. **Patient 모델** : 환자의 기본적인 정보를 담고있는 모델이다. 다음과 같은 내용을 포함.
- pid : patient id
- name : 이름
- gender : 성별
- age : 나이
- registered_time : 등록일시
---
2. **MedicalImage 모델** : 이미지에 대한 메타 정보를 담고있는 모델이다.
- img_id : 이미지 고유 id
- patient : 하나의 MedicalImage 모델이 하나의 Patient 모델을 참조.
- image : Chest X-ray 이미지
- taken_time : 촬영일시
- description : 라벨(NORMAL or PNUEMONIA)

## *serializers.py*
1. **PatientSerializer** : 등록된 patients의 리스트를 보여주는 기능을 위한 serializer.
2. **MedicalImageSerializer** : image의 메타 정보를 보여주는 기능을 위한 serializer.
3. **PatientDetailSerializer** : 특정 patient의 detail을 보여주는 기능을 위한 serializer.
각 환자의 Chest X-ray 이미지는 각 환자의 detail 화면에서만 나타나도록 설계하였다.

## *views.py*
1. **PatientsAPI** : 등록된 patients의 리스트를 보여주고 등록할 수 있는 기능.
2. **PatientDetailView** : 특정 patient의 detail을 보여주고 수정 및 삭제할 수 있는 기능.
3. **MedicalImagesAPI** : 특정 patient의 이미지 리스트를 보여주고 추가할 수 있는 기능.
4. **MedicalImageAPI** : 특정 image의 메타 정보를 보여주고 수정 및 삭제할 수 있는 기능.

## 동작방식
1. *localhost:8000/board/patients* 경로로 이동하면 다음과 같이 등록된 patients의 목록과 patient를 추가할 수 있다.
<img width="1190" height="1145" alt="image" src="https://github.com/user-attachments/assets/1aa39ac4-5131-415d-8ab1-888ee224acdf" />
2. 위와 같은 경로에서 특정 patient의 pid에 해당하는 경로로 이동하면 해당 patient의 detail 정보를 조회하고 수정 및 삭제할 수 있다.
<img width="1190" height="1145" alt="image" src="https://github.com/user-attachments/assets/9cb3709f-1835-42de-8096-e4eed5355315" />
3. 위와 같은 경로에서 *images/* 경로로 이동하면 해당 patient의 이미지 메타정보를 조회하고 추가할 수 있다.
<img width="1190" height="1145" alt="image" src="https://github.com/user-attachments/assets/00cafff1-d22b-4107-be3f-e032953ff685" />
4. 위와 같은 경로에서 특정 image의 img id에 해당하는 경로로 이동하면 해당 image의 메타정보를 조회하고 수정 및 삭제할 수 있다.
<img width="1190" height="1145" alt="image" src="https://github.com/user-attachments/assets/e6c077bb-ff9c-46fb-aa78-c18bda141f0e" />








