# 포말 포토(Fomal Photo) - 증명사진 자동 보정 서비스

증명사진 자동 보정 서비스로, 웹캠으로 촬영한 사진을 증명사진 규격에 맞게 자동으로 보정하는 기능을 제공합니다.

## 주요 기능

- 웹캠으로 사진 촬영
- 얼굴 위치 자동 보정
- 배경 제거 및 흰색 배경으로 변경
- 이미지 업스케일링 및 화질 개선
- 피부 보정 및 선명도 개선

## 설치 방법

### Docker를 이용한 설치

```bash
# 저장소 클론
git clone https://github.com/sumwy/fomal-photo-improved.git
cd fomal-photo-improved

# Docker Compose로 실행
docker-compose up -d
```

### 직접 설치

```bash
# 저장소 클론
git clone https://github.com/sumwy/fomal-photo-improved.git
cd fomal-photo-improved

# 백엔드 설치
cd backend
pip install -r requirements.txt

# 실행
python src/app.py
```

## 개선된 점

원본 프로젝트에서 다음과 같은 개선이 이루어졌습니다:

### 1. 백엔드 코드 구조 개선

기존의 큰 services.py 파일을 여러 개의 모듈로 분리하여 구조화했습니다:

- **modules/__init__.py**: 모듈 패키지 초기화
- **modules/face_detection.py**: 얼굴 감지 및 위치 조정 기능
- **modules/background_removal.py**: 배경 제거 기능
- **modules/image_enhancement.py**: 이미지 향상 기능 (업스케일링, 피부 보정, 눈 강조, 선명도 개선)
- **modules/image_utils.py**: 이미지 유틸리티 (인코딩, 디코딩, 이미지 변환 등)
- **modules/image_processor.py**: 주요 이미지 처리 파이프라인 통합

### 개선 사항

1. **기능별 모듈화**: 각 기능을 독립적인 모듈로 분리하여 코드의 가독성과 유지보수성을 향상시켰습니다.
2. **타입 힌트 추가**: 함수 인자와 반환값에 타입 힌트를 추가하여 코드의 안정성을 개선했습니다.
3. **체계적인 예외 처리**: 각 함수마다 일관된 예외 처리를 구현했습니다.
4. **명확한 문서화**: 각 모듈과 함수에 문서화 문자열(docstring)을 추가하여 사용법을 명확히 했습니다.
5. **책임 분리**: 각 모듈은 단일 책임 원칙을 따르도록 설계되었습니다.

자세한 분석 및 개선 계획은 [project_analysis.md](./project_analysis.md) 파일을 참조하세요.