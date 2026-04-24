from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENGLISH_README = ROOT / "README.md"

LANGUAGE_LINE = (
    "Languages: [English](README.md) | [简体中文](README.zh-CN.md) | "
    "[繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | "
    "[Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md)\n"
)

SECTION_KEYS = [
    ("## 📷 Photography & Photorealism", "photography", "-photography--photorealism"),
    ("## 🎮 Game & Entertainment", "game", "-game--entertainment"),
    ("## 📱 UI/UX & Social Media", "uiux", "-uiux--social-media"),
    ("## 🎬 Video, Animation & Collage", "video", "-video-animation--collage"),
    ("## 📰 Typography & Poster Design", "typography", "-typography--poster-design"),
    ("## 📚 Infographics, Education & Documents", "infographics", "-infographics-education--documents"),
    ("## 🎭 Character & Consistency", "character", "-character--consistency"),
    ("## 🖼️ Image Editing & Style Transfer", "image_editing", "-image-editing--style-transfer"),
]

CONTENT_H3_COUNT = 54

CONFIG = {
    "zh-CN": {
        "file": "README.zh-CN.md",
        "title": "# Awesome GPT Image 2 简体中文",
        "updated": "最后更新于",
        "intro": [
            "一个精选的 GPT Image 2 优质提示词与示例合集，适合学习提示词工程，并探索 OpenAI GPT Image 2 的创作潜力。",
            "本仓库聚焦于来自 X（Twitter）和社区的高保真图像提示词。无论你想要照片级游戏截图、风格化视觉，还是复杂的创意实验，都能在这里找到高效输入，充分释放 GPT Image 2 的能力。",
        ],
        "why_heading": "## 为什么选择 GPT Image 2？",
        "why_lead": "GPT Image 2 相比 1.5 版本有明显升级：",
        "why_bullets": [
            "- **更好的世界知识** - 对真实世界物体和场景的表达更准确",
            "- **更强的风格理解** - 能够复现特定艺术风格和游戏美学",
            "- **更好的指令遵循** - 对复杂要求的执行更精准",
            "- **更强的照片真实感** - 输出更像真实照片或截图",
        ],
        "web_heading": "## [点击这里查看这个提示词库的网页版本](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## 目录",
        "sections": {
            "photography": ("📷 摄影与照片级写实", "用于生成超真实场景、自然摄影质感和复杂光照的提示词。"),
            "game": ("🎮 游戏与娱乐", "利用 GPT Image 2 复现特定游戏美学并生成真实游戏截图感的提示词。"),
            "uiux": ("📱 UI / UX 与社交媒体", "用于生成真实 App 界面、社交媒体帖子和数字视觉设计的提示词。"),
            "video": ("🎬 视频、动画与拼贴", "用于生成视频感内容、动画序列和拼贴画面的提示词。"),
            "typography": ("📰 字体排版与海报设计", "用于测试复杂文字排版、信息密度和高完成度视觉设计的提示词。"),
            "infographics": ("📚 信息图、教育与文档", "用于生成知识卡片、教育材料、训练计划和高信息密度版式的提示词。"),
            "character": ("🎭 角色与一致性", "用于测试角色在多张图像中的一致性与风格复现能力的提示词。"),
            "image_editing": ("🖼️ 图像编辑与风格迁移", "用于图像编辑、风格迁移和参考图驱动生成的提示词。"),
        },
        "labels": {"prompt": "提示词", "source": "来源", "note": "说明"},
        "resources_heading": "## 📊 资源",
        "resources_official": "### 官方资源",
        "resources_community": "### 社区",
        "resources_bullets": [
            "- 在 X 上使用 #GPTImage2 分享你的提示词和结果",
            "- 参与关于提示词工程技巧的讨论",
        ],
        "contributing_heading": "## 🤝 贡献",
        "contributing_intro": "欢迎贡献内容，欢迎直接提交 Pull Request。",
        "to_contribute": "**贡献方式：**",
        "contributing_steps": [
            "1. Fork 本仓库",
            "2. 创建你的功能分支（`git checkout -b feature/AmazingFeature`）",
            "3. 提交你的改动（`git commit -m 'Add some AmazingFeature'`）",
            "4. 推送到分支（`git push origin feature/AmazingFeature`）",
            "5. 创建 Pull Request",
        ],
        "guidelines": "**贡献指南：**",
        "guideline_bullets": [
            "- 提供完整的提示词文本",
            "- 附上 X / Twitter 来源链接",
            "- 尽可能添加示例图片",
            "- 放入合适的分类",
        ],
        "ack_heading": "## 致谢",
        "ack_1": "特别感谢中文 AI 社区贡献了这批完整的测试样例。Typography、Photorealism、UI/UX、Consistency 和 Image Editing 部分新增的提示词来自：",
        "ack_2": "这些真实世界测试场景为理解 GPT Image 2 在排版、真实场景生成、界面还原、角色一致性和图像编辑任务上的能力提供了很有价值的参考。",
        "ack_3": "所有内容均来自互联网。如你认为其中内容侵犯了你的版权，请创建 issue，我们会及时处理。",
        "star_heading": "## Star History",
        "license_heading": "## 许可证",
        "license_text": "本项目采用 Creative Commons Attribution 4.0 International License 许可发布。详情请见 [LICENSE](LICENSE) 文件。",
        "footer": "*本仓库由社区维护，与 OpenAI 无关联。*",
    },
    "zh-TW": {
        "file": "README.zh-TW.md",
        "title": "# Awesome GPT Image 2 繁體中文",
        "updated": "最後更新於",
        "intro": [
            "一份精選的 GPT Image 2 優質提示詞與示例合集，方便學習提示詞工程，並探索 OpenAI GPT Image 2 的創作潛力。",
            "本倉庫聚焦於來自 X（Twitter）與社群的高保真圖像提示詞。無論你想做照片級遊戲截圖、風格化視覺，或更複雜的創意實驗，都能在這裡找到高效輸入，充分釋放 GPT Image 2 的能力。",
        ],
        "why_heading": "## 為什麼選擇 GPT Image 2？",
        "why_lead": "相較於 1.5 版本，GPT Image 2 有明顯升級：",
        "why_bullets": [
            "- **更好的世界知識** - 對真實世界物件與場景的表達更準確",
            "- **更強的風格理解** - 能夠重現特定藝術風格與遊戲美學",
            "- **更好的指令遵循** - 對複雜要求的執行更精準",
            "- **更強的照片真實感** - 輸出更像真正的照片或截圖",
        ],
        "web_heading": "## [點這裡查看這個提示詞庫的網頁版本](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## 目錄",
        "sections": {
            "photography": ("📷 攝影與照片級寫實", "用於生成超真實場景、自然攝影質感與複雜光線效果的提示詞。"),
            "game": ("🎮 遊戲與娛樂", "用於重現特定遊戲美學並生成真實遊戲截圖感的提示詞。"),
            "uiux": ("📱 UI / UX 與社群媒體", "用於生成真實 App 介面、社群貼文與數位視覺設計的提示詞。"),
            "video": ("🎬 影片、動畫與拼貼", "用於生成帶有影片感的畫面、動畫序列與拼貼構圖的提示詞。"),
            "typography": ("📰 字體排版與海報設計", "用於測試複雜文字排版、資訊密度與高完成度視覺設計的提示詞。"),
            "infographics": ("📚 資訊圖、教育與文件", "用於生成知識卡、教育材料、訓練計畫與高資訊密度版式的提示詞。"),
            "character": ("🎭 角色與一致性", "用於測試角色在多張圖像中的一致性與風格重現能力的提示詞。"),
            "image_editing": ("🖼️ 圖像編輯與風格轉換", "用於圖像編輯、風格轉換與參考圖驅動生成的提示詞。"),
        },
        "labels": {"prompt": "提示詞", "source": "來源", "note": "說明"},
        "resources_heading": "## 📊 資源",
        "resources_official": "### 官方資源",
        "resources_community": "### 社群",
        "resources_bullets": [
            "- 在 X 上使用 #GPTImage2 分享你的提示詞與結果",
            "- 參與關於提示詞工程技巧的討論",
        ],
        "contributing_heading": "## 🤝 貢獻",
        "contributing_intro": "歡迎貢獻內容，也歡迎直接提交 Pull Request。",
        "to_contribute": "**貢獻方式：**",
        "contributing_steps": [
            "1. Fork 這個倉庫",
            "2. 建立你的功能分支（`git checkout -b feature/AmazingFeature`）",
            "3. 提交你的修改（`git commit -m 'Add some AmazingFeature'`）",
            "4. 推送到分支（`git push origin feature/AmazingFeature`）",
            "5. 建立 Pull Request",
        ],
        "guidelines": "**貢獻指南：**",
        "guideline_bullets": [
            "- 附上完整的提示詞文字",
            "- 提供 X / Twitter 來源連結",
            "- 盡量加入示例圖片",
            "- 放入正確的分類",
        ],
        "ack_heading": "## 致謝",
        "ack_1": "特別感謝中文 AI 社群提供了這批完整測試案例。Typography、Photorealism、UI/UX、Consistency 與 Image Editing 區塊新增的提示詞來自：",
        "ack_2": "這些真實世界測試場景，對理解 GPT Image 2 在排版、真實場景生成、介面還原、角色一致性與圖像編輯任務上的能力很有幫助。",
        "ack_3": "所有內容均來自網路。如果你認為其中內容侵犯了你的版權，請建立 issue，我們會及時處理。",
        "star_heading": "## Star History",
        "license_heading": "## 授權",
        "license_text": "本專案採用 Creative Commons Attribution 4.0 International License。詳情請見 [LICENSE](LICENSE) 檔案。",
        "footer": "*本倉庫由社群維護，與 OpenAI 無關。*",
    },
    "ja": {
        "file": "README.ja.md",
        "title": "# Awesome GPT Image 2 日本語",
        "updated": "最終更新",
        "intro": [
            "GPT Image 2 の優れたプロンプトと作例を集めたキュレーション集です。プロンプトエンジニアリングを学び、OpenAI の GPT Image 2 が持つ創作力を探るための出発点として使えます。",
            "このリポジトリは、X（Twitter）やコミュニティで共有された高品質な画像プロンプトに焦点を当てています。フォトリアルなゲーム画面、スタイライズされたビジュアル、複雑なクリエイティブ実験まで、GPT Image 2 の力を引き出すための実践的な入力をまとめています。",
        ],
        "why_heading": "## なぜ GPT Image 2 なのか？",
        "why_lead": "GPT Image 2 は 1.5 から大きく進化しており、次のような強みがあります。",
        "why_bullets": [
            "- **現実世界の知識が向上** - 実在する物体や場面をより正確に表現できる",
            "- **スタイル理解が向上** - 特定のアートスタイルやゲーム美学を再現しやすい",
            "- **指示追従性が向上** - 複雑な要求にもより正確に従える",
            "- **フォトリアリズムが向上** - 本物の写真やスクリーンショットのような出力を作れる",
        ],
        "web_heading": "## [このプロンプトライブラリの Web 版を見るにはここをクリック](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## 目次",
        "sections": {
            "photography": ("📷 写真・フォトリアリズム", "超リアルなシーン、自然な写真表現、複雑なライティングを再現するためのプロンプト。"),
            "game": ("🎮 ゲーム・エンターテインメント", "特定のゲーム美学を再現し、本物らしいゲーム画面を作るためのプロンプト。"),
            "uiux": ("📱 UI / UX・ソーシャルメディア", "リアルなアプリ画面、SNS 投稿、デジタルビジュアルを生成するためのプロンプト。"),
            "video": ("🎬 動画・アニメーション・コラージュ", "動画的なフレーム、連続演出、コラージュ表現を作るためのプロンプト。"),
            "typography": ("📰 タイポグラフィ・ポスターデザイン", "複雑な文字組み、高密度レイアウト、完成度の高いビジュアルデザインを試すためのプロンプト。"),
            "infographics": ("📚 インフォグラフィック・教育・文書", "知識カード、教材、トレーニング計画、高密度レイアウトを作るためのプロンプト。"),
            "character": ("🎭 キャラクター・一貫性", "複数画像間でのキャラクター一貫性やスタイル再現性を試すためのプロンプト。"),
            "image_editing": ("🖼️ 画像編集・スタイル変換", "画像編集、スタイル変換、参照画像ベース生成のためのプロンプト。"),
        },
        "labels": {"prompt": "プロンプト", "source": "出典", "note": "メモ"},
        "resources_heading": "## 📊 リソース",
        "resources_official": "### 公式リソース",
        "resources_community": "### コミュニティ",
        "resources_bullets": [
            "- X で #GPTImage2 を付けてプロンプトや結果を共有する",
            "- プロンプトエンジニアリングの手法について議論に参加する",
        ],
        "contributing_heading": "## 🤝 コントリビュート",
        "contributing_intro": "コントリビューション歓迎です。Pull Request をぜひ送ってください。",
        "to_contribute": "**参加方法：**",
        "contributing_steps": [
            "1. リポジトリを Fork する",
            "2. 機能ブランチを作成する（`git checkout -b feature/AmazingFeature`）",
            "3. 変更をコミットする（`git commit -m 'Add some AmazingFeature'`）",
            "4. ブランチへ push する（`git push origin feature/AmazingFeature`）",
            "5. Pull Request を作成する",
        ],
        "guidelines": "**投稿ガイドライン：**",
        "guideline_bullets": [
            "- 完全なプロンプト本文を含める",
            "- X / Twitter の出典リンクを付ける",
            "- 可能であれば作例画像を追加する",
            "- 適切なカテゴリに分類する",
        ],
        "ack_heading": "## 謝辞",
        "ack_1": "中国語 AI コミュニティが提供してくれた包括的なテストケースに感謝します。Typography、Photorealism、UI/UX、Consistency、Image Editing セクションに追加された新しいプロンプトは以下から来ています。",
        "ack_2": "これらの現実的なテストシナリオは、GPT Image 2 がタイポグラフィ、写実的なシーン生成、UI 再現、キャラクター一貫性、画像編集でどこまでできるのかを理解するうえで非常に有用です。",
        "ack_3": "すべての内容はインターネットから収集しています。もし著作権侵害に該当すると考える場合は、issue を作成してください。確認のうえ対応します。",
        "star_heading": "## Star History",
        "license_heading": "## ライセンス",
        "license_text": "このプロジェクトは Creative Commons Attribution 4.0 International License の下で公開されています。詳細は [LICENSE](LICENSE) を参照してください。",
        "footer": "*このリポジトリはコミュニティによって管理されており、OpenAI とは提携していません。*",
    },
    "ko": {
        "file": "README.ko.md",
        "title": "# Awesome GPT Image 2 한국어",
        "updated": "마지막 업데이트",
        "intro": [
            "GPT Image 2의 뛰어난 프롬프트와 예제를 모아 둔 큐레이션 컬렉션입니다. 프롬프트 엔지니어링을 익히고 OpenAI GPT Image 2의 창작 잠재력을 탐색하는 데 유용합니다.",
            "이 저장소는 X(트위터)와 커뮤니티에서 공유된 고품질 이미지 프롬프트에 초점을 맞춥니다. 포토리얼한 게임 스크린샷, 스타일화된 비주얼, 복잡한 크리에이티브 실험까지 GPT Image 2의 성능을 끌어내는 입력을 정리해 두었습니다.",
        ],
        "why_heading": "## 왜 GPT Image 2인가?",
        "why_lead": "GPT Image 2는 1.5에 비해 크게 업그레이드되었으며 다음과 같은 장점이 있습니다.",
        "why_bullets": [
            "- **더 나은 세계 지식** - 실제 사물과 장면을 더 정확하게 표현할 수 있음",
            "- **향상된 스타일 이해** - 특정 아트 스타일과 게임 미학을 더 잘 재현함",
            "- **강화된 지시 충실도** - 복잡한 요구사항도 더 정밀하게 따름",
            "- **향상된 포토리얼리즘** - 실제 사진이나 스크린샷 같은 결과를 생성함",
        ],
        "web_heading": "## [이 프롬프트 라이브러리의 웹 버전을 보려면 여기를 클릭하세요](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## 목차",
        "sections": {
            "photography": ("📷 사진과 포토리얼리즘", "초현실적인 장면, 자연스러운 사진 질감, 복잡한 조명을 만들기 위한 프롬프트입니다."),
            "game": ("🎮 게임과 엔터테인먼트", "특정 게임 미학을 재현하고 실제 게임 화면 같은 이미지를 만들기 위한 프롬프트입니다."),
            "uiux": ("📱 UI / UX 와 소셜 미디어", "현실적인 앱 화면, 소셜 미디어 게시물, 디지털 비주얼을 생성하기 위한 프롬프트입니다."),
            "video": ("🎬 영상, 애니메이션, 콜라주", "영상 같은 장면, 애니메이션 시퀀스, 콜라주 구성을 만들기 위한 프롬프트입니다."),
            "typography": ("📰 타이포그래피와 포스터 디자인", "복잡한 텍스트 레이아웃, 높은 정보 밀도, 완성도 높은 비주얼 디자인을 시험하기 위한 프롬프트입니다."),
            "infographics": ("📚 인포그래픽, 교육, 문서", "지식 카드, 교육 자료, 훈련 계획, 고밀도 레이아웃을 만들기 위한 프롬프트입니다."),
            "character": ("🎭 캐릭터와 일관성", "여러 이미지에서 캐릭터 일관성과 스타일 재현 능력을 테스트하기 위한 프롬프트입니다."),
            "image_editing": ("🖼️ 이미지 편집과 스타일 전이", "이미지 편집, 스타일 전이, 레퍼런스 기반 생성에 사용하는 프롬프트입니다."),
        },
        "labels": {"prompt": "프롬프트", "source": "출처", "note": "메모"},
        "resources_heading": "## 📊 리소스",
        "resources_official": "### 공식 리소스",
        "resources_community": "### 커뮤니티",
        "resources_bullets": [
            "- X에서 #GPTImage2 해시태그로 프롬프트와 결과를 공유하세요",
            "- 프롬프트 엔지니어링 기법에 대한 토론에 참여하세요",
        ],
        "contributing_heading": "## 🤝 기여",
        "contributing_intro": "기여를 환영합니다. Pull Request를 자유롭게 보내 주세요.",
        "to_contribute": "**기여 방법:**",
        "contributing_steps": [
            "1. 저장소를 Fork 합니다",
            "2. 기능 브랜치를 만듭니다 (`git checkout -b feature/AmazingFeature`)",
            "3. 변경 사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`)",
            "4. 브랜치에 push 합니다 (`git push origin feature/AmazingFeature`)",
            "5. Pull Request를 엽니다",
        ],
        "guidelines": "**기여 가이드라인:**",
        "guideline_bullets": [
            "- 전체 프롬프트 텍스트를 포함하세요",
            "- X / Twitter 출처 링크를 제공하세요",
            "- 가능하면 예시 이미지를 추가하세요",
            "- 적절한 카테고리로 분류하세요",
        ],
        "ack_heading": "## 감사의 말",
        "ack_1": "중국 AI 커뮤니티가 제공한 포괄적인 테스트 케이스에 감사드립니다. Typography, Photorealism, UI/UX, Consistency, Image Editing 섹션에 추가된 새 프롬프트는 다음 출처에서 왔습니다.",
        "ack_2": "이 실제 테스트 시나리오는 GPT Image 2가 타이포그래피, 사실적 장면 생성, UI 재현, 캐릭터 일관성, 이미지 편집 작업에서 어떤 능력을 갖고 있는지 이해하는 데 큰 도움이 됩니다.",
        "ack_3": "모든 콘텐츠는 인터넷에서 수집되었습니다. 저작권 침해라고 판단되면 issue를 생성해 주세요. 확인 후 조치하겠습니다.",
        "star_heading": "## Star History",
        "license_heading": "## 라이선스",
        "license_text": "이 프로젝트는 Creative Commons Attribution 4.0 International License에 따라 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.",
        "footer": "*이 저장소는 커뮤니티가 관리하며 OpenAI와 직접적인 관련이 없습니다.*",
    },
    "fr": {
        "file": "README.fr.md",
        "title": "# Awesome GPT Image 2 Français",
        "updated": "Dernière mise à jour",
        "intro": [
            "Une collection sélectionnée des meilleurs prompts et exemples GPT Image 2. Une base de référence pour apprendre le prompt engineering et explorer le potentiel créatif du modèle GPT Image 2 d’OpenAI.",
            "Ce dépôt se concentre sur des prompts d’image à haute fidélité issus de X (Twitter) et de la communauté. Que vous cherchiez des captures de jeu photoréalistes, des visuels stylisés ou des expérimentations créatives complexes, vous trouverez ici des entrées efficaces pour exploiter GPT Image 2 au maximum.",
        ],
        "why_heading": "## Pourquoi GPT Image 2 ?",
        "why_lead": "GPT Image 2 représente une nette évolution par rapport à la version 1.5 :",
        "why_bullets": [
            "- **Meilleure compréhension du monde** - représentation plus précise des objets et scènes du monde réel",
            "- **Meilleure compréhension des styles** - reproduction plus fidèle de styles artistiques et d’esthétiques de jeu",
            "- **Meilleur respect des consignes** - exécution plus précise d’instructions complexes",
            "- **Photoréalisme renforcé** - des images qui ressemblent davantage à de vraies photos ou captures",
        ],
        "web_heading": "## [Cliquez ici pour voir la version web de cette bibliothèque de prompts](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## Table des matières",
        "sections": {
            "photography": ("📷 Photographie et photoréalisme", "Prompts pour créer des scènes ultra réalistes, des caractéristiques photographiques crédibles et des éclairages complexes."),
            "game": ("🎮 Jeu et divertissement", "Prompts pour reproduire des esthétiques de jeu spécifiques et générer des captures in-game crédibles."),
            "uiux": ("📱 UI / UX et réseaux sociaux", "Prompts pour générer des interfaces d’app réalistes, des publications sociales et des visuels numériques soignés."),
            "video": ("🎬 Vidéo, animation et collage", "Prompts pour créer des visuels à l’aspect vidéo, des séquences animées et des compositions en collage."),
            "typography": ("📰 Typographie et design d'affiche", "Prompts pour tester la mise en page typographique complexe, la densité d’information et les designs visuels très aboutis."),
            "infographics": ("📚 Infographies, éducation et documents", "Prompts pour produire des fiches de connaissance, supports éducatifs, plans d’entraînement et mises en page riches en informations."),
            "character": ("🎭 Personnages et cohérence", "Prompts qui testent la cohérence d’un personnage sur plusieurs images et la reproduction de style."),
            "image_editing": ("🖼️ Édition d'image et transfert de style", "Prompts pour l’édition d’image, le transfert de style et la génération guidée par référence."),
        },
        "labels": {"prompt": "Prompt", "source": "Source", "note": "Note"},
        "resources_heading": "## 📊 Ressources",
        "resources_official": "### Ressources officielles",
        "resources_community": "### Communauté",
        "resources_bullets": [
            "- Partagez vos prompts et résultats sur X avec #GPTImage2",
            "- Rejoignez les discussions autour des techniques de prompt engineering",
        ],
        "contributing_heading": "## 🤝 Contribution",
        "contributing_intro": "Les contributions sont les bienvenues. N’hésitez pas à ouvrir une Pull Request.",
        "to_contribute": "**Pour contribuer :**",
        "contributing_steps": [
            "1. Forkez le dépôt",
            "2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)",
            "3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)",
            "4. Poussez la branche (`git push origin feature/AmazingFeature`)",
            "5. Ouvrez une Pull Request",
        ],
        "guidelines": "**Règles de contribution :**",
        "guideline_bullets": [
            "- Inclure le texte complet du prompt",
            "- Fournir le lien source X / Twitter",
            "- Ajouter des images d’exemple si possible",
            "- Classer le contenu dans la bonne catégorie",
        ],
        "ack_heading": "## Remerciements",
        "ack_1": "Un grand merci à la communauté IA chinoise pour ces cas de test très complets. Les nouveaux prompts ajoutés aux sections Typography, Photorealism, UI/UX, Consistency et Image Editing proviennent de :",
        "ack_2": "Ces scénarios de test issus du monde réel apportent des informations précieuses sur les capacités de GPT Image 2 en typographie, génération de scènes réalistes, recréation d’interfaces, cohérence de personnage et édition d’image.",
        "ack_3": "Tout le contenu provient d’Internet. Si vous estimez qu’un élément enfreint vos droits d’auteur, ouvrez une issue et nous le retirerons.",
        "star_heading": "## Historique des étoiles",
        "license_heading": "## Licence",
        "license_text": "Ce projet est publié sous licence Creative Commons Attribution 4.0 International. Voir le fichier [LICENSE](LICENSE) pour les détails.",
        "footer": "*Ce dépôt est maintenu par la communauté et n’est pas affilié à OpenAI.*",
    },
    "de": {
        "file": "README.de.md",
        "title": "# Awesome GPT Image 2 Deutsch",
        "updated": "Zuletzt aktualisiert",
        "intro": [
            "Eine kuratierte Sammlung der besten GPT Image 2 Prompts und Beispiele. Eine praktische Referenz, um Prompt Engineering zu lernen und das kreative Potenzial von OpenAI GPT Image 2 zu erkunden.",
            "Dieses Repository konzentriert sich auf hochwertige Bild-Prompts aus X (Twitter) und der Community. Ob fotorealistische Spielscreenshots, stilisierte Visuals oder komplexe kreative Experimente: Hier findest du wirksame Eingaben, um das volle Potenzial von GPT Image 2 auszuschöpfen.",
        ],
        "why_heading": "## Warum GPT Image 2?",
        "why_lead": "GPT Image 2 ist ein deutlicher Schritt nach vorn gegenüber Version 1.5 und bietet:",
        "why_bullets": [
            "- **Besseres Weltwissen** - realistische Objekte und Szenen werden präziser dargestellt",
            "- **Besseres Stilverständnis** - bestimmte Kunststile und Spielästhetiken lassen sich zuverlässiger reproduzieren",
            "- **Stärkere Befolgung von Anweisungen** - komplexe Vorgaben werden präziser umgesetzt",
            "- **Mehr Fotorealismus** - Ergebnisse wirken deutlich stärker wie echte Fotos oder Screenshots",
        ],
        "web_heading": "## [Klicke hier, um die Web-Version dieser Prompt-Bibliothek zu sehen](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## Inhaltsverzeichnis",
        "sections": {
            "photography": ("📷 Fotografie und Fotorealismus", "Prompts für ultra-realistische Szenen, glaubwürdige Fotoeigenschaften und komplexe Lichtstimmungen."),
            "game": ("🎮 Spiele und Unterhaltung", "Prompts, um bestimmte Spielästhetiken zu reproduzieren und glaubwürdige In-Game-Screenshots zu erzeugen."),
            "uiux": ("📱 UI / UX und Social Media", "Prompts für realistische App-Oberflächen, Social-Media-Posts und digitale Visuals."),
            "video": ("🎬 Video, Animation und Collage", "Prompts für videohafte Szenen, animierte Sequenzen und Collage-Kompositionen."),
            "typography": ("📰 Typografie und Posterdesign", "Prompts zum Testen komplexer Typografie, hoher Informationsdichte und ausgearbeiteter visueller Gestaltung."),
            "infographics": ("📚 Infografiken, Bildung und Dokumente", "Prompts für Wissenskarten, Lernmaterialien, Trainingspläne und informationsdichte Layouts."),
            "character": ("🎭 Figuren und Konsistenz", "Prompts zum Testen von Figurenkonsistenz über mehrere Bilder hinweg und zur Stilreproduktion."),
            "image_editing": ("🖼️ Bildbearbeitung und Stiltransfer", "Prompts für Bildbearbeitung, Stiltransfer und referenzbasierte Generierung."),
        },
        "labels": {"prompt": "Prompt", "source": "Quelle", "note": "Hinweis"},
        "resources_heading": "## 📊 Ressourcen",
        "resources_official": "### Offizielle Ressourcen",
        "resources_community": "### Community",
        "resources_bullets": [
            "- Teile deine Prompts und Ergebnisse auf X mit #GPTImage2",
            "- Nimm an Diskussionen über Prompt-Engineering-Techniken teil",
        ],
        "contributing_heading": "## 🤝 Beitrag",
        "contributing_intro": "Beiträge sind willkommen. Reiche gerne eine Pull Request ein.",
        "to_contribute": "**So kannst du beitragen:**",
        "contributing_steps": [
            "1. Forke das Repository",
            "2. Erstelle einen Feature-Branch (`git checkout -b feature/AmazingFeature`)",
            "3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)",
            "4. Pushe den Branch (`git push origin feature/AmazingFeature`)",
            "5. Öffne eine Pull Request",
        ],
        "guidelines": "**Beitragsrichtlinien:**",
        "guideline_bullets": [
            "- Den vollständigen Prompt-Text angeben",
            "- Den X / Twitter-Quelllink angeben",
            "- Wenn möglich Beispielbilder hinzufügen",
            "- Passend kategorisieren",
        ],
        "ack_heading": "## Danksagung",
        "ack_1": "Besonderer Dank an die chinesische KI-Community für diese umfassenden Testfälle. Die neuen Prompts in den Bereichen Typography, Photorealism, UI/UX, Consistency und Image Editing stammen aus:",
        "ack_2": "Diese realen Testszenarien liefern wertvolle Einblicke in die Fähigkeiten von GPT Image 2 bei Typografie, realistischen Szenen, UI-Rekonstruktion, Figurenkonsistenz und Bildbearbeitung.",
        "ack_3": "Alle Inhalte stammen aus dem Internet. Falls du der Ansicht bist, dass etwas deine Urheberrechte verletzt, eröffne bitte ein Issue, dann entfernen wir es.",
        "star_heading": "## Star-Verlauf",
        "license_heading": "## Lizenz",
        "license_text": "Dieses Projekt steht unter der Creative Commons Attribution 4.0 International License. Details findest du in der Datei [LICENSE](LICENSE).",
        "footer": "*Dieses Repository wird von der Community gepflegt und ist nicht mit OpenAI verbunden.*",
    },
    "es": {
        "file": "README.es.md",
        "title": "# Awesome GPT Image 2 Español",
        "updated": "Última actualización",
        "intro": [
            "Una colección curada con los mejores prompts y ejemplos de GPT Image 2. Un recurso práctico para aprender prompt engineering y explorar el potencial creativo del modelo GPT Image 2 de OpenAI.",
            "Este repositorio se centra en prompts de imagen de alta fidelidad compartidos en X (Twitter) y por la comunidad. Tanto si buscas capturas de juego fotorrealistas, visuales estilizados o experimentos creativos complejos, aquí encontrarás entradas eficaces para exprimir GPT Image 2.",
        ],
        "why_heading": "## ¿Por qué GPT Image 2?",
        "why_lead": "GPT Image 2 supone una mejora importante frente a la versión 1.5 y ofrece:",
        "why_bullets": [
            "- **Mejor conocimiento del mundo** - representación más precisa de objetos y escenas reales",
            "- **Mejor comprensión del estilo** - reproduce mejor estilos artísticos y estéticas de videojuegos",
            "- **Mayor fidelidad a las instrucciones** - sigue peticiones complejas con más precisión",
            "- **Más fotorrealismo** - genera imágenes que parecen fotos o capturas auténticas",
        ],
        "web_heading": "## [Haz clic aquí para ver la versión web de esta biblioteca de prompts](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)",
        "toc_heading": "## Tabla de contenidos",
        "sections": {
            "photography": ("📷 Fotografía y fotorrealismo", "Prompts para crear escenas ultrarrealistas, rasgos fotográficos creíbles e iluminación compleja."),
            "game": ("🎮 Juegos y entretenimiento", "Prompts para reproducir estéticas de juegos concretas y generar capturas in-game convincentes."),
            "uiux": ("📱 UI / UX y redes sociales", "Prompts para generar interfaces de apps realistas, publicaciones sociales y visuales digitales cuidados."),
            "video": ("🎬 Video, animación y collage", "Prompts para crear escenas con aspecto de video, secuencias animadas y composiciones en collage."),
            "typography": ("📰 Tipografía y diseño de pósteres", "Prompts para probar maquetación tipográfica compleja, alta densidad de información y diseños visuales muy pulidos."),
            "infographics": ("📚 Infografías, educación y documentos", "Prompts para crear tarjetas de conocimiento, materiales educativos, planes de entrenamiento y composiciones densas en información."),
            "character": ("🎭 Personajes y consistencia", "Prompts para probar la consistencia de personajes entre múltiples imágenes y la reproducción de estilo."),
            "image_editing": ("🖼️ Edición de imagen y transferencia de estilo", "Prompts para edición de imagen, transferencia de estilo y generación basada en referencias."),
        },
        "labels": {"prompt": "Prompt", "source": "Fuente", "note": "Nota"},
        "resources_heading": "## 📊 Recursos",
        "resources_official": "### Recursos oficiales",
        "resources_community": "### Comunidad",
        "resources_bullets": [
            "- Comparte tus prompts y resultados en X con #GPTImage2",
            "- Únete a las conversaciones sobre técnicas de prompt engineering",
        ],
        "contributing_heading": "## 🤝 Contribuciones",
        "contributing_intro": "Las contribuciones son bienvenidas. No dudes en enviar una Pull Request.",
        "to_contribute": "**Cómo contribuir:**",
        "contributing_steps": [
            "1. Haz un fork del repositorio",
            "2. Crea tu rama de funcionalidad (`git checkout -b feature/AmazingFeature`)",
            "3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)",
            "4. Haz push a la rama (`git push origin feature/AmazingFeature`)",
            "5. Abre una Pull Request",
        ],
        "guidelines": "**Guía de contribución:**",
        "guideline_bullets": [
            "- Incluye el texto completo del prompt",
            "- Añade el enlace fuente de X / Twitter",
            "- Agrega imágenes de ejemplo cuando sea posible",
            "- Clasifica el contenido correctamente",
        ],
        "ack_heading": "## Agradecimientos",
        "ack_1": "Un agradecimiento especial a la comunidad china de IA por aportar estos casos de prueba tan completos. Los nuevos prompts añadidos en las secciones Typography, Photorealism, UI/UX, Consistency e Image Editing provienen de:",
        "ack_2": "Estos escenarios del mundo real ofrecen información muy valiosa sobre las capacidades de GPT Image 2 en tipografía, generación de escenas realistas, recreación de interfaces, consistencia de personajes y edición de imagen.",
        "ack_3": "Todo el contenido proviene de Internet. Si consideras que algo infringe tus derechos de autor, abre una issue y lo retiraremos.",
        "star_heading": "## Historial de estrellas",
        "license_heading": "## Licencia",
        "license_text": "Este proyecto está publicado bajo la licencia Creative Commons Attribution 4.0 International. Consulta el archivo [LICENSE](LICENSE) para más detalles.",
        "footer": "*Este repositorio está mantenido por la comunidad y no está afiliado a OpenAI.*",
    },
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def split_h2_blocks(lines: list[str]) -> tuple[list[str], list[list[str]]]:
    preamble: list[str] = []
    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in lines:
        if line.startswith("## "):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return preamble, blocks


def block_map(blocks: list[list[str]]) -> dict[str, list[str]]:
    return {block[0].strip(): block for block in blocks}


def extract_content_titles(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    cutoff = text.find("\n## 📊")
    if cutoff != -1:
        text = text[:cutoff]

    h3_titles = re.findall(r"^### (.+)$", text, re.MULTILINE)
    if h3_titles:
        return h3_titles[:CONTENT_H3_COUNT]

    bullet_titles = re.findall(r"^- \*\*(.+?)\*\*", text, re.MULTILINE)
    if bullet_titles:
        return bullet_titles[:CONTENT_H3_COUNT]

    raise ValueError(f"Could not extract titles from {path}")


def git_show_head(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def normalize_label_line(line: str) -> str:
    return line.strip().replace("**", "").replace("*", "")


def extract_labeled_value(line: str, markers: list[str]) -> str | None:
    normalized = normalize_label_line(line)
    for marker in markers:
        match = re.match(rf"^{re.escape(marker)}\s*(?::|：)?\s*(.*)$", normalized)
        if match:
            return match.group(1).strip()
    return None


def split_legacy_blocks(text: str) -> list[tuple[str, list[str]]]:
    lines = text.splitlines()
    blocks: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines
        if current_title is not None:
            blocks.append((current_title, current_lines))
        current_title = None
        current_lines = []

    for line in lines:
        if line.startswith("### "):
            flush()
            current_title = line[4:].strip()
            current_lines = []
            continue

        bullet_match = re.match(r"^- \*\*(.+?)\*\*", line)
        if bullet_match:
            flush()
            current_title = bullet_match.group(1).strip()
            current_lines = []
            continue

        if current_title is not None:
            current_lines.append(line)

    flush()
    return blocks


def parse_legacy_entry(lines: list[str]) -> dict[str, str]:
    markers = {
        "prompt": ["Prompt", "提示词", "提示詞", "プロンプト", "프롬프트"],
        "source": ["Source", "来源", "來源", "出典", "출처", "Quelle", "Fuente"],
        "note": ["Note", "说明", "說明", "メモ", "메모", "Hinweis", "Nota"],
    }
    entry: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        prompt_value = extract_labeled_value(line, markers["prompt"])
        if prompt_value is not None:
            if prompt_value:
                entry["prompt"] = prompt_value
                i += 1
                continue
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("```"):
                i += 2
                prompt_lines: list[str] = []
                while i < len(lines) and lines[i].strip() != "```":
                    prompt_lines.append(lines[i])
                    i += 1
                entry["prompt"] = "\n".join(prompt_lines).strip()
                if i < len(lines):
                    i += 1
                continue

        source_value = extract_labeled_value(line, markers["source"])
        if source_value is not None:
            if source_value:
                entry["source"] = source_value
            i += 1
            continue

        note_value = extract_labeled_value(line, markers["note"])
        if note_value is not None:
            if note_value:
                entry["note"] = note_value
            i += 1
            continue

        i += 1

    return entry


def load_legacy_entries(path: str) -> dict[str, dict[str, str]]:
    text = git_show_head(path)
    entries: dict[str, dict[str, str]] = {}
    for title, block_lines in split_legacy_blocks(text):
        parsed = parse_legacy_entry(block_lines)
        if parsed:
            entries[title] = parsed
    return entries


def replace_labels(line: str, labels: dict[str, str]) -> str:
    line = line.replace("**Prompt:**", f"**{labels['prompt']}:**")
    line = line.replace("**Source:**", f"**{labels['source']}:**")
    line = line.replace("**Note:**", f"**{labels['note']}:**")
    line = line.replace("*Source:", f"*{labels['source']}:")
    line = line.replace("*Note:", f"*{labels['note']}:")
    return line


def build_top(config: dict[str, object], timestamp: str) -> list[str]:
    intro = config["intro"]
    return [
        f"{config['title']}\n",
        "\n",
        f"{config['updated']} {timestamp}\n",
        "\n",
        '<img width="100%" alt="Awesome GPT Image 2 Header Banner" src="assets/banner/readme-header-16x9.png" />\n',
        "\n",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n",
        "[![Stars](https://img.shields.io/github/stars/ZeroLu/awesome-gpt-image?style=flat-square)](https://github.com/ZeroLu/awesome-gpt-image/stargazers)\n",
        "\n",
        LANGUAGE_LINE,
        "\n",
        f"{intro[0]}\n",
        "\n",
        f"{intro[1]}\n",
        "\n",
    ]


def build_why(config: dict[str, object]) -> list[str]:
    out = [f"{config['why_heading']}\n", f"{config['why_lead']}\n"]
    out.extend(f"{line}\n" for line in config["why_bullets"])
    out.append("\n")
    out.append("---\n")
    out.append("\n")
    return out


def build_web_banner(config: dict[str, object]) -> list[str]:
    return [
        f"{config['web_heading']}\n",
        "\n",
        '[<img width="100%" alt="GPT Image Prompt Library Screenshot" src="assets/banner/gpt-image-prompt-library-screenshot.jpg" />](https://cyberbara.com/gpt-image-prompt-library?utm_source=gpt-image-banner)\n',
        "\n",
    ]


def build_toc(config: dict[str, object]) -> list[str]:
    section_names = config["sections"]
    toc_pairs = [
        (section_names["photography"][0], "#-photography--photorealism"),
        (section_names["game"][0], "#-game--entertainment"),
        (section_names["uiux"][0], "#-uiux--social-media"),
        (section_names["video"][0], "#-video-animation--collage"),
        (section_names["typography"][0], "#-typography--poster-design"),
        (section_names["infographics"][0], "#-infographics-education--documents"),
        (section_names["character"][0], "#-character--consistency"),
        (section_names["image_editing"][0], "#-image-editing--style-transfer"),
        (config["resources_heading"].replace("## ", ""), "#-resources"),
        (config["contributing_heading"].replace("## ", ""), "#-contributing"),
    ]
    out = [f"{config['toc_heading']}\n"]
    out.extend(f"- [{label}]({anchor})\n" for label, anchor in toc_pairs)
    out.append("\n")
    out.append("---\n")
    out.append("\n")
    return out


def localize_item_block(
    english_item: list[str],
    localized_title: str,
    labels: dict[str, str],
    legacy_entry: dict[str, str] | None,
) -> list[str]:
    legacy_entry = legacy_entry or {}
    out = [f"### {localized_title}\n"]
    i = 1
    while i < len(english_item):
        line = english_item[i]

        if line.startswith("**Prompt:**"):
            prompt_text = legacy_entry.get("prompt")
            out.append(f"**{labels['prompt']}:**\n")
            if prompt_text and i + 1 < len(english_item) and english_item[i + 1].strip().startswith("```"):
                out.append("```text\n")
                out.append(prompt_text.rstrip() + "\n")
                out.append("```\n")
                i += 2
                while i < len(english_item) and english_item[i].strip() != "```":
                    i += 1
                if i < len(english_item):
                    i += 1
                continue
            i += 1
            continue

        if line.startswith("**Source:**"):
            source_text = legacy_entry.get("source")
            if source_text:
                out.append(f"**{labels['source']}:** {source_text}\n")
            else:
                out.append(replace_labels(line, labels))
            i += 1
            continue

        if line.startswith("**Note:**"):
            note_text = legacy_entry.get("note")
            if note_text:
                out.append(f"**{labels['note']}:** {note_text}\n")
            else:
                out.append(replace_labels(line, labels))
            i += 1
            continue

        if line.startswith("*Source:"):
            source_text = legacy_entry.get("source")
            if source_text:
                out.append(f"*{labels['source']}: {source_text}*\n")
            else:
                out.append(replace_labels(line, labels))
            i += 1
            continue

        if line.startswith("*Note:"):
            note_text = legacy_entry.get("note")
            if note_text:
                out.append(f"*{labels['note']}: {note_text}*\n")
            else:
                out.append(replace_labels(line, labels))
            i += 1
            continue

        out.append(replace_labels(line, labels))
        i += 1

    return out


def localize_content_block(
    english_block: list[str],
    config: dict[str, object],
    section_key: str,
    anchor_id: str,
    localized_titles: list[str],
    offset: int,
    legacy_entries: dict[str, dict[str, str]],
) -> tuple[list[str], int]:
    section_title, section_intro = config["sections"][section_key]
    labels = config["labels"]
    lines = english_block
    first_h3 = next((i for i, line in enumerate(lines) if line.startswith("### ")), len(lines))
    pre_subsection = lines[1:first_h3]
    out = [f'<a id="{anchor_id}"></a>\n', "\n", f"## {section_title}\n", f"{section_intro}\n"]

    non_empty_seen = False
    for line in pre_subsection:
        if not line.strip():
            if non_empty_seen:
                out.append(line)
            continue
        if not non_empty_seen:
            non_empty_seen = True
            out.append("\n")
            continue
        out.append(replace_labels(line, labels))

    titles_used = 0
    item_start_indices = [idx for idx in range(first_h3, len(lines)) if lines[idx].startswith("### ")]
    item_start_indices.append(len(lines))

    for idx in range(len(item_start_indices) - 1):
        start = item_start_indices[idx]
        end = item_start_indices[idx + 1]
        localized_title = localized_titles[offset + titles_used]
        item_lines = lines[start:end]
        out.extend(localize_item_block(item_lines, localized_title, labels, legacy_entries.get(localized_title)))
        titles_used += 1

    return out, titles_used


def build_resources(config: dict[str, object]) -> list[str]:
    out = [
        '<a id="-resources"></a>\n',
        "\n",
        f"{config['resources_heading']}\n",
        "\n",
        f"{config['resources_official']}\n",
        "- [OpenAI GPT Image Documentation](https://platform.openai.com/docs/guides/image-generation)\n",
        "- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/images)\n",
        "\n",
        f"{config['resources_community']}\n",
    ]
    out.extend(f"{line}\n" for line in config["resources_bullets"])
    out.append("\n")
    out.append("---\n")
    out.append("\n")
    return out


def build_contributing(config: dict[str, object]) -> list[str]:
    out = [
        '<a id="-contributing"></a>\n',
        "\n",
        f"{config['contributing_heading']}\n",
        f"{config['contributing_intro']}\n",
        "\n",
        f"{config['to_contribute']}\n",
    ]
    out.extend(f"{line}\n" for line in config["contributing_steps"])
    out.append("\n")
    out.append(f"{config['guidelines']}\n")
    out.extend(f"{line}\n" for line in config["guideline_bullets"])
    out.append("\n")
    out.append("---\n")
    out.append("\n")
    return out


def build_ack(config: dict[str, object]) -> list[str]:
    return [
        f"{config['ack_heading']}\n",
        f"{config['ack_1']}\n",
        "\n",
        "**卡尔的AI沃茨 (Carl's AI Watts)** - [五大真实场景横测GPT-image-2和Nano Banana2](https://mp.weixin.qq.com/s/ASxig6mFVYxrIE8-8Fthew)\n",
        "\n",
        f"{config['ack_2']}\n",
        "\n",
        f"{config['ack_3']}\n",
        "\n",
        "---\n",
        "\n",
    ]


def build_star_history(config: dict[str, object]) -> list[str]:
    return [
        f"{config['star_heading']}\n",
        "[![Star History Chart](https://api.star-history.com/svg?repos=ZeroLu/awesome-gpt-image&type=Date)](https://star-history.com/#ZeroLu/awesome-gpt-image&Date)\n",
        "\n",
        "---\n",
        "\n",
    ]


def build_license(config: dict[str, object]) -> list[str]:
    return [
        f"{config['license_heading']}\n",
        f"{config['license_text']}\n",
        "\n",
        "---\n",
        f"{config['footer']}\n",
    ]


def main() -> None:
    english_lines = read_lines(ENGLISH_README)
    _, english_blocks = split_h2_blocks(english_lines)
    english_block_lookup = block_map(english_blocks)
    timestamp = next(line.strip().replace("Last updated on ", "") for line in english_lines if line.startswith("Last updated on "))

    localized_titles = {
        locale: extract_content_titles(ROOT / cfg["file"])
        for locale, cfg in CONFIG.items()
    }
    legacy_entries = {
        locale: load_legacy_entries(cfg["file"])
        for locale, cfg in CONFIG.items()
    }

    for locale, cfg in CONFIG.items():
        titles = localized_titles[locale]
        if len(titles) != CONTENT_H3_COUNT:
            raise ValueError(f"{locale} has {len(titles)} content titles, expected {CONTENT_H3_COUNT}")

        output: list[str] = []
        output.extend(build_top(cfg, timestamp))
        output.extend(build_why(cfg))
        output.extend(build_web_banner(cfg))
        output.extend(build_toc(cfg))

        title_offset = 0
        for english_heading, section_key, anchor_id in SECTION_KEYS:
            block = english_block_lookup[english_heading]
            localized_block, used = localize_content_block(
                block,
                cfg,
                section_key,
                anchor_id,
                titles,
                title_offset,
                legacy_entries[locale],
            )
            output.extend(localized_block)
            title_offset += used

        if title_offset != CONTENT_H3_COUNT:
            raise ValueError(f"{locale} consumed {title_offset} titles, expected {CONTENT_H3_COUNT}")

        output.extend(build_resources(cfg))
        output.extend(build_contributing(cfg))
        output.extend(build_ack(cfg))
        output.extend(build_star_history(cfg))
        output.extend(build_license(cfg))

        target = ROOT / cfg["file"]
        target.write_text("".join(output), encoding="utf-8")


if __name__ == "__main__":
    main()
