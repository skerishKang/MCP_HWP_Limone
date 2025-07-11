#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
한글 COM API 메서드 확인 스크립트
"""

import win32com.client
import pythoncom
import sys

# 콘솔 인코딩 설정
sys.stdout.reconfigure(encoding='utf-8')

def check_hwp_api():
    """한글 COM 객체의 사용 가능한 메서드를 확인"""
    try:
        pythoncom.CoInitialize()
        hwp = win32com.client.Dispatch("HWPFrame.HwpObject")
        
        print("=== 한글 COM 객체 정보 ===")
        print(f"객체 타입: {type(hwp)}")
        
        # 주요 속성과 메서드 확인
        print("\n=== 사용 가능한 속성/메서드 ===")
        methods = []
        for attr in dir(hwp):
            if not attr.startswith('_'):
                try:
                    obj = getattr(hwp, attr)
                    methods.append(attr)
                except:
                    pass
        
        # 중요한 메서드들 확인
        important_methods = [
            'PageCount', 'GetPageCount', 'GetFieldText', 'GetTextLen',
            'GetPos', 'SetPos', 'HAction', 'CreateAction', 'GetCurrentPage'
        ]
        
        print("\n=== 중요 메서드 확인 ===")
        for method in important_methods:
            if hasattr(hwp, method):
                print(f"[O] {method} - 사용 가능")
            else:
                print(f"[X] {method} - 사용 불가")
        
        # 실제 문서 정보 조회 시도
        print("\n=== 실제 기능 테스트 ===")
        try:
            # 새 문서 생성
            hwp.HAction.Run("FileNew")
            print("[O] 새 문서 생성 성공")
            
            # 페이지 수 확인 (다양한 방법 시도)
            try:
                if hasattr(hwp, 'PageCount'):
                    page_count = hwp.PageCount
                    print(f"[O] PageCount: {page_count}")
                elif hasattr(hwp, 'GetPageCount'):
                    page_count = hwp.GetPageCount()
                    print(f"[O] GetPageCount(): {page_count}")
                else:
                    print("[X] 페이지 수 조회 메서드를 찾을 수 없음")
            except Exception as e:
                print(f"[X] 페이지 수 조회 실패: {e}")
            
            # 텍스트 길이 확인
            try:
                if hasattr(hwp, 'GetTextLen'):
                    text_len = hwp.GetTextLen()
                    print(f"[O] GetTextLen(): {text_len}")
                else:
                    print("[X] GetTextLen 메서드를 찾을 수 없음")
            except Exception as e:
                print(f"[X] 텍스트 길이 조회 실패: {e}")
            
            # 현재 위치 확인
            try:
                if hasattr(hwp, 'GetPos'):
                    pos = hwp.GetPos()
                    print(f"[O] GetPos(): {pos}")
                else:
                    print("[X] GetPos 메서드를 찾을 수 없음")
            except Exception as e:
                print(f"[X] 현재 위치 조회 실패: {e}")
                
        except Exception as e:
            print(f"[X] 문서 생성 실패: {e}")
        
        # 모든 메서드 목록 출력 (처음 50개만)
        print(f"\n=== 전체 메서드 목록 (처음 50개) ===")
        for i, method in enumerate(sorted(methods)[:50]):
            print(f"{i+1:2d}. {method}")
        
        if len(methods) > 50:
            print(f"... 그 외 {len(methods) - 50}개 더 있음")
        
        pythoncom.CoUninitialize()
        return True
        
    except Exception as e:
        print(f"[X] 한글 COM 객체 초기화 실패: {e}")
        return False

if __name__ == "__main__":
    check_hwp_api()
