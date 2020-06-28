#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define TRUE 1
#define False 0

typedef struct edge_t
{
	int fromNode;
	int toNode;
	int w;
	struct edge_t *next;
} edge;

typedef struct node_t
{
	struct node_t *p;
	int rank;
	int nodeID;

} node;

typedef struct element_t
{
	edge *e;
	struct element_t *next;
} element;

typedef struct list_t
{
	element *head;
	element *tail;
	int length;
} list;

void listInit(list *a)
{
	a->head = (element *)calloc(1, sizeof(element));
	a->tail = a->head->next;
	a->length = 0;
}

void makeSet(node *x)
{
	x->p = x;
	x->rank = 0;
	return;
}

node *findSet(node *x)
{
	if (x != x->p){
		x->p = findSet(x->p);
	}
	return x->p;
}

void link(node *x, node *y)
{
	if (x->rank > y->rank){
		y->p = x;
	}
	else {
		x->p = y;
		if (x->rank == y->rank){
			y->rank = y->rank + 1;
		}
	}
	return;
}

void union1(node *x, node *y)
{
	link(findSet(x), findSet(y));
}



typedef struct vec_t{
	double x;
	double y;
	double length;
}vec;

int compare(const void* a, const void* b){
	edge* x = (edge *) a;
	edge* y = (edge *) b;

	return (x->w - y->w);  //struct edge가 왜 불완전 형식?_?
}

void addLast(list *a, edge *e)
{
	if (!a->tail) {
		a->tail = (element *)calloc(1, sizeof(element));
		a->tail->e = e;
		a->head->next = a->tail;
	}
	else {
		a->tail->next = (element *)calloc(1, sizeof(element));
		a->tail->next->e = e;
		a->tail = a->tail->next;
	}
	return;
}

void printList(list *a)
{
	element *b = a->head->next;

	while (b) {
		printf("%d %d %d\n", b->e->fromNode, b->e->toNode, b->e->w);
		b = b->next;
	}
	return;
}

list *kruskal(node *V, edge *E, int numNode, int numEdge)
{
	list *a;
	int i;
	edge *e;

	a = (list *)calloc(1, sizeof(list));

	listInit(a);

	for (i=0; i<numNode; i++){
		makeSet(V+i);
	}

	/* for (i = 0; i < numEdge; i++) {
		e = E + i;
		printf("%d %d %d\n", e->fromNode, e->toNode, e->w);
	}
	printf("\n\n"); */
	qsort(E, numEdge, sizeof(edge), compare);

	/* for (i = 0; i < numEdge; i++) {
		e = E + i;
		printf("%d %d %d\n", e->fromNode, e->toNode, e->w);
	}*/

	for (i=0; i<numEdge; i++){
		e = E + i;
		if (findSet(V+e->fromNode) != findSet(V+e->toNode) ){
			addLast(a, e);
			union1(V+e->fromNode, V+e->toNode);
		}
	}
	return a;
}

int main()
{
	int i;
	list *A;
	edge *b, *E;
	node *V;

	FILE *ifp;
	int m, n, from, to, w;
	ifp = fopen("kruskaldata.in", "r");
	fscanf(ifp, "%d %d\n", &m, &n);

	V = (node *)calloc(m, sizeof(node));
	E = (edge *)calloc(n, sizeof(edge));

	for (i = 0; i < m; i++) {
		(V + i)->nodeID = i;
	}

	for (i = 0; i < n; i++) {
		fscanf(ifp, "%d %d %d\n", &from, &to, &w);
		b = E + i;
		b->fromNode = from;
		b->toNode = to;
		b->w = w;
	}

	A = kruskal(V, E, m, n);
	printList(A);

	return 0;



}