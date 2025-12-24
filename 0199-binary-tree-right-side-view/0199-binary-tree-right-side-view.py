# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        self.total = 0
        def num(node):
            if root:
                self.total += 1
                if node.left:
                    num(node.left)
                if node.right:
                    num(node.right)
            return
        num(root)
        self.total += 10
        arr = [0] * self.total
        nodeArr = deque()
        result = []
        if root:
            nodeArr.append(root)
        else:
            return result
        valArr = []
        length = -1

        def bfs(node, stage):
            arr[stage] += 1
            if node:
                if node.left:
                    bfs(node.left, stage + 1)
                if node.right:
                    bfs(node.right, stage + 1)
            return

        while nodeArr:
            nodes = nodeArr.popleft()
            valArr.append(nodes.val)
            
            if nodes.left:
                nodeArr.append(nodes.left)
            if nodes.right:
                nodeArr.append(nodes.right)

        bfs(root, 0)

        print(arr)
        print("****")
        print(valArr)
        i = 0
        st = arr[i]

        while st is not 0:
            length += st
            result.append(valArr[length])
            i += 1
            st = arr[i]
        
        return result

############

        # def rightSideView(self, root):
        # self.total = 0
        # def num(node):
        #     if root:
        #         self.total += 1
        #         if node.left:
        #             num(node.left)
        #         if node.right:
        #             num(node.right)
        #     return
        # num(root)
        # self.total += 10
        # arr = [0] * self.total
        # nodeArr = deque()
        # if root:
        #     nodeArr.append(root)
        # valArr = []
        # length = -1

        # def bfs(node, stage):
        #     arr[stage] += 1
        #     if node:
        #         if node.left:
        #             bfs(node.left, stage + 1)
        #         if node.right:
        #             bfs(node.right, stage + 1)
        #     return

        # while nodeArr:
        #     nodes = nodeArr.popleft()
        #     valArr.append(nodes.val)
            
        #     if nodes.left:
        #         nodeArr.append(nodes.left)
        #     if nodes.right:
        #         nodeArr.append(nodes.right)

        # bfs(root, 0)

        # print(arr)
        # print("****")
        # print(valArr)
        # i = 0
        # st = arr[i]
        # result = []

        # while st is not 0:
        #     length += st
        #     result.append(valArr[length])
        #     i += 1
        #     st = arr[i]

        # return result
######

        # output = []
        # if not root:
        #     return output
        # arr = deque([root])
        # output = []
        # spnode = root
        # self.prev = None
        # node = None
    
        # while arr:
        #     if node:
        #         self.prev = node
        #     node = arr.popleft()
        #     if spnode == node:
        #         if node.left:
        #             spnode = node.left
        #         elif node.right:
        #             spnode = node.right
        #         if self.prev and spnode != node:
        #             output.append(self.prev.val)

        #     if node.left:
        #         arr.append(node.left)
        #     if node.right:
        #         arr.append(node.right)
        # return output

        # arr = deque([root])
        # printval = []
        # while arr:
        #     node = arr.popleft()
        #     if node:
        #         printval.append(node.val)
        #     else:
        #         printval.append(None)

        # print(printval)
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        