import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage

# 서비스 계정 키 경로 설정
cred = credentials.Certificate('secreat.json')

# Firebase 앱 초기화
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'reverievault-ede4d.appspot.com'
    })

st.title('Image Upload to Firebase Storage')

# 이미지 파일 업로드
uploaded_file = st.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Firebase Storage 버킷 객체 가져오기
    bucket = storage.bucket()
    
    # 파일 경로 설정
    blob = bucket.blob(f'images/{uploaded_file.name}')
    
    # 이미지 파일 업로드
    try:
        blob.upload_from_file(uploaded_file, content_type=uploaded_file.type)
        st.success(f'Image {uploaded_file.name} uploaded to Firebase Storage!')
    except Exception as e:
        st.error(f'Error: {e}')
