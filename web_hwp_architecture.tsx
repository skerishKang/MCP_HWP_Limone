import React, { useState } from 'react';

const WebHWPArchitecture = () => {
  const [selectedAI, setSelectedAI] = useState('claude');

  const aiServices = {
    claude: {
      name: 'Claude API',
      pros: ['뛰어난 한국어 이해', '정확한 명령 해석', '개발자 친화적'],
      cons: ['API 비용', '네트워크 의존성'],
      code: `// Claude API 예시
const response = await anthropic.messages.create({
  model: "claude-3-sonnet-20240229",
  messages: [{
    role: "user",
    content: "새 한글 문서를 만들고 제목을 '보고서'로 설정해주세요"
  }]
});`
    },
    gpt: {
      name: 'ChatGPT API',
      pros: ['Function Calling 지원', '광범위한 생태계', '안정적인 서비스'],
      cons: ['한국어 이해도 상대적으로 낮음', 'API 비용'],
      code: `// ChatGPT API 예시
const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: userCommand }],
  functions: hwpFunctions
});`
    },
    gemini: {
      name: 'Gemini API',
      pros: ['Google 생태계 연동', '멀티모달 지원', '경쟁력 있는 가격'],
      cons: ['상대적으로 새로운 서비스', '한국어 특화 부족'],
      code: `// Gemini API 예시
const result = await model.generateContent({
  contents: [{ role: "user", parts: [{ text: userCommand }] }]
});`
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-white">
      <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">
        🌐 웹용 HWP 자동화 시스템 설계
      </h1>

      {/* 아키텍처 다이어그램 */}
      <div className="mb-10 p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">시스템 아키텍처</h2>
        <div className="flex items-center justify-between text-sm">
          <div className="bg-blue-100 p-4 rounded-lg text-center">
            <div className="font-semibold">웹 브라우저</div>
            <div className="text-gray-600">사용자 인터페이스</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="bg-green-100 p-4 rounded-lg text-center">
            <div className="font-semibold">웹 애플리케이션</div>
            <div className="text-gray-600">React/Vue.js</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="bg-yellow-100 p-4 rounded-lg text-center">
            <div className="font-semibold">AI API</div>
            <div className="text-gray-600">Claude/GPT/Gemini</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="bg-purple-100 p-4 rounded-lg text-center">
            <div className="font-semibold">HWP 제어 서버</div>
            <div className="text-gray-600">Windows 서버</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="bg-red-100 p-4 rounded-lg text-center">
            <div className="font-semibold">한글 프로그램</div>
            <div className="text-gray-600">COM 객체</div>
          </div>
        </div>
      </div>

      {/* AI 서비스 선택 */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">AI 서비스 비교</h2>
        <div className="flex space-x-4 mb-6">
          {Object.keys(aiServices).map((key) => (
            <button
              key={key}
              onClick={() => setSelectedAI(key)}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                selectedAI === key
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              {aiServices[key].name}
            </button>
          ))}
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-green-50 p-4 rounded-lg">
            <h3 className="font-semibold text-green-800 mb-2">👍 장점</h3>
            <ul className="space-y-1">
              {aiServices[selectedAI].pros.map((pro, index) => (
                <li key={index} className="text-green-700">• {pro}</li>
              ))}
            </ul>
          </div>
          <div className="bg-red-50 p-4 rounded-lg">
            <h3 className="font-semibold text-red-800 mb-2">👎 단점</h3>
            <ul className="space-y-1">
              {aiServices[selectedAI].cons.map((con, index) => (
                <li key={index} className="text-red-700">• {con}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-4 bg-gray-100 p-4 rounded-lg">
          <h3 className="font-semibold mb-2">코드 예시</h3>
          <pre className="text-sm overflow-x-auto">
            <code>{aiServices[selectedAI].code}</code>
          </pre>
        </div>
      </div>

      {/* 개발 단계 */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">개발 단계별 계획</h2>
        <div className="space-y-4">
          {[
            { phase: '1단계', title: 'HWP 제어 API 서버', time: '1-2주', desc: '기존 MCP 코드를 웹 API로 변환' },
            { phase: '2단계', title: '웹 인터페이스 개발', time: '1-2주', desc: 'React 기반 사용자 인터페이스 구축' },
            { phase: '3단계', title: 'AI API 통합', time: '1주', desc: 'Claude/GPT/Gemini API 연동' },
            { phase: '4단계', title: '배포 및 테스트', time: '1주', desc: '서버 배포 및 통합 테스트' }
          ].map((stage, index) => (
            <div key={index} className="flex items-center p-4 bg-blue-50 rounded-lg">
              <div className="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center font-semibold mr-4">
                {index + 1}
              </div>
              <div className="flex-1">
                <div className="font-semibold">{stage.phase}: {stage.title}</div>
                <div className="text-gray-600 text-sm">{stage.desc}</div>
              </div>
              <div className="bg-purple-100 px-3 py-1 rounded-full text-sm font-medium">
                {stage.time}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 비교 테이블 */}
      <div className="bg-gray-50 p-6 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">현재 MCP vs 웹용 솔루션 비교</h2>
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr className="bg-gray-200">
                <th className="border p-3 text-left">항목</th>
                <th className="border p-3 text-center">현재 MCP (Claude Desktop)</th>
                <th className="border p-3 text-center">웹용 솔루션</th>
              </tr>
            </thead>
            <tbody>
              {[
                ['개발 상태', '✅ 완료', '❌ 개발 필요 (4-6주)'],
                ['사용 편의성', '⭐⭐⭐⭐⭐', '⭐⭐⭐⭐'],
                ['기능 완성도', '25개 고급 도구', '기본 기능부터 개발'],
                ['응답 속도', '즉시', '네트워크 지연'],
                ['비용', '무료', 'AI API 비용 발생'],
                ['접근성', 'Claude Desktop 필요', '어디서나 웹 접근'],
                ['안정성', '매우 안정적', '네트워크 의존적'],
                ['확장성', 'Claude Desktop 전용', '모든 AI 서비스 지원']
              ].map(([item, mcp, web], index) => (
                <tr key={index} className={index % 2 === 0 ? 'bg-white' : 'bg-gray-100'}>
                  <td className="border p-3 font-medium">{item}</td>
                  <td className="border p-3 text-center">{mcp}</td>
                  <td className="border p-3 text-center">{web}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* 결론 */}
      <div className="mt-8 p-6 bg-gradient-to-r from-green-100 to-blue-100 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">💡 결론 및 권장사항</h2>
        <div className="space-y-3">
          <div className="flex items-start">
            <span className="text-2xl mr-3">🎯</span>
            <div>
              <strong>단기 권장:</strong> 현재 MCP 솔루션 계속 사용
              <div className="text-gray-600 text-sm">이미 완성되어 있고, 안정적이며, 모든 기능이 구현됨</div>
            </div>
          </div>
          <div className="flex items-start">
            <span className="text-2xl mr-3">🚀</span>
            <div>
              <strong>장기 계획:</strong> 필요시 웹용 확장 개발
              <div className="text-gray-600 text-sm">더 넓은 사용자층을 위해 웹 기반 솔루션 고려</div>
            </div>
          </div>
          <div className="flex items-start">
            <span className="text-2xl mr-3">💡</span>
            <div>
              <strong>AI 선택:</strong> Claude API 권장
              <div className="text-gray-600 text-sm">한국어 이해도가 높고, 정확한 명령 해석 가능</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WebHWPArchitecture;