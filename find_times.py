from pathlib import Path
text = Path(r'c:\Users\HP\Downloads\INVITACION\Muestra Azure - Invitali.html').read_text('utf-8', errors='replace')
for term in ['16:00 h', '18:00 h', 'Ceremonia Religiosa', 'Recepción Social']:
    idx = text.find(term)
    print(term, idx)
    if idx != -1:
        print(text[max(0, idx-120):idx+120])
        print('---')
