class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = j = wcount = 0
        m_white = k
        while j < len(blocks):
            if blocks[j] == "W":
                wcount += 1
            if j - i + 1 == k:
                m_white = min(wcount, m_white)
                if blocks[i] == "W":
                    wcount -= 1
                i += 1
            j += 1
        return m_white
            
            



