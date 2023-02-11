# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
depth가 가장 큰 노드를 판별.
노드 탐색을 하면서 가장 깊은 노드인지 알 수 없으므로 해시테이블 생성
'''
from collections import defaultdict
class Solution:
    def __init__(self):
        self.my_dict = defaultdict(int)
    # my_dict = defaultdict(int)
        
    def DFS(self, root: Optional[TreeNode], depth) -> int:
        if root.left == None and root.right == None:
            self.my_dict[depth] += root.val
        else:
            if root.left:
                self.DFS(root.left, depth+1)
            if root.right:
                self.DFS(root.right, depth+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        else:
            if root.left:
                self.DFS(root.left, 2)
            if root.right:
                self.DFS(root.right, 2)
        li = sorted(self.my_dict.keys())
        answer = self.my_dict[li[-1]]
        return answer
