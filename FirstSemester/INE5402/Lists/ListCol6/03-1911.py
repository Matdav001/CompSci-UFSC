while True:
    n = int(input())
    if n == 0:
        break
        
    students = {}
    for _ in range(n):
        parts = input().split()
        students[parts[0]] = parts[1]
        
    m = int(input())
    
    daily_signatures = {}
    for _ in range(m):
        parts = input().split()
        daily_signatures[parts[0]] = parts[1]
        
    false_count = 0
    
    for name, today_sig in daily_signatures.items():
        original_sig = students[name]
        
        diffs = 0
        len_orig = len(original_sig)
        len_sign = len(today_sig)
        max_len = max(len_orig, len_sign)
        
        for i in range(max_len):
            if i >= len_orig or i >= len_sign or original_sig[i] != today_sig[i]:
                diffs += 1
        
        if diffs > 1:
            false_count += 1
            
    print(false_count)

