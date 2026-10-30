from pathlib import Path
p=Path('RecycleAI_修复版_第一阶段.html')
s=p.read_text(encoding='utf-8').replace('支持 JPG、PNG、WEBP 格式；真实图像识别待接入后端。','支持 JPG、PNG、WEBP，最大 8 MB；真实照片将发送至 Google 识别。').replace('支持 JPG、PNG、WEBP；真实图像识别待接入后端。','支持 JPG、PNG、WEBP，最大 8 MB；真实照片将发送至 Google 识别。').replace('Supports JPG, PNG, WEBP; live recognition requires a backend connection.','JPG, PNG, WEBP up to 8 MB; real photos are sent to Google for recognition.').replace('// Phase 2 contract for Codex:', '// Backend contract:')
p.write_text(s,encoding='utf-8')
env=Path('.env')
if not env.exists():
    env.write_text(Path('.env.example').read_text(encoding='utf-8'),encoding='utf-8')
