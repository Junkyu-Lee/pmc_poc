"""
프로젝트 시나리오 텍스트를 다양한 파일 형식에서 읽어오는 모듈.

지원 형식: .txt, .md, .pdf
"""

import os
from io import BytesIO

import PyPDF2


def read_file(file_path_or_uploaded_file) -> str:
    """
    파일 경로 또는 Streamlit UploadedFile 객체에서 텍스트를 추출한다.

    Args:
        file_path_or_uploaded_file: 파일 경로(str) 또는 Streamlit UploadedFile 객체

    Returns:
        추출된 텍스트 문자열

    Raises:
        ValueError: 지원하지 않는 파일 형식인 경우
        FileNotFoundError: 파일 경로가 존재하지 않는 경우
    """
    if isinstance(file_path_or_uploaded_file, str):
        return _read_from_path(file_path_or_uploaded_file)
    else:
        return _read_from_uploaded_file(file_path_or_uploaded_file)


def _read_from_path(file_path: str) -> str:
    """
    파일 경로에서 텍스트를 읽어온다.

    Args:
        file_path: 읽을 파일의 경로

    Returns:
        파일에서 추출된 텍스트
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext in (".txt", ".md"):
        return _read_text_file(file_path)
    elif ext == ".pdf":
        with open(file_path, "rb") as f:
            return _extract_pdf_text(f)
    else:
        raise ValueError(f"지원하지 않는 파일 형식입니다: {ext}")


def _read_from_uploaded_file(uploaded_file) -> str:
    """
    Streamlit UploadedFile 객체에서 텍스트를 읽어온다.

    Args:
        uploaded_file: Streamlit UploadedFile 객체

    Returns:
        파일에서 추출된 텍스트
    """
    name = uploaded_file.name
    ext = os.path.splitext(name)[1].lower()

    if ext in (".txt", ".md"):
        raw = uploaded_file.read()
        return _decode_bytes(raw)
    elif ext == ".pdf":
        return _extract_pdf_text(BytesIO(uploaded_file.read()))
    else:
        raise ValueError(f"지원하지 않는 파일 형식입니다: {ext}")


def _read_text_file(file_path: str) -> str:
    """
    텍스트 파일을 읽는다. utf-8로 시도한 후 실패하면 cp949로 재시도한다.

    Args:
        file_path: 텍스트 파일 경로

    Returns:
        파일 내용 문자열
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="cp949") as f:
            return f.read()


def _decode_bytes(raw: bytes) -> str:
    """
    바이트 데이터를 문자열로 디코딩한다. utf-8 우선, 실패 시 cp949 시도.

    Args:
        raw: 디코딩할 바이트 데이터

    Returns:
        디코딩된 문자열
    """
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp949")


def _extract_pdf_text(file_obj) -> str:
    """
    PDF 파일 객체에서 텍스트를 추출한다.

    Args:
        file_obj: PDF 파일 객체 (바이너리 모드)

    Returns:
        PDF에서 추출된 전체 텍스트
    """
    reader = PyPDF2.PdfReader(file_obj)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)
