"""
이미지 처리를 총괄하는 메인 모듈
모든 이미지 처리 단계를 조합하여 실행합니다.
"""

import cv2
import numpy as np
from PIL import Image
from typing import Dict, Any, Optional, Union

# 모듈 가져오기
from .face_detection import adjust_face_position
from .background_removal import remove_background
from .image_enhancement import (
    upscale_image, enhance_skin, enhance_eyes, enhance_sharpness
)
from .image_utils import (
    decode_image, encode_image, pil_to_cv2, cv2_to_pil
)

def process_image(image_data: str, options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    이미지 데이터를 처리하여 증명사진으로 변환합니다.
    
    Args:
        image_data: Base64 인코딩된 이미지 데이터
        options: 처리 옵션
            - adjust_face_position (bool): 얼굴 위치 보정 여부
            - remove_background (bool): 배경 제거 여부
            - upscale (bool): 이미지 확대 여부
            - skin_smoothing (bool): 피부 보정 여부
            - eye_enhance (bool): 눈 강조 여부
            - sharpness_enhance (bool): 선명도 개선 여부
            
    Returns:
        처리 결과를 담은 딕셔너리
            - enhanced_image: 처리된 이미지 (Base64)
            - metadata: 이미지 메타데이터
            
    Raises:
        ValueError: 이미지 데이터가 유효하지 않은 경우
    """
    try:
        # 옵션이 None이면 빈 딕셔너리로 초기화
        if options is None:
            options = {}
            
        # 이미지 데이터 검증
        if not image_data:
            raise ValueError('이미지 데이터가 유효하지 않습니다')
            
        # base64 데이터 형식 확인 및 처리
        if not isinstance(image_data, str):
            raise ValueError('이미지 데이터는 문자열이어야 합니다')
            
        # 이미지 디코딩
        if not image_data.startswith('data:image'):
            image_data = f'data:image/jpeg;base64,{image_data}'
            
        # 이미지 디코딩
        image_pil = decode_image(image_data)
        
        # 처리 옵션 기본값 설정
        options.setdefault('adjust_face_position', True)
        options.setdefault('remove_background', True)
        options.setdefault('upscale', True)
        options.setdefault('skin_smoothing', True)
        options.setdefault('eye_enhance', True)
        options.setdefault('sharpness_enhance', True)
        
        # PIL 이미지를 OpenCV로 변환
        image_cv = pil_to_cv2(image_pil)
        
        # 얼굴 위치 보정
        if options.get('adjust_face_position'):
            image_cv = adjust_face_position(image_cv)
            
        # 업스케일링
        if options.get('upscale'):
            scale_factor = options.get('scale_factor', 2.0)
            image_cv = upscale_image(image_cv, scale_factor)
            
        # 피부 보정
        if options.get('skin_smoothing'):
            image_cv = enhance_skin(image_cv)
            
        # 눈 보정
        if options.get('eye_enhance'):
            image_cv = enhance_eyes(image_cv)
            
        # OpenCV 이미지를 PIL로 변환
        image_pil = cv2_to_pil(image_cv)
        
        # 배경 제거
        if options.get('remove_background'):
            image_pil = remove_background(image_pil)
            
        # 선명도 개선
        if options.get('sharpness_enhance'):
            factor = options.get('sharpness_factor', 1.5)
            image_pil = enhance_sharpness(image_pil, factor)
            
        # 결과 인코딩
        encoded_image = encode_image(image_pil, format="JPEG", quality=95)
        
        return {
            'enhanced_image': encoded_image,
            'metadata': {
                'format': 'JPEG',
                'dimensions': image_pil.size,
                'size': len(encoded_image)
            }
        }

    except Exception as e:
        raise Exception(f"이미지 처리 중 오류 발생: {str(e)}")
        
def apply_beauty_filter(image, strength=0.5):
    """
    뷰티 필터 스텁 함수 - 향후 구현을 위한 자리 표시자
    """
    return image

def apply_color_filter(image, filter_type='natural'):
    """
    색상 필터 스텁 함수 - 향후 구현을 위한 자리 표시자
    """
    return image

def adjust_contrast(image, contrast_factor=1.15):
    """
    대비 조절 스텁 함수 - 향후 구현을 위한 자리 표시자
    """
    return image