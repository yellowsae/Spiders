'''
1.5. 叶结点数
【问题描述】
一棵包含有2019个结点的二叉树，最多包含多少个叶结点？
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。


最多叶子结点数就是求其对应的完全二叉树
然后求2019个结点的完全二叉树的叶子结点即可

'''

def most_leaf_nodes(total):

    layer = 0

    while 2 ** layer - 1 < total:
        layer += 1

    now_layer = layer - 1

    now_layer_nodes = 2 ** (layer - 2)

    now_total_nodes = 2 ** (layer - 1) - 1

    left_nodes = total - now_total_nodes

    leaf_nodes = now_layer_nodes - (left_nodes // 2 + left_nodes % 2) + left_nodes

    return leaf_nodes


print(most_leaf_nodes(2019))


