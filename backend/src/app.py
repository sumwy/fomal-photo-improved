import os
import sys
import base64
import re

# 현재 디렉토리와 부모 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir)
sys.path.insert(0, parent_dir)

from flask import Flask, Blueprint, request, jsonify, render_template, send_from_directory

# 기존 services.py 대신 모듈화된 image_processor 가져오기
from modules.image_processor import process_image

app = Flask(__name__, 
            static_folder='../../frontend/static',
            template_folder='../../frontend/templates')

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/process_image', methods=['POST'])
def process_image_route():
    try:
        # 이미지 데이터 가져오기
        image_data = request.form.get('image')
        
        # 이미지 데이터에서 base64 부분만 추출
        if image_data and ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # 이미지 처리 옵션 설정
        options = {
            'adjust_face_position': True,
            'remove_background': True,
            'upscale': True,
            'skin_smoothing': True,
            'eye_enhance': True,
            'sharpness_enhance': True
        }
        
        # 이미지 처리 - 이제 모듈화된 process_image 함수 사용
        result = process_image(image_data, options)
        
        # 처리된 이미지 반환
        return jsonify({
            'success': True,
            'processed_image': f"data:image/jpeg;base64,{result['enhanced_image']}"
        })
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

@main_blueprint.route('/api/enhance_image', methods=['POST'])
def enhance_image():
    try:
        # 이미지 데이터 가져오기
        image_data = request.json.get('image_data')
        options = request.json.get('options', {})
        
        # 이미지 처리 - 이제 모듈화된 process_image 함수 사용
        result = process_image(image_data, options)
        
        # 처리된 이미지 반환
        return jsonify({
            'success': True,
            'enhanced_image': result['enhanced_image']
        })
    except Exception as e:
        print(f"Error enhancing image: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

@main_blueprint.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# 블루프린트 등록
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)