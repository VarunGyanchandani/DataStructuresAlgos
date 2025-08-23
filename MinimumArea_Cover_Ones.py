from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        INF = 10**9
        ans = INF

        # Precompute area for row ranges [l, r)
        area_row = [[0] * (n + 1) for _ in range(n)]
        for l in range(n):
            min_c = m
            max_c = -1
            min_rr = n
            max_rr = -1
            has_one = False
            for r in range(l, n):
                row_has_one = False
                for c in range(m):
                    if grid[r][c]:
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
                        row_has_one = True
                if row_has_one:
                    min_rr = min(min_rr, r)
                    max_rr = max(max_rr, r)
                    has_one = True
                if has_one:
                    height = max_rr - min_rr + 1
                    width = max_c - min_c + 1 if min_c <= max_c else 0
                    area_row[l][r + 1] = height * width

        # Precompute area for col ranges [s, t)
        area_col = [[0] * (m + 1) for _ in range(m)]
        for s in range(m):
            min_r = n
            max_r = -1
            min_cc = m
            max_cc = -1
            has_one = False
            for t in range(s, m):
                col_has_one = False
                for rr in range(n):
                    if grid[rr][t]:
                        min_r = min(min_r, rr)
                        max_r = max(max_r, rr)
                        col_has_one = True
                if col_has_one:
                    min_cc = min(min_cc, t)
                    max_cc = max(max_cc, t)
                    has_one = True
                if has_one:
                    height = max_r - min_r + 1 if min_r <= max_r else 0
                    width = max_cc - min_cc + 1
                    area_col[s][t + 1] = height * width

        def get_area(row_l: int, row_r: int, col_l: int, col_r: int) -> int:
            min_c = m
            max_c = -1
            min_rr = n
            max_rr = -1
            for rr in range(row_l, row_r):
                for cc in range(col_l, col_r):
                    if grid[rr][cc]:
                        min_c = min(min_c, cc)
                        max_c = max(max_c, cc)
                        min_rr = min(min_rr, rr)
                        max_rr = max(max_rr, rr)
            if min_c > max_c or min_rr > max_rr:
                return 0
            return (max_rr - min_rr + 1) * (max_c - min_c + 1)

        # Case 1: Divide into 3 horizontal strips
        for p in range(1, n):
            for q in range(p + 1, n):
                a1 = area_row[0][p]
                a2 = area_row[p][q]
                a3 = area_row[q][n]
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Case 2: Divide into 3 vertical strips
        for p in range(1, m):
            for q in range(p + 1, m):
                a1 = area_col[0][p]
                a2 = area_col[p][q]
                a3 = area_col[q][m]
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Case 3: Divide rows into 2 parts, one with 1 rect, one with 2 rects
        for p in range(1, n + 1):
            # Top with 1, bottom with 2
            a_top = area_row[0][p]
            if a_top == 0:
                continue
            bottom_l, bottom_r = p, n
            if bottom_l >= bottom_r:
                continue
            min_bottom = INF
            # 3.1: Divide bottom horizontally into 2
            for mid in range(bottom_l + 1, bottom_r):
                a_up = area_row[bottom_l][mid]
                a_down = area_row[mid][bottom_r]
                if a_up > 0 and a_down > 0:
                    min_bottom = min(min_bottom, a_up + a_down)
            # 3.2: Divide bottom vertically into 2
            for mid_c in range(1, m):
                a_left = get_area(bottom_l, bottom_r, 0, mid_c)
                a_right = get_area(bottom_l, bottom_r, mid_c, m)
                if a_left > 0 and a_right > 0:
                    min_bottom = min(min_bottom, a_left + a_right)
            if min_bottom < INF:
                ans = min(ans, a_top + min_bottom)

            # Bottom with 1, top with 2
            a_bottom = area_row[p][n]
            if a_bottom == 0:
                continue
            top_l, top_r = 0, p
            if top_l >= top_r:
                continue
            min_top = INF
            # 3.1: Divide top horizontally into 2
            for mid in range(top_l + 1, top_r):
                a_up = area_row[top_l][mid]
                a_down = area_row[mid][top_r]
                if a_up > 0 and a_down > 0:
                    min_top = min(min_top, a_up + a_down)
            # 3.2: Divide top vertically into 2
            for mid_c in range(1, m):
                a_left = get_area(top_l, top_r, 0, mid_c)
                a_right = get_area(top_l, top_r, mid_c, m)
                if a_left > 0 and a_right > 0:
                    min_top = min(min_top, a_left + a_right)
            if min_top < INF:
                ans = min(ans, min_top + a_bottom)

        # Case 4: Divide cols into 2 parts, one with 1 rect, one with 2 rects
        for p in range(1, m + 1):
            # Left with 1, right with 2
            a_left = area_col[0][p]
            if a_left == 0:
                continue
            right_l, right_r = p, m
            if right_l >= right_r:
                continue
            min_right = INF
            # 4.1: Divide right horizontally into 2
            for mid in range(1, n):
                a_up = get_area(0, mid, right_l, right_r)
                a_down = get_area(mid, n, right_l, right_r)
                if a_up > 0 and a_down > 0:
                    min_right = min(min_right, a_up + a_down)
            # 4.2: Divide right vertically into 2
            for mid_c in range(right_l + 1, right_r):
                a_lft = get_area(0, n, right_l, mid_c)
                a_rgt = get_area(0, n, mid_c, right_r)
                if a_lft > 0 and a_rgt > 0:
                    min_right = min(min_right, a_lft + a_rgt)
            if min_right < INF:
                ans = min(ans, a_left + min_right)

            # Right with 1, left with 2
            a_right = area_col[p][m]
            if a_right == 0:
                continue
            left_l, left_r = 0, p
            if left_l >= left_r:
                continue
            min_left = INF
            # 4.1: Divide left horizontally into 2
            for mid in range(1, n):
                a_up = get_area(0, mid, left_l, left_r)
                a_down = get_area(mid, n, left_l, left_r)
                if a_up > 0 and a_down > 0:
                    min_left = min(min_left, a_up + a_down)
            # 4.2: Divide left vertically into 2
            for mid_c in range(left_l + 1, left_r):
                a_lft = get_area(0, n, left_l, mid_c)
                a_rgt = get_area(0, n, mid_c, left_r)
                if a_lft > 0 and a_rgt > 0:
                    min_left = min(min_left, a_lft + a_rgt)
            if min_left < INF:
                ans = min(ans, min_left + a_right)

        return ans


sol = Solution()

# Sample 2D grid
grid = [
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

result = sol.minimumSum(grid)

print("Minimum total area of 3 rectangles covering all 1s:", result)

grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

result = sol.minimumSum(grid)

print("Minimum total area of 3 rectangles covering all 1s:", result)