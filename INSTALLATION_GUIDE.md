# 🚀 Advanced HWP MCP Server 설치 가이드

## 누구나 쉽게 설치하는 방법

### 1단계: 저장소 다운로드
```bash
# Git이 있는 경우
git clone https://github.com/skerishKang/MCP_HWP_Limone.git

# Git이 없는 경우
# GitHub에서 "Code" > "Download ZIP" 클릭하여 다운로드
```

### 2단계: 필수 프로그램 확인
- ✅ **Windows 운영체제** (필수)
- ✅ **Python 3.10 이상** 설치
- ✅ **한글 프로그램** 설치 (한글 2010 이상)
- ✅ **Claude Desktop** 설치

### 3단계: Python 패키지 설치
```bash
# 다운로드한 폴더에서 실행
cd MCP_HWP_Limone
pip install -r requirements.txt
```

### 4단계: Claude Desktop 설정
Claude Desktop 설정 파일에 추가:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "hwp": {
      "command": "python",
      "args": [
        "C:/Users/[사용자명]/Downloads/MCP_HWP_Limone/advanced_hwp_server.py"
      ],
      "env": {
        "PYTHONPATH": "C:/Users/[사용자명]/Downloads/MCP_HWP_Limone"
      }
    }
  }
}
```

⚠️ **중요**: `[사용자명]`과 경로를 실제 다운로드한 위치로 변경하세요!

### 5단계: Claude Desktop 재시작
Claude Desktop을 완전히 종료 후 다시 시작

### 6단계: 테스트
Claude Desktop에서 다음과 같이 입력:
```
새 한글 문서를 만들고 "테스트"라는 텍스트를 입력해주세요.
```

## 🎯 사용 예시

### 기본 사용법
```
새 한글 문서를 만들고 "안녕하세요"라는 텍스트를 삽입해주세요.
```

### 고급 사용법
```
새 문서를 만들고 제목을 "보고서"로 하되 맑은고딕 18pt 굵게 설정하고, 
본문에 "내용입니다"를 바탕 12pt로 추가해주세요.
```

```
3행 4열 표를 만들고 첫 번째 행의 셀들을 병합해주세요.
```

## 🔧 문제해결

### 한글 초기화 실패
- 한글 프로그램이 설치되어 있는지 확인
- 한글을 한 번 실행해서 정상 동작하는지 확인

### 패키지 설치 오류
```bash
pip install --user mcp fastmcp pywin32
```

### Claude Desktop 연결 실패
- 설정 파일 경로가 정확한지 확인
- Python 경로가 올바른지 확인

## 💡 주요 특징

- **25개 고급 한글 제어 도구**
- **기존 한글 MCP 대비 10배 향상된 기능**
- **정밀한 텍스트 위치 지정**
- **완전한 서식 제어**
- **표/이미지/도형 삽입**
- **PDF 내보내기**

## 🤝 지원

- 문제가 있으면 GitHub Issues에 문의
- 개선 아이디어도 환영합니다!
