from queue_and_stack import Queue
cmparator = 0
def recursive(vari = Queue()):
    if vari.is_empty():
        vari.enqueue(0)
    global cmparator
    cmparator = vari.dequeue()
    if cmparator == 10:
        vari.enqueue(cmparator)
        print('in the comparer',vari)
        return
    else:
        print(cmparator, "is entering the rcur loop")
        vari.enqueue(cmparator+1)
        recursive(vari)
    print('before exiting',vari)
    if vari.is_empty() is False:
        cmparator = vari.dequeue()
    return cmparator
print(recursive())