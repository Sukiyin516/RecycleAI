import json,re
from pathlib import Path
root=Path('.')
p=root/'RecycleAI_修复版_第一阶段.html'
s=p.read_text(encoding='utf-8')
db=json.loads((root/'rules-original.tmp.json').read_text(encoding='utf-8'))
url='https://www.szlh.gov.cn/zmhd/wdzsk/content/post_12679202.html'
# 精确而有限的白名单；说明均为对官方分类事实的概括。
entries=[
('bottle','可回收物','清空且清洁的塑料饮料瓶属于可回收的废塑料。','An empty, clean plastic beverage bottle is recyclable plastic.','清空内容物并保持清洁干燥，投放可回收物收集容器。','Empty the bottle, keep it clean and dry, and use the recyclables container.','One empty clean plastic beverage bottle, clearly plastic; no chemicals, mixed materials or obvious heavy contamination.'),
('can','可回收物','清空且清洁的金属饮料罐属于可回收的废金属。','An empty, clean metal beverage can is recyclable metal.','清空内容物并保持清洁干燥，投放可回收物收集容器。','Empty the can, keep it clean and dry, and use the recyclables container.','One empty clean metal beverage can; not an aerosol or chemical container.'),
('box','可回收物','清洁干燥、未被油污污染的纸箱属于可回收纸类。','Clean, dry cardboard without oil contamination is recyclable paper.','清空纸箱，保持清洁干燥，投放可回收物收集容器。','Empty the box, keep it clean and dry, and use the recyclables container.','One clean dry cardboard box without oil, food or mixed-material coating.'),
('banana','厨余垃圾','香蕉皮是容易腐烂的瓜果皮，属于厨余垃圾。','Banana peel is perishable fruit peel and belongs to food waste.','沥干水分，去除塑料袋等外包装后投放厨余垃圾。','Drain liquids and remove plastic bags or other packaging before placing in food waste.','One banana peel; no packaging or other mixed waste.'),
('tissue','其他垃圾','被污染的纸巾属于其他垃圾，不作为清洁废纸回收。','Contaminated tissue belongs to residual waste rather than clean recyclable paper.','收拢以免散落，投放其他垃圾；医疗废物不在此规则范围内。','Contain it to prevent scattering and use residual waste; medical waste is outside this rule.','One clearly used contaminated household tissue, not medical waste or an unidentified wet wipe.'),
('alkaline','其他垃圾','已确认无汞的普通碱性干电池通常按其他垃圾处理，不能推广到所有电池。','Confirmed mercury-free ordinary alkaline dry cells are usually residual waste; this does not apply to all batteries.','仅适用于确认无汞的普通碱性干电池；类型不明、充电或破损电池请向投放管理人核实。','Only for confirmed mercury-free ordinary alkaline dry cells. Ask the sorting manager about unknown, rechargeable or damaged batteries.','One intact ordinary non-rechargeable alkaline dry cell with clearly readable alkaline and mercury-free labels; never infer chemistry from shape.')]
rules={}
for k,cat,reason,enreason,guide,enguide,condition in entries:
    rules[k]=dict(category=cat,reason=reason,enReason=enreason,disposalGuide=guide,enDisposalGuide=enguide,matchCondition=condition,matchedKey=k if k!='alkaline' else None,sourceUrl=url,reviewedAt='2026-10-29')
    if k in db:
        db[k].update(reason=reason,enReason=enreason,guide=guide,enGuide=enguide,ruleVerified=True,sourceUrl=url)
        quiz=db[k]['quiz']; quiz['id'] += '_reviewed_v2'
        if k in ('bottle','can','box'):
            quiz.update(question='这件清洁的可回收物投放前，应该怎样处理？',enQuestion='How should this clean recyclable item be prepared?',options=[dict(text='A. 清空内容物，保持清洁干燥',enText='A. Empty contents and keep clean and dry',isCorrect=True),dict(text='B. 混入食物残渣',enText='B. Mix with food scraps',isCorrect=False),dict(text='C. 投入厨余垃圾',enText='C. Put into food waste',isCorrect=False)],explanation='深圳罗湖官方说明要求可回收物清空内容物，并保持清洁干燥。',enExplanation='Official Luohu guidance asks for recyclable items to be emptied and kept clean and dry.')
        elif k=='banana':
            quiz.update(explanation='深圳罗湖官方说明：厨余垃圾投放前沥干水分，并去除塑料袋等外包装。',enExplanation='Official Luohu guidance asks for food waste to be drained and removed from plastic packaging.')
        else:
            quiz.update(question='被污染的生活用纸巾属于哪一类？',enQuestion='Which category covers contaminated household tissues?',options=[dict(text='A. 其他垃圾',enText='A. Residual waste',isCorrect=True),dict(text='B. 可回收物',enText='B. Recyclables',isCorrect=False),dict(text='C. 厨余垃圾',enText='C. Food waste',isCorrect=False)],explanation='深圳罗湖官方说明将被污染的纸巾列入其他垃圾。',enExplanation='Official Luohu guidance lists contaminated tissues as residual waste.')
        quiz.update(sourceUrl=url,verified=True)
db['banana'].update(name='香蕉皮',enName='Banana Peel')
db['tissue'].update(name='被污染的生活用纸巾',enName='Contaminated Household Tissue')
db['battery'].update(category='暂时无法确定',enCategory='Uncertain',reason='待核实：本项目尚未核实铅蓄电池的具体投放渠道。不同电池不能统一分类。',enReason='Unverified: this project has not reviewed the specific lead-acid battery collection route. Battery types differ.',guide='不要拆解或随意投放。请向当地投放管理人或合规回收渠道确认。普通无汞碱性干电池通常属于其他垃圾，不能套用到铅蓄电池。',enGuide='Do not dismantle or discard indiscriminately. Confirm with a sorting manager or approved collector. Ordinary mercury-free alkaline cells usually belong to residual waste; this does not apply to lead-acid batteries.',quiz=None,ruleVerified=False,badgeClass='bg-amber-100 text-amber-800 border-amber-200',cardClass='bg-amber-50/70 border-amber-200',icon='❓')
s=re.sub(r'const SHENZHEN_RULES_DB = \{[\s\S]*?\n        \};','const SHENZHEN_RULES_DB = '+json.dumps(db,ensure_ascii=False,indent=4)+';',s,count=1)
s=s.replace('本地演示样例（不调用 AI，分类待核实）：','本地演示（不调用 AI；电池案例待核实）：').replace('Local demo samples (no AI used; rules require review):','Local demos (no AI; battery example unverified):')
s=s.replace('学习原型：示例规则待核对；真实图像识别接口尚未接入','课程 Demo：Gemini 识别物品，已核实规则分类；未覆盖物品返回暂时无法确定').replace('Learning prototype: example rules require review; real image recognition is not connected yet','Course demo: Gemini identifies items; reviewed rules classify them. Uncovered items remain uncertain.')
s=s.replace('当前版本仅支持本地样例；真实照片识别需要在下一阶段接入安全的后端接口。','本地演示无需密钥。真实照片经 Python 后端调用 Gemini；请在 .env 配置密钥并重启。图片将发送至 Google 处理。').replace('This version supports local samples only. Real photo recognition will require a secure backend endpoint.','Demos need no key. Real photos go through Python to Gemini. Configure .env and restart. Photos are sent to Google for processing.')
s=s.replace('本地版尚未接入真实 AI 识别；请使用“本地演示样例”体验流程，后续可连接后端。','无法连接后端。请运行 start.bat，并从 http://127.0.0.1:5000 打开网页。').replace('Real AI image recognition is not connected in this local version. Try the local demo samples, then connect a backend later.','Backend unavailable. Run start.bat and open http://127.0.0.1:5000.')
s=s.replace("showToast(UI_EXTRA[STATE.currentLang][error.message === 'BACKEND_UNAVAILABLE' ? 'apiOffline' : 'apiError'], 'error');","showToast((STATE.currentLang === 'en' ? error.enMessage : error.userMessage) || UI_EXTRA[STATE.currentLang][error.message === 'BACKEND_UNAVAILABLE' ? 'apiOffline' : 'apiError'], 'error');")
s=s.replace("throw new Error('CLASSIFICATION_FAILED');\n            }\n            const parsed", "const payload = await response.json().catch(() => ({}));\n                const error = new Error('CLASSIFICATION_FAILED');\n                error.userMessage = payload.error?.message;\n                error.enMessage = payload.error?.enMessage;\n                throw error;\n            }\n            const parsed",1)
s=s.replace("if (parsed.matchedKey && SHENZHEN_RULES_DB[parsed.matchedKey])", "if (parsed.ruleVerified === true && parsed.matchedKey && SHENZHEN_RULES_DB[parsed.matchedKey]?.ruleVerified)")
s=s.replace("return { ...rule, name: parsed.itemName, enName: parsed.enItemName || rule.enName };", "return { ...rule, name: parsed.itemName, enName: parsed.enItemName || rule.enName, reason: parsed.reason, enReason: parsed.enReason, guide: parsed.disposalGuide, enGuide: parsed.enDisposalGuide };")
s=s.replace("QUIZ_EN_OPTIONS[quiz.id]?.[idx] || opt.enText || opt.text", "opt.enText || QUIZ_EN_OPTIONS[quiz.id.replace('_reviewed_v2', '')]?.[idx] || opt.text")
s=s.replace("res.source === 'demo' ? 'statusDemo' : 'statusAI'", "res.source === 'demo' ? 'statusDemo' : 'statusAI'")
s=s.replace("document.getElementById('txt-verified-tag').textContent = UI_EXTRA[STATE.currentLang][res.source === 'demo' ? 'statusDemo' : 'statusAI'];", "document.getElementById('txt-verified-tag').textContent = UI_EXTRA[STATE.currentLang][res.source === 'demo' ? 'statusDemo' : 'statusAI'] + (res.category === '暂时无法确定' ? (isEn ? ' · Rule unverified / uncertain' : ' · 规则待核实 / 暂时无法确定') : '');")
# 在原有页脚添加简短来源，不改变页面结构。
s=s.replace('</footer>','''<p class="text-xs text-slate-500 text-center px-4 pb-4"><a href="'''+url+'''" target="_blank" rel="noopener noreferrer">规则来源 / Rules: 深圳罗湖官方分类说明</a> · 2026-10-29 核对 / reviewed<br>未覆盖规则不推测；真实照片发送至 Google，本项目不保存照片。<br>Uncovered rules remain uncertain. Real photos are sent to Google; this app does not save photos.</p></footer>''',1)
p.write_text(s,encoding='utf-8')
(root/'rules.json').write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'rules-original.tmp.json').unlink()
