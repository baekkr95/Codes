#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define infty 10000;

int time1;

typedef enum colorName_t
{
	WHITE, GRAY, BLACK
} colorName;

typedef enum edgeTypeName_t
{
	Tree, Forward, Back, Cross
} edgeTypeName;

typedef struct element_t
{
	int fromNode;
	int toNode;
	int w;
	edgeTypeName edgeType;
	struct element_t *next;
} element;

typedef struct list_t
{
	element *head;
	element *tail;
	int length;
	int d;
	int f;
	int nodeID;
	struct list_t *pi;
	colorName color;
	struct list_t *next;
} list;

#define MAX_ELEMENT 100

typedef struct {
	list *heap[MAX_ELEMENT];
	int heap_size;
} HeapType;

void initHeap(HeapType *h)
{
	h->heap_size =0;
}
//
int isHeapEmpty(HeapType *h)
{
	if( h->heap_size == 0 )
		return 1;
	else
		return 0;
}

void insert_min_heap(HeapType *h, list *item) 
{ 
    int i; 
    i = ++(h->heap_size); 

    
    while((i != 1) && (item->d < h->heap[i/2]->d)){ 
	   h->heap[i] = h->heap[i/2]; 
       i /= 2; 
    } 
    h->heap[i] = item;     
} 

list *delete_min_heap(HeapType *h) 
{ 
    int parent, child; 
    list *item, *temp;

    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];
    parent = 1;	
    child = 2;
    while( child <= h->heap_size ){
	  // 현재 노드의 자식노드중 더 작은 자식노드를 찾는다.
	  if( ( child < h->heap_size ) && 
	      (h->heap[child]->d) > h->heap[child+1]->d)
	      child++;
	  if( temp->d <= h->heap[child]->d ) break;
	  // 한단계 아래로 이동
	  h->heap[parent] = h->heap[child];
	  parent = child;
	  child *= 2;
    }
    h->heap[parent] = temp;
    return item;
} 

typedef struct qlist_t
{
	list *head;
	list *tail;
	int length;
} qlist;

void enqueue(qlist *a, list *b)
{
	if (!a->tail) {
		a->head->next = b;
		a->tail = b;
		++a->length;
		return;
	}
	else {
		a->tail->next = b;
		a->tail = a->tail->next;
		++a->length;
		return;
	}
}

int isQueueEmpty(qlist *a)
{
	if (!a->head->next) return 1;
	else return 0;
}

void qlistInit(qlist *a)
{
	a->head = (list *)calloc(1, sizeof(list));
	a->tail = NULL;
	return;
}

list *dequeue(qlist *a)
{
	list *removed = a->head->next;

	if (!removed) {
		printf("error list is empty\n");
		return NULL;
	}

	if (a->tail != removed) a->head->next = removed->next;
	else {
		a->head->next = NULL;
		a->tail = NULL;
	}
	--a->length;
	return removed;
}

void listInit(list *a)
{
	a->head = (element *)calloc(1, sizeof(element));
	a->tail = a->head->next;
	a->length = 0;
}

void addArc(list *a, element *b)
{
	if (!a->tail) {
		a->head->next = b;
		a->tail = b;
		++a->length;
		return;
	}
	else {
		a->tail->next = b;
		a->tail = a->tail->next;
		++a->length;
		return;
	}
}

void BFS(list *a, int sourceNodeID, int numNode)
{
	int i;
	qlist L;
	list *source = a + sourceNodeID;
	list *u, *v;
	element *e;
	source->pi = NULL;
	qlistInit(&L);
	enqueue(&L, source);

	for (i = 0; i < numNode; i++){
		if (i != sourceNodeID){
			(a + i)->color = WHITE;
			(a + i)->d = infty;
			(a + i)->pi = NULL;
		}
	}
	(a + sourceNodeID)->color = GRAY;
	qlistInit(&L);
	enqueue(&L, source);

	while (!isQueueEmpty(&L)){
		u = dequeue(&L);
		e = u->head->next;
		while (e){
			v = a + e->toNode;
			if (v->color == WHITE){
				v->color = GRAY;
				v->d = u->d + 1;
				printf("%d %d \n", v->nodeID, v->d);
				v->pi = u;
				enqueue(&L, v);
			}
			e = e->next;
		}
		u->color = BLACK;
	}
	return;
}

void DFS_Visit(list *a, list *u)
{

}

void DFS(list *a, int numNode)
{

}

void printList(list *a)
{
	element *b = a->head->next;

	while (b) {
		printf("%d->", b->toNode);
		b = b->next;
	}
	printf("\n");
	return;
}

void printGraph(list *a, int numNode)
{
	int i;

	for (i = 0; i < numNode; i++) {
		printf("%3d :", i);
		printList(a + i);
	}
	return;
}



int main()
{
	int i;
	list *V;
	element *b;
	FILE *ifp;
	int m, n, from, to, w;

	ifp = fopen("data.in", "r");

	fscanf(ifp, "%d %d\n", &m, &n);

	V = (list *)calloc(m, sizeof(list));

	for (i = 0; i < m; i++) {
		listInit(V + i);
		(V + i)->nodeID = i;
	}
	for (i = 0; i < n; i++) {
		fscanf(ifp, "%d %d %d\n", &from, &to, &w);
		b = (element *)calloc(1, sizeof(element));
		b->fromNode = from;
		b->toNode = to;
		b->w = w;
		addArc(V + from, b);
	}

	printGraph(V, m);


	BFS(V, 1, 8);


	return 0;



}