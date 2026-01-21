
def generate_pattern(n):
    # n is the max number (e.g., 6)
    rows = 2 * n + 3  # 0 to 2n+2
    cols = 2 * n + 3  # 0 to 2n+2
    
    for i in range(rows):
        line_str = ""
        for j in range(cols):
            # Logic to determine value
            val = " "
            
            # Borders
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                val = "0"
            
            # Center of the whole grid
            elif i == n + 1 and j == n + 1:
                val = "0"
                
            # Top Left
            elif 1 <= i <= n and 1 <= j <= n:
                if j >= i:
                    val = str(n - j + 1)
            
            # Top Right
            elif 1 <= i <= n and n + 2 <= j <= 2 * n + 1:
                v = (2 * n + 2) - j
                if v <= i:
                     val = str(v)
            
            # Bottom Left
            elif n + 2 <= i <= 2 * n + 1 and 1 <= j <= n:
                r = i - (n + 1)
                if j <= (n - r + 1):
                    val = str(j)
                    
            # Bottom Right
            elif n + 2 <= i <= 2 * n + 1 and n + 2 <= j <= 2 * n + 1:
                r = i - (n + 1)
                k = j - (n + 1)
                if k <= r:
                    val = str(k)
            
            # Append val and a space
            line_str += val + " "
        print(line_str.rstrip())

if __name__ == "__main__":
    generate_pattern(6)
