# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
큰 수 부터 탐색하는 방법

DFS(root.right)
DFS(root.left)

Point: cur_sum을 인스턴스 변수로 선언하여 새로운 노드에 방문할 때 마다 root.val 값을 더해주어 업데이트한다.
'''
class Solution:
    def bstToGst(self, root: TreeNode):
        self.cur_sum = 0
        def DFS(self, root: TreeNode):
            if root.right:
                DFS(self, root.right)
            self.cur_sum += root.val
            root.val = self.cur_sum
            if root.left:
                DFS(self, root.left)
        
        if root.right:
            DFS(self, root.right)
        self.cur_sum += root.val
        root.val = self.cur_sum
        if root.left:
            DFS(self, root.left)
        return root
