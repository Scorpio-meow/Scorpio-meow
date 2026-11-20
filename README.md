<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero.svg" alt="Scorpio-meow 天蠍喵喵" width="100%">
</picture>

**自架、可引用、能接進工作流程的 AI 工具：文件檢索、語音轉錄、叫號系統與 Agent Skill。**

[AskMiao](https://scorpio-meow.github.io/AskMiao/) · [ListenMiao](https://scorpio-meow.github.io/ListenMiao/) · [Threadkeep](https://scorpio-meow.github.io/Threadkeep/) · [DrillMiao](https://scorpio-meow.github.io/DrillMiao/) · [所有儲存庫](https://github.com/Scorpio-meow?tab=repositories)

</div>

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-featured-dark.svg">
    <img src="assets/h-featured.svg" alt="精選作品" width="720">
  </picture>
</h2>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://scorpio-meow.github.io/AskMiao/"><img src="assets/shots/AskMiao.webp" alt="AskMiao 對話畫面，回答附出處"></a>
      <br><b>AskMiao</b>：自架 RAG 聊天機器人，研究公司文件並標註每項論述出處。
      <br>FAISS 加 BM25 混合檢索；ReAct Agent 可建立與編輯 Word、Excel、PowerPoint、PDF；MCP 與 OpenAPI 工具需使用者核准。
      <br><a href="https://github.com/Scorpio-meow/AskMiao">原始碼</a> · <a href="https://scorpio-meow.github.io/AskMiao/">網站</a>
    </td>
    <td width="50%" valign="top">
      <a href="https://scorpio-meow.github.io/ListenMiao/"><img src="assets/shots/ListenMiao.png" alt="ListenMiao 字幕編輯器，含波形與說話者"></a>
      <br><b>ListenMiao</b>：本機網頁應用，以 Breeze ASR 把音訊轉成字幕與逐字稿，不上傳音訊。
      <br>台灣華語、中英夾雜與台語；講者分離、字幕編輯、SRT 與 DOCX 匯出、CLI、MCP server。
      <br><a href="https://github.com/Scorpio-meow/ListenMiao">原始碼</a> · <a href="https://scorpio-meow.github.io/ListenMiao/">網站</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://scorpio-meow.github.io/Threadkeep/"><img src="assets/shots/Threadkeep.png" alt="Threadkeep 控制面板"></a>
      <br><b>Threadkeep</b>：Manifest V3 瀏覽器擴充功能，一鍵保存 Threads 貼文的官方嵌入碼。
      <br>資料留在瀏覽器；瀑布流儀表板、標籤雲、即時預覽、.js 匯出。
      <br><a href="https://github.com/Scorpio-meow/Threadkeep">原始碼</a> · <a href="https://scorpio-meow.github.io/Threadkeep/">網站</a>
    </td>
    <td width="50%" valign="top">
      <a href="https://scorpio-meow.github.io/DrillMiao/"><img src="assets/shots/DrillMiao.webp" alt="DrillMiao 作答畫面"></a>
      <br><b>DrillMiao</b>：純前端模擬測驗與練習工具。
      <br>內建 11 個題庫；錯題重練、進度自動儲存、成績趨勢、CSV 與 JSON 匯出。
      <br><a href="https://github.com/Scorpio-meow/DrillMiao">原始碼</a> · <a href="https://scorpio-meow.github.io/DrillMiao/">網站</a>
    </td>
  </tr>
</table>

**CallMiao**：可嵌入任何網站的叫號系統。取號機、櫃檯後台、大廳顯示與語音叫號、手機追蹤、管理介面，全由單一伺服器提供（Bun 或 Node.js、Socket.IO、SQLite）。[原始碼](https://github.com/Scorpio-meow/CallMiao)

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-how-dark.svg">
    <img src="assets/h-how.svg" alt="我怎麼做" width="720">
  </picture>
</h2>

- **自架與本機優先**：ListenMiao 不上傳音訊，Threadkeep 的資料留在瀏覽器，AskMiao 可接 Ollama 或 vLLM 在自己的環境推論。
- **每項論述附出處**：AskMiao 回答時以 [n] 對回原文段落，查不到就照實說。
- **動手前先確認**：LINE-skill 的 Messaging API 腳本預設先 dry-run，AskMiao 的 MCP 與 OpenAPI 工具在呼叫前須經使用者同意。
- **少依賴、可驗證**：DrillMiao 與 Liquid-Cipher 以零依賴的原生網頁實作，Liquid-Cipher 的每一關都由 BFS 解題器驗證可解。

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-skills-dark.svg">
    <img src="assets/h-skills.svg" alt="Agent Skills" width="720">
  </picture>
</h2>

- **[LINE-skill](https://github.com/Scorpio-meow/LINE-skill)**：協助 AI 編程助手開發 LINE Bot、LIFF 與 LINE Login，含即時官方文件查詢與先試跑的 Messaging API 腳本。
- **[Threads-skill](https://github.com/Scorpio-meow/Threads-skill)**：協助 AI 編程助手撰寫與除錯 Meta Threads API 整合，或以自己的權杖發文與取得洞察（[網站](https://scorpio-meow.github.io/Threads-skill/)）。
- **[senior-network-engineer-skill-bundle](https://github.com/Scorpio-meow/senior-network-engineer-skill-bundle)**：資深網路工程師技能包，跨廠牌主技能加 Palo Alto、Fortinet、Cisco、HPE Aruba 子技能。
- **[Threads-API](https://github.com/Scorpio-meow/Threads-API)**：Meta Threads API 文件的非官方 Markdown 鏡像（49 頁），方便搜尋、引用與 RAG。

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-stats-dark.svg">
    <img src="assets/h-stats.svg" alt="GitHub 活動" width="720">
  </picture>
</h2>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <img src="assets/stats.svg" alt="公開儲存庫的語言分布" width="800">
</picture>

<!--RECENT:START-->
近期更新：[ListenMiao](https://github.com/Scorpio-meow/ListenMiao)（11-19） · [CallMiao](https://github.com/Scorpio-meow/CallMiao)（11-18） · [AskMiao](https://github.com/Scorpio-meow/AskMiao)（11-15） · [DrillMiao](https://github.com/Scorpio-meow/DrillMiao)（11-14） · [Threadfolio-Example](https://github.com/Scorpio-meow/Threadfolio-Example)（11-14）
<!--RECENT:END-->

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-tech-dark.svg">
    <img src="assets/h-tech.svg" alt="常用技術" width="720">
  </picture>
</h2>

- **AI 系統**：RAG、混合檢索（FAISS、BM25）、ReAct Agent、Agent Skills、MCP、語音辨識；模型支援 OpenAI、Claude、Gemini、Ollama、vLLM
- **應用整合**：LINE Messaging API、LIFF、Threads API、Manifest V3 擴充功能、GitHub Pages
- **後端與前端**：Python、FastAPI、Bun、Node.js、Express、Socket.IO、SQLite、原生 JavaScript
- **基礎設施**：自架部署、Docker、本機推論（CPU、Intel GPU、NVIDIA、AMD）

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-lab-dark.svg">
    <img src="assets/h-lab.svg" alt="Miao Lab" width="720">
  </picture>
</h2>

- [Miao-Playground](https://github.com/Scorpio-meow/Miao-Playground)：五個小遊戲與互動工具的集合
- [Liquid-Cipher](https://github.com/Scorpio-meow/Liquid-Cipher)：無盡倒水排序 PWA，每一關都由 BFS 解題器驗證可解（[試玩](https://scorpio-meow.github.io/Liquid-Cipher/)）
- [Stardust-Labyrinth](https://github.com/Scorpio-meow/Stardust-Labyrinth)：終端機迷宮遊戲，幽靈以曼哈頓距離追捕
- [Quantum-Duel](https://github.com/Scorpio-meow/Quantum-Duel)：回合制終端機對戰，AI 依戰況調整出招權重
- [Azure-OpenAI-VS-Code-Proxy](https://github.com/Scorpio-meow/Azure-OpenAI-VS-Code-Proxy)：修正 VS Code 與 Azure OpenAI 溫度參數相容問題的本機 FastAPI 代理
- [COBOL-Introductory-Examples](https://github.com/Scorpio-meow/COBOL-Introductory-Examples)：COBOL 銀行系統範例

<h2>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/h-contact-dark.svg">
    <img src="assets/h-contact.svg" alt="聯絡與回饋" width="720">
  </picture>
</h2>

歡迎在各專案的 Issues 提出問題與建議：[AskMiao](https://github.com/Scorpio-meow/AskMiao/issues) · [ListenMiao](https://github.com/Scorpio-meow/ListenMiao/issues) · [Threadkeep](https://github.com/Scorpio-meow/Threadkeep/issues) · [CallMiao](https://github.com/Scorpio-meow/CallMiao/issues)

追蹤與合作：[github.com/Scorpio-meow](https://github.com/Scorpio-meow)

Email：[yao921024@gmail.com](mailto:yao921024@gmail.com)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer.svg" alt="Scorpio-meow 天蠍喵喵" width="100%">
</picture>
