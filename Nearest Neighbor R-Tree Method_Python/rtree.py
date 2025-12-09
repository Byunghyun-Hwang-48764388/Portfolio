import sys
import math
import time

#maximum capacity of the node, after this the node will overflow
B = 4

#define node class
class Node(object): 
    def __init__(self):
        self.child_nodes = []  # for non-leaf node, a list to store nodes
        self.data_points = []  # for leaf node, a list to store data points
        self.parent = None
        self.MBR = {
            'x1': -1,
            'y1': -1,
            'x2': -1,
            'y2': -1,
        }

    def perimeter(self):
        # compute the size of MBRs
        # if points location is negative, return 0
        if self.MBR['x1'] < 0 or self.MBR['y1'] < 0 or self.MBR['x2'] < 0 or self.MBR['y2'] < 0:
            return 0
        width = self.MBR['x2'] - self.MBR['x1']
        height = self.MBR['y2'] - self.MBR['y1']
        return 2 * (width + height)  # perimeter of the MBR

    def is_overflow(self):
        if self.is_leaf():
            if len(self.data_points) > B: # checking overflows of data points, B is the upper bound.
                return True
            else:
                return False
        else:
            if len(self.child_nodes) > B: # checking overflows of child nodes, B is the upper bound.
                return True
            else:
                return False
            
    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        if len(self.child_nodes) == 0:
            return True
        else:
            return False
        

#Definition of the Rtree classes

class RTree(object): # R tree class
    def __init__(self):
        self.root = Node() # create a root

    def insert(self, node, point): # insert p(data point) to u (MBR)
        if node.is_leaf(): 
            self.add_data_point(node, point) # add the data point and update the corresponding MBR
            if node.is_overflow():
                self.handle_overflow(node) # handle overflow for leaf nodes
        else:
            sub_node = self.choose_subtree(node, point) # choose a subtree to insert the data point to miminize the perimeter sum
            self.insert(sub_node, point) # keep continue to check the next layer recursively
            self.update_mbr(sub_node) # update the MBR for inserting the data point
        
    def add_data_point(self, node, data_point): # add data points and update the the MBRS
        # 1. add the point into node.data_points
        node.data_points.append(data_point)
        # 2. update node.MBR
        self.update_mbr(node)
        
    def add_child(self, node, child):
        # 1. add the child into node.child_nodes
        node.child_nodes.append(child)
        # 2. set the node as the parent of the child
        child.parent = node
        # 3. update node.MBR
        if node.MBR['x1'] < 0 or child.MBR['x1'] < node.MBR['x1']:
            node.MBR['x1'] = child.MBR['x1']
        if node.MBR['y1'] < 0 or child.MBR['y1'] < node.MBR['y1']:
            node.MBR['y1'] = child.MBR['y1']
        if node.MBR['x2'] < 0 or child.MBR['x2'] > node.MBR['x2']:
            node.MBR['x2'] = child.MBR['x2']
        if node.MBR['y2'] < 0 or child.MBR['y2'] > node.MBR['y2']:
            node.MBR['y2'] = child.MBR['y2']

    # return the child whose MBR requires the minimum increase in perimeter to cover p

    def handle_overflow(self, node):
        node1, node2 = self.split(node) # u1 u2 are the two splits returned by the function "split"
        # if u is root, create a new root with s1 and s2 as its' children
        if node.is_root():
            new_root = Node()
            self.add_child(new_root, node1)
            self.add_child(new_root, node2)
            self.root = new_root
            self.update_mbr(new_root)
        # if u is not root, delete u, and set s1 and s2 as u's parent's new children
        else:
            parent = node.parent
            # copy the information of s1 into u
            parent.child_nodes.remove(node)
            self.add_child(parent, node1) # link the two splits and update the corresponding MBR
            self.add_child(parent, node2)
            if parent.is_overflow(): # check the parent node recursively
                self.handle_overflow(parent)

    def choose_subtree(self, node, point): 
        if node.is_leaf(): # find the leaf and insert the data point
            return node
        else:
            min_increase = sys.maxsize # set an initial value
            best_child = None
            for child in node.child_nodes: # check each child to find the best node to insert the point 
                if min_increase > self.peri_increase(child, point):
                    min_increase = self.peri_increase(child, point)
                    best_child = child
            return best_child
        
    def peri_increase(self, node, p): # calculate the increase of the perimeter after inserting the new data point
        # new perimeter - original perimeter = increase of perimeter
        pre_perimeter = node.perimeter()

        x1_new = min(node.MBR['x1'], p[0]) if node.MBR['x1'] >= 0 else p[0]
        y1_new = min(node.MBR['y1'], p[1]) if node.MBR['y1'] >= 0 else p[1]
        x2_new = max(node.MBR['x2'], p[0]) if node.MBR['x2'] >= 0 else p[0]
        y2_new = max(node.MBR['y2'], p[1]) if node.MBR['y2'] >= 0 else p[1]

        new_perimeter = 2 * ((x2_new - x1_new) + (y2_new - y1_new))

        return new_perimeter - pre_perimeter # perimeter incresement
    
    def split(self, node): # split a node into two nodes 
        # split u into s1 and s2
        best_s1 = Node()
        best_s2 = Node()

        # u is a leaf node
        if node.is_leaf():
            points = node.data_points
            points.sort(key=lambda p: p[0])  
            middle = len(points) // 2
            best_s1.data_points = points[:middle]
            best_s2.data_points = points[middle:]
            self.update_mbr(best_s1)
            self.update_mbr(best_s2)

        # u is a internal node
        else:
            child = node.child_nodes
            child.sort(key=lambda c: c.MBR['x1'])
            middle = len(child) // 2
            best_s1.child_nodes = child[:middle]
            best_s2.child_nodes = child[middle:]
            for child in best_s1.child_nodes:
                child.parent = best_s1
            for child in best_s2.child_nodes:
                child.parent = best_s2
            self.update_mbr(best_s1)
            self.update_mbr(best_s2)

        return best_s1, best_s2

    #I ensure accurate bounding rectangles for BBS skyline calculations.
    def update_mbr(self, node): # update MBRs when forming a new MBR. It is used in checking the combinations and update the root
        if node.is_leaf(): # compare points in the node
            if not node.data_points:
                # does not have data points, so default is no MBR (negative value,-1)
                node.MBR = {'x1': -1, 'y1': -1, 'x2': -1, 'y2': -1}
                return
            x_list = [p[0] for p in node.data_points]
            y_list = [p[1] for p in node.data_points]
            new_mbr = {
                'x1': min(x_list),
                'y1': min(y_list),
                'x2': max(x_list),
                'y2': max(y_list),
            }
        else:  # compare MBR values of node's childs
            if not node.child_nodes:
                node.MBR = {'x1': -1, 'y1': -1, 'x2': -1, 'y2': -1}
                return
            child_x1 = [child.MBR['x1'] for child in node.child_nodes]
            child_y1 = [child.MBR['y1'] for child in node.child_nodes]
            child_x2 = [child.MBR['x2'] for child in node.child_nodes]
            child_y2 = [child.MBR['y2'] for child in node.child_nodes]
            new_mbr = {
                'x1': min(child_x1),
                'y1': min(child_y1),
                'x2': max(child_x2),
                'y2': max(child_y2),
            }

        # update MBR
        node.MBR = new_mbr