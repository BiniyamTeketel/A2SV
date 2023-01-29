class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(a, b, c, d, e, f, g, h, i):
            return (sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and
                    (a + b + c == d + e + f == g + h + i == a + d + g ==
                    b + e + h == c + f + i == a + e + i == c + e + g == 15))
        
        R, C = len(grid), len(grid[0])
        fuck = 0
        for r in range(R-2):
            for c in range(C-2):
                if is_magic(grid[r][c], grid[r][c + 1], grid[r][c + 2],
                            grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                            grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]):
                    fuck += 1
        return fuck
