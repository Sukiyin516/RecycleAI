from pathlib import Path
p=Path('RecycleAI_修复版_第一阶段.html')
s=p.read_text(encoding='utf-8').replace("setText('txt-image-upload-hint', u.imageHint);","setText('txt-image-upload-hint', u.imageHint);\n            setText('txt-preset-title', u.presetTitle);\n            setText('progress-text', lang === 'en' ? 'Growth progress' : '成长进度');")
p.write_text(s,encoding='utf-8')
