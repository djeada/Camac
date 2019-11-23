package com.company;

import java.util.Random;
import java.util.stream.IntStream;

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

    private BinaryTree(Nod givenRoot) {
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

    private void add(int data) {
        if (root.data == null)
            root.data = data;
        else
            addToNod(root, data);
    }

    private void preorder(Nod givenRoot) {
        if (givenRoot == null) return;
        System.out.print(givenRoot.data + "-");
        preorder(givenRoot.left);
        preorder(givenRoot.right);
    }

    private void inorder(Nod givenRoot) {
        if (givenRoot == null) return;
        inorder(givenRoot.left);
        System.out.print(givenRoot.data + "-");
        inorder(givenRoot.right);
    }

    private void postorder(Nod givenRoot) {
        if (givenRoot == null) return;
        postorder(givenRoot.left);
        postorder(givenRoot.right);
        System.out.print(givenRoot.data + "-");
    }

    private Nod searchNod(Nod nod, int data) {
        Nod tmp = null;
        if (nod != null) {
            if (nod.data == data)
                tmp = nod;
            else if (data < nod.data)
                tmp = searchNod(nod.left, data);
            else
                tmp = searchNod(nod.right, data);
        }
        return tmp;
    }

    private Nod search(int data) {
        if (root.data == data)
            return root;
        return searchNod(root, data);
    }

    public static void main(String[] args) {
        Nod root = new Nod(50);
        BinaryTree binaryTree = new BinaryTree(root);

        Random random = new Random();
        IntStream.range(0, 100).parallel().forEach(
                nbr -> binaryTree.add(random.nextInt(100))
        );


        binaryTree.preorder(root);
        System.out.println();
        binaryTree.inorder(root);
        System.out.println();
        binaryTree.postorder(root);
        System.out.println();

        int searchFor = 7;
        try {
            Nod nod = binaryTree.search(searchFor);
            System.out.println("Found node: " + nod.data);
        } catch (NullPointerException e) {
            System.out.println("Not found node: " + searchFor);
        }
    }
}