import heapq
class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        root = (nums1[0] + nums2[0], 0, 0)
        q = [root]
        heapq.heapify(q)
        ans = []
        visited = set()

        while q and len(ans) < k:
            sum, i, j = heapq.heappop(q)
            visited.add((sum, i, j))
            ans.append([nums1[i], nums2[j]])

            cand1 = (nums1[i + 1] + nums2[j], i+1, j) if i+1 < len(nums1) else None
            cand2 = (nums1[i] + nums2[j + 1], i, j + 1) if j + 1 < len(nums2) else None

            if cand1 and cand1 not in visited:
                heapq.heappush(q, cand1)
            if cand2 and cand2 not in visited:
                heapq.heappush(q, cand2)
        return ans



print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))