import unittest
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def max_path_sum(self, root):
        paths_starting_from_root = []
        Solution.fill_paths_starting_from_node(root,paths_starting_from_root)
        valid_combinations_of_paths_starting_from_root = Solution.get_paths_valid_combinations_starting_from_node(root,paths_starting_from_root) 
        max_path_sum = 0
        for path in valid_combinations_of_paths_starting_from_root:
            path_sum = Solution.get_path_sum_in_partition_with_max_sum(path)
            if (path_sum>max_path_sum):
              max_path_sum = path_sum
        return max_path_sum

    @staticmethod
    def fill_paths_starting_from_node(node,all_paths, path = [], is_root = True,comming_from_left = False):        
        if (node == None):
            if(comming_from_left):
              all_paths.append(path)
            return
        if not is_root:
            path.append(node)
        left_copy =  [node for node in path]
        right_copy = [node for node in path]        
        Solution.fill_paths_starting_from_node(node.left,all_paths,left_copy, False,True)
        Solution.fill_paths_starting_from_node(node.right,all_paths,right_copy,False)

    @staticmethod
    def get_path_sum_in_partition_with_max_sum(path):
        path_len = len(path)
        max_sum = 0
        for i in range(path_len):
            for j in range(i+1,path_len):
                path_copy = path[i:j+1]
                numeric_copy = [node.val for node in path_copy]
                sub_path_sum = sum(numeric_copy)
                if sub_path_sum>max_sum:
                    max_sum = sub_path_sum
        return max_sum

    @staticmethod
    def get_paths_valid_combinations_starting_from_node(node, paths):
        paths_len = len(paths)
        combinations = []
        replaced_node = node
        for i in range(paths_len):
            for j in range(i+1,paths_len):
                first_part_len = len(paths[i])
                second_part_len = len(paths[j])
                first_part_copy = [node for node in paths[i]]
                second_part_copy = [node for node in paths[j]]
                smaller_part_len = min(first_part_len,second_part_len)
                part_one_reversed = []
                for k in range(smaller_part_len):
                  if(first_part_copy[0] == second_part_copy[0]):  
                     replaced_node = first_part_copy.pop(0)
                     second_part_copy.pop(0) 
                first_part_len = len(first_part_copy)
                for k in range(first_part_len-1,-1,-1):
                    part_one_reversed.append(first_part_copy[k])
                combined_path = part_one_reversed+[replaced_node]+second_part_copy
                combinations.append(combined_path)
        return combinations

class TestBinaryTreeMaxPathSum(unittest.TestCase):
    def setUp(self):
        left2 = TreeNode(val=2)
        right3 = TreeNode(val=3)
        self.test_node_three_element = TreeNode(val=1,left=left2,right=right3)
        left9 = TreeNode(val=9)
        left15 = TreeNode(val=15)
        right7 = TreeNode(val=7)
        right20 = TreeNode(val=20, left=left15,right=right7)
        self.test_node_five_element = TreeNode(val=-10,left=left9,right= right20)   
    
    def test_soluion(self):
      solution = Solution()
      self.assertEqual(solution.max_path_sum(self.test_node_three_element),6)
      self.assertEqual(solution.max_path_sum(self.test_node_five_element),42)

if __name__ == "__main__":
  unittest.main(argv=[''],verbosity=2,exit=False)
