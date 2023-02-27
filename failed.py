        prev = self._root
        cur = self._root
        last = None
        while cur is not None:
            if last == 'right':
                prev = prev.right
            if last == 'left':
                prev = prev.left
            if value > cur.value:
                cur = cur.right
                last = 'right'
            if value < cur.value:
                cur = cur.left
                last = 'left'

        if cur == None:
            cur = BSTNode(value)
            if last == 'left':
                prev.left = cur
            if last == 'right':
                prev.right = cur