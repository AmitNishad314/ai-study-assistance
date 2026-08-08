
def chunk_text(text,chunk_size=1000,chunk_overlap=200):
    
    chunks=[]
    start=0
    text_len = len(text)
    
    while start < text_len:
        end = min(start + chunk_size, text_len)
        
        if(end<text_len):
            last_space = text.rfind(" ", start, end)
            if(last_space>start):
                end = last_space
        
        chunk = text[start:end].strip()
        
        if chunk:
            chunks.append(chunk)
        
        if end>= text_len:
            break
        
        start = max(end - chunk_overlap, start+1)
        
    return chunks