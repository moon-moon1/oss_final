# oss_final

## 프로젝트 목적
**oss_final**은 영상 편집에 어려움을 겪는 사람들을 위해, 최소한의 이해만으로도 쇼츠 영상을 쉽게 편집할 수 있게 도와주는 웹사이트 및 서버 프로그램입니다. 웹 브라우저에서 간단한 입력만으로 영상의 병합, 자막 추가 등 핵심 편집 기능을 사용할 수 있습니다.

## 상세 기능
- 웹페이지(index.html)에서 영상 파일 및 편집 정보를 입력
- 서버(server.py)에서 입력값을 받아 자동으로 영상 처리
- 결과 영상을 웹페이지에서 바로 다운로드
- 단독 실행 가능(외부 서비스 필요 없음)

## 입출력 형태
- **입력:** 영상 파일(mp4 등), 자막/효과 정보 등(웹폼)
- **출력:** 편집된 영상 파일(mp4, 웹페이지에서 다운로드 가능)

## 사용 방법

### 1. 소스코드 다운로드
```bash
git clone https://github.com/moon-moon1/oss_final.git
cd oss_final

2. 환경 설정
Python 3.10 이상 필요

필수 라이브러리 설치(Flask):

```bash
pip install flask

3. 실행 방법
서버 실행:

```bash
python server.py
웹 브라우저에서 http://localhost:5000 접속
(Edge 브라우저 권장)

4. 주요 파일 설명
index.html: 사용자용 웹페이지

server.py: 서버 및 영상 처리 로직

실행 예시
브라우저에서 영상 파일 업로드 → 옵션 입력 → 서버가 처리 → 결과 영상 다운로드

기타 안내
본 SW는 완전한 단독 실행 프로그램입니다.
Windows(Edge 권장) 지원, 기타 OS는 별도 테스트 필요

추가 설치/환경설정은 위 설명 참고

GitHub 저장소 링크
https://github.com/moon-moon1/oss_final
