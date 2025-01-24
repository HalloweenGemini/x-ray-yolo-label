from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# 이미지 디렉토리 설정
IMAGE_FOLDER = 'static/images'
LABEL_FOLDER = 'static/labels'

# 필요한 폴더들 생성
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(LABEL_FOLDER, exist_ok=True)

LABELS = {
    '0': '애매한 골절',
    '1': '골절'
}

def get_image_list():
    # .png 파일만 필터링
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.png')]
    return sorted(images)

def get_existing_labels():
    # 이미 라벨링된 이미지들의 바운딩 박스 정보를 읽어옴
    labeled_images = {}
    
    for label_file in os.listdir(LABEL_FOLDER):
        if label_file.endswith('.txt'):
            image_name = label_file.replace('.txt', '.png')
            label_path = os.path.join(LABEL_FOLDER, label_file)
            
            boxes = []
            with open(label_path, 'r') as f:
                for line in f:
                    label, x_center, y_center, width, height = map(float, line.strip().split())
                    boxes.append({
                        'label': str(int(label)),  # JavaScript에서 사용하기 위해 문자열로 변환
                        'x': x_center,
                        'y': y_center,
                        'width': width,
                        'height': height
                    })
            
            if boxes:  # 박스 정보가 있는 경우만 저장
                labeled_images[image_name] = boxes
    
    return labeled_images

@app.route('/')
def index():
    images = get_image_list()
    if not images:
        return "이미지가 없습니다. static/images 폴더에 PNG 파일을 넣어주세요."
    
    # 기존 라벨 정보 가져오기
    existing_labels = get_existing_labels()
    print(f"Found {len(existing_labels)} labeled images")  # 디버깅용
    
    return render_template('index.html', 
                         images=images, 
                         labels=LABELS, 
                         existing_labels=existing_labels)

@app.route('/save_label', methods=['POST'])
def save_label():
    data = request.json
    image_name = data.get('image')
    boxes = data.get('boxes', [])
    
    # YOLO 형식으로 라벨 저장 (클래스 x_center y_center width height)
    label_file = os.path.splitext(image_name)[0] + '.txt'
    label_path = os.path.join('static/labels', label_file)
    
    # labels 디렉토리가 없으면 생성
    os.makedirs('static/labels', exist_ok=True)
    
    # 모든 박스 정보를 YOLO 형식으로 저장
    with open(label_path, 'w') as f:
        for box in boxes:
            # YOLO 형식으로 변환: <class> <x_center> <y_center> <width> <height>
            x_center = box['x'] + (box['width'] / 2)
            y_center = box['y'] + (box['height'] / 2)
            f.write(f"{box['label']} {x_center} {y_center} {box['width']} {box['height']}\n")
    
    return jsonify({'success': True})

@app.route('/get_labels')
def get_labels():
    existing_labels = get_existing_labels()
    return jsonify(existing_labels)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
