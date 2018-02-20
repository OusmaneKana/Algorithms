import java.util.*;

/** 
 * CircularArrayQueue represents an array implementation of a queue in  
 * which the indexes for the front and rear of the queue circle back to 0 
 * when they reach the end of the array. 
 *  
 * @author Lewis and Chase 
 * @version 4.0 
 */ 

public class CircularArrayQueue<T> implements QueueADT<T>

{ 

    private final static int DEFAULT_CAPACITY = 100; 

private int front, rear, count; 
private T[] queue;  

	/** 
     * Creates an empty queue using the specified capacity. 
     * @param initialCapacity the initial size of the circular array queue 
     */

    public CircularArrayQueue (int initialCapacity) 

    { 

        front = rear = count = 0; 
        queue = (T[]) (new Object[initialCapacity]); 
    } 

    /** 
     * Creates an empty queue using the default capacity. 
     */

    public CircularArrayQueue() 

    { 
        this(DEFAULT_CAPACITY);
    }  

  /** 
     * Adds the specified element to the rear of this queue, expanding 
     * the capacity of the queue array if necessary. 
	 * @param element the element to add to the rear of the queue 
     */ 

    public void enqueue(T element) 

	{ 

        if (size() == queue.length)  
        	expandCapacity(); 

        queue[rear] = element; 
        rear = (rear+1) % queue.length; 
        count++; 

    }
}



/** The program is not gonna work, because the programmer who wrote it called
    many functions that he wrote by himself and made up his own library *that
    I eventually don't have*. 
    If anyone would like to implement his own import a dictionnary of his own
    to replace some non-working functions calls, he or she is welcom to do so!
    **/ 