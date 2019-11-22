package com.company;

class Nod {

    Integer data;
    Nod left;
    Nod right;

    Nod(int givenData) {
        data = givenData;
    }

    public Integer getData() {
        return data;
    }

    public void setData(Integer data) {
        this.data = data;
    }

    public Nod getLeft() {
        return left;
    }

    public void setLeft(Nod left) {
        this.left = left;
    }

    public Nod getRight() {
        return right;
    }

    public void setRight(Nod right) {
        this.right = right;
    }
}

class BinaryTree {
    private Nod root;

    BinaryTree(Nod givenRoot) {
        root = givenRoot;
    }

    private void addToNod(Nod nod, int data) {
        if (data < nod.data) {
            if (nod.left == null)
                nod.left = new Nod(data);
            else
                addToNod(nod.left, data);
        } else if (data > nod.data) {
            if (nod.right == null)
                nod.right = new Nod(data);
            else
                addToNod(nod.right, data);
        }
    }

    void add(int data) {
        if (root.data == null)
            root.data = data;
        else
            addToNod(root, data);
    }

    void preorder(Nod givenRoot) {
        if (givenRoot == null) return;
        System.out.println(givenRoot.data);
        preorder(givenRoot.left);
        preorder(givenRoot.right);
    }

    void inorder(Nod givenRoot) {
        if(givenRoot == null) return;
        inorder(givenRoot.left);
        System.out.println(givenRoot.data);
        inorder(givenRoot.right);
    }

    void postorder(Nod givenRoot) {
        if(givenRoot == null) return;
        postorder(givenRoot.left);
        postorder(givenRoot.right);
        System.out.println(givenRoot.data);
    }

    public static void main(String[] args) {
        Nod root = new Nod(10);
        BinaryTree binaryTree = new BinaryTree(root);
        binaryTree.add(5);
        binaryTree.add(3);
        binaryTree.add(7);
        binaryTree.add(2);
        binaryTree.add(12);
        binaryTree.preorder(root);
        System.out.println();
        binaryTree.inorder(root);
        System.out.println();
        binaryTree.postorder(root);
    }
}



