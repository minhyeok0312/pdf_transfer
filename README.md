# PDF 텍스트 추출 예제

이 프로젝트는 다양한 Python 라이브러리를 사용하여 PDF 파일에서 텍스트를 추출하는 방법을 보여줍니다.

## 사용된 라이브러리

- PyMuPDF (fitz)
- pdfplumber
- PyPDF2
- pdfminer.six

## 설치 방법

1. 이 저장소를 클론합니다
2. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

## 사용 방법

각 라이브러리마다 예제 스크립트가 포함된 디렉토리가 있습니다. 추출기를 사용하려면:

1. PDF 파일을 프로젝트 디렉토리에 넣습니다
2. 스크립트의 `pdf_path` 변수를 수정하여 PDF 파일의 경로를 지정합니다
3. 스크립트를 실행합니다:
```bash
python <library_name>_extractor/extract_text.py
```

## 디렉토리 구조

- `pymupdf_extractor/`: PyMuPDF 구현체 포함
- `pdfplumber_extractor/`: pdfplumber 구현체 포함
- `pypdf2_extractor/`: PyPDF2 구현체 포함
- `pdfminer_extractor/`: pdfminer.six 구현체 포함

## 참고사항

- 각 라이브러리는 서로 다른 장점이 있으며, PDF 파일의 구조에 따라 성능이 다를 수 있습니다
- PyMuPDF는 일반적으로 빠르고 안정적입니다
- pdfplumber는 표 추출과 레이아웃 유지에 좋습니다
- PyPDF2는 가볍지만 일부 PDF 형식에서 문제가 있을 수 있습니다
- pdfminer.six는 강력하지만 다른 옵션들보다 느릴 수 있습니다 