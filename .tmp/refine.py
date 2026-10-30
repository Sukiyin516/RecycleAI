from pathlib import Path
p=Path('RecycleAI_修复版_第一阶段.html')
s=p.read_text(encoding='utf-8')
s=s.replace('function processFile(file) {','function processFile(file) {\n            resetImage();')
s=s.replace('reader.readAsDataURL(file);',"reader.onerror = () => { resetImage(); showToast(UI_EXTRA[STATE.currentLang].imageInvalid, 'error'); };\n            reader.readAsDataURL(file);")
s=s.replace('async function startAIClassification() {\n            if (!STATE.currentImageBase64) return;', 'async function startAIClassification() {\n            if (!STATE.currentImageBase64 || STATE.classifying) return;\n            STATE.classifying = true;')
s=s.replace("} finally {\n                document.getElementById('sec-loading')", "} finally {\n                STATE.classifying = false;\n                document.getElementById('sec-loading')")
s=s.replace('toast.innerHTML = `<i class="fa-solid fa-circle-info"></i><span>${message}</span>`;', "const icon = document.createElement('i');\n            icon.className = 'fa-solid fa-circle-info';\n            const label = document.createElement('span');\n            label.textContent = message;\n            toast.append(icon, label);")
p.write_text(s,encoding='utf-8')
