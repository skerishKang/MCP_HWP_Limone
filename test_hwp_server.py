#!/usr/bin/env python3
"""
Advanced HWP MCP Server 테스트 스크립트
"""

import os
import sys
import time
import logging

# 테스트를 위한 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_hwp_server():
    """HWP 서버 기능 테스트"""
    
    try:
        # 서버 모듈 임포트
        from advanced_hwp_server import hwp_controller
        
        logger.info("=== Advanced HWP MCP Server 테스트 시작 ===")
        
        # 1. 한글 초기화 테스트
        logger.info("1. 한글 초기화 테스트")
        if hwp_controller.initialize():
            logger.info("✅ 한글 초기화 성공")
        else:
            logger.error("❌ 한글 초기화 실패")
            return False
        
        # 2. 새 문서 생성 테스트
        logger.info("2. 새 문서 생성 테스트")
        try:
            hwp_controller.hwp.HAction.Run("FileNew")
            logger.info("✅ 문서 생성 성공")
        except Exception as e:
            logger.error(f"❌ 문서 생성 실패: {e}")
            return False
        
        # 3. 텍스트 삽입 테스트
        logger.info("3. 텍스트 삽입 테스트")
        try:
            act = hwp_controller.hwp.CreateAction("InsertText")
            pset = act.CreateSet()
            pset.SetItem("Text", "Advanced HWP MCP Server 테스트")
            act.Execute(pset)
            logger.info("✅ 텍스트 삽입 성공")
        except Exception as e:
            logger.error(f"❌ 텍스트 삽입 실패: {e}")
            return False
        
        # 4. 글꼴 서식 테스트
        logger.info("4. 글꼴 서식 테스트")
        try:
            act = hwp_controller.hwp.CreateAction("CharShape")
            pset = act.CreateSet()
            pset.SetItem("FaceNameHangul", "맑은 고딕")
            pset.SetItem("Height", 1400)  # 14pt
            pset.SetItem("Bold", True)
            act.Execute(pset)
            logger.info("✅ 글꼴 서식 적용 성공")
        except Exception as e:
            logger.error(f"❌ 글꼴 서식 적용 실패: {e}")
            return False
        
        # 5. 표 생성 테스트
        logger.info("5. 표 생성 테스트")
        try:
            # 새 줄 추가
            act = hwp_controller.hwp.CreateAction("InsertText")
            pset = act.CreateSet()
            pset.SetItem("Text", "\n\n")
            act.Execute(pset)
            
            # 표 생성
            act = hwp_controller.hwp.CreateAction("TableCreate")
            pset = act.CreateSet()
            pset.SetItem("Rows", 3)
            pset.SetItem("Cols", 3)
            pset.SetItem("WidthType", 2)
            pset.SetItem("HeightType", 0)
            pset.SetItem("CreateItemArray", [0, 1, 0])
            act.Execute(pset)
            logger.info("✅ 표 생성 성공")
        except Exception as e:
            logger.error(f"❌ 표 생성 실패: {e}")
            return False
        
        # 6. 문서 정보 조회 테스트
        logger.info("6. 문서 정보 조회 테스트")
        try:
            page_count = hwp_controller.hwp.GetPageCount()
            text_len = hwp_controller.hwp.GetTextLen()
            logger.info(f"✅ 문서 정보 조회 성공 - 페이지: {page_count}, 텍스트 길이: {text_len}")
        except Exception as e:
            logger.error(f"❌ 문서 정보 조회 실패: {e}")
            return False
        
        # 7. 문서 저장 테스트
        logger.info("7. 문서 저장 테스트")
        try:
            test_file = os.path.join(os.getcwd(), "test_document.hwp")
            act = hwp_controller.hwp.CreateAction("FileSaveAs")
            pset = act.CreateSet()
            pset.SetItem("filename", test_file)
            pset.SetItem("format", "HWP")
            act.Execute(pset)
            logger.info(f"✅ 문서 저장 성공: {test_file}")
        except Exception as e:
            logger.error(f"❌ 문서 저장 실패: {e}")
            return False
        
        logger.info("=== 모든 테스트 완료 ===")
        return True
        
    except ImportError as e:
        logger.error(f"❌ 모듈 임포트 실패: {e}")
        logger.error("필수 패키지를 설치해주세요: pip install mcp fastmcp pywin32")
        return False
    except Exception as e:
        logger.error(f"❌ 예상치 못한 오류: {e}")
        return False

def test_mcp_tools():
    """MCP 도구 기능 테스트"""
    
    try:
        logger.info("=== MCP 도구 기능 테스트 시작 ===")
        
        # 서버 모듈 임포트
        from advanced_hwp_server import (
            initialize_hwp, create_document, insert_text, 
            apply_font_format, create_table, get_document_info
        )
        
        # 1. 초기화 테스트
        logger.info("1. 초기화 테스트")
        result = initialize_hwp()
        logger.info(f"초기화 결과: {result}")
        
        # 2. 문서 생성 테스트
        logger.info("2. 문서 생성 테스트")
        result = create_document()
        logger.info(f"문서 생성 결과: {result}")
        
        # 3. 텍스트 삽입 테스트
        logger.info("3. 텍스트 삽입 테스트")
        result = insert_text("MCP 도구 테스트 텍스트")
        logger.info(f"텍스트 삽입 결과: {result}")
        
        # 4. 서식 적용 테스트
        logger.info("4. 서식 적용 테스트")
        result = apply_font_format("나눔고딕", 12, True, False, True, "blue")
        logger.info(f"서식 적용 결과: {result}")
        
        # 5. 표 생성 테스트
        logger.info("5. 표 생성 테스트")
        result = create_table(2, 4, True)
        logger.info(f"표 생성 결과: {result}")
        
        # 6. 문서 정보 조회 테스트
        logger.info("6. 문서 정보 조회 테스트")
        result = get_document_info()
        logger.info(f"문서 정보: {result}")
        
        logger.info("=== MCP 도구 테스트 완료 ===")
        return True
        
    except Exception as e:
        logger.error(f"❌ MCP 도구 테스트 실패: {e}")
        return False

def main():
    """메인 테스트 함수"""
    
    logger.info("Advanced HWP MCP Server 통합 테스트")
    logger.info("=" * 50)
    
    # 1. 기본 HWP 기능 테스트
    if test_hwp_server():
        logger.info("✅ 기본 HWP 기능 테스트 통과")
    else:
        logger.error("❌ 기본 HWP 기능 테스트 실패")
        return False
    
    # 잠시 대기
    time.sleep(2)
    
    # 2. MCP 도구 기능 테스트
    if test_mcp_tools():
        logger.info("✅ MCP 도구 기능 테스트 통과")
    else:
        logger.error("❌ MCP 도구 기능 테스트 실패")
        return False
    
    logger.info("=" * 50)
    logger.info("🎉 모든 테스트가 성공적으로 완료되었습니다!")
    logger.info("Advanced HWP MCP Server가 정상적으로 작동합니다.")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)