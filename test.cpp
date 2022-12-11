  void up_heap(int i) {
    if( i != root_index && node[i].getKey() < getParent(i).getKey()) {
      int temp = node[i].getKey();
      node[i].setKey(getParent(i).getKey());
      getParent(i).setKey(temp);

      up_heap( i / 2 );
    }
  }

  void down_heap(int i) {
    Node left_child = getLeft(i);
    Node right_child = getRight(i);
    int left = i*2;
    int right = i*2+1;

    int smallest = i;
    if(left <= cur_size && left_child.getKey() < node[smallest].getKey()) {
      smallest = left;
    }
    if(right <= cur_size && right_child.getKey() < node[smallest].getKey()) {
      smallest = right;
    }
    if(smallest != i) {
      int temp = node[smallest].getKey();
      node[smallest].setKey(node[i].getKey());
      node[i].setKey(temp);
      down_heap(smallest);
    }
  }
