class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Nếu độ dài lẻ, chắc chắn không thể khớp cặp
        if len(s) % 2 != 0:
            return False
            
        # 2. Dùng dict để ánh xạ ngoặc đóng -> ngoặc mở tương ứng
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            # Nếu là ngoặc đóng
            if char in mapping:
                # Lấy phần tử trên cùng của stack (nếu stack rỗng thì gán bằng ký tự dummy '#')
                top_element = stack.pop() if stack else '#'
                
                # Nếu ngoặc mở không khớp với ngoặc đóng hiện tại -> Sai luôn
                if mapping[char] != top_element:
                    return False
            else:
                # Nếu là ngoặc mở, chỉ cần đẩy vào stack
                stack.append(char)
                
        # 3. Nếu stack rỗng tức là mọi ngoặc đều được đóng khớp -> True
        return not stack