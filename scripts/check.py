from pathlib import Path
from html.parser import HTMLParser
import json
root=Path(__file__).resolve().parents[1]
base='/pixelyn-site/'
class Page(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for key in ['href','src']:
   v=a.get(key,'')
   if v.startswith(base):
    target=root/v[len(base):].split('#')[0]
    if v.endswith('/') or target.is_dir(): target=target/'index.html'
    assert target.is_file(), (self.file,v)
  assert not (tag=='script' or tag=='iframe'),self.file
for file in root.rglob('*.html'):
 p=Page();p.file=file;p.feed(file.read_text())
for lang,paras in json.loads((root/'scripts/privacy-source.json').read_text()).items():
 for path in ['', 'privacy/', 'support/']:
  html=(root/lang/path/'index.html').read_text()
  assert 'lang="'+('zh-Hans' if lang=='zh' else 'en')+'"' in html
  other='en' if lang=='zh' else 'zh'
  assert base+other+'/'+path in html
 for para in paras: assert para in (root/lang/'privacy/index.html').read_text()
print('PASS: 7 published routes, bilingual links, local assets, exact app privacy paragraphs, no scripts or trackers')
