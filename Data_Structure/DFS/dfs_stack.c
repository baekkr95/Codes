#include<stdio.h>
#include<stdlib.h>

typedef enum nodeColor_t 
{
	WHITE, GRAY, BLACK
} nodeColor;

typedef struct element_t
{
	int toNode;
	int fromNode;
	int w;
	struct element_t *next;
} element;

typedef struct list_t
{
	element *head;
	element *tail;
	int length;
	int nodeID;
	nodeColor color;
	struct list_t *next;
} list;

typedef struct stack_t
{
	list *head;
} stack;

list *pop(stack *s)
{
	list *n;
	if(!s->head->next) return NULL;
	else {
		n = s->head->next;
		s->head->next = n->next;
		return n;
	}
}

void push(stack *s, list *l)
{
	l->next = s->head->next;
	s->head->next = l;
	return;
}
	
list *top(stack *s)
{
	return s->head->next;
}

void initStack(stack *s)
{
	s->head = (list *) calloc(1, sizeof(list));
	return;
}

int stackEmpty(stack *s) 
{
	if(!s->head->next) return 1;
	else return 0;
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

void printList(list *a){
	element *b = a->head->next;

	while (b){
		printf("%3d -> ", b->toNode);
		b = b->next;
	}
	printf("\n");
	return;
}

void printGraph(list *a, int numNode){

	int i;

	for (i = 0; i < numNode; i++){
		printf("%3d :", i);
		printList(a + i);

	}
	return;

}

void DFS_stack(list *V, list *v)
{
	stack S;
	list *w, *n, *m, *k;
	element *a;

	initStack(&S);
	v->color = GRAY;
	printf("%d - ",v->nodeID);
	push(&S, v);

	while(!stackEmpty(&S)) {
		n = top(&S);
		a = n->head->next;
		while(a && (V+a->toNode)->color == GRAY) a = a->next;
		if(!a) k = pop(&S);
		else {
			m = V+a->toNode;
			m->color = GRAY;
			printf("%d - ", m->nodeID);
			push(&S, m);
				
		}
	}
	printf("\n\n");
	return;
}

int main()
{
	int i;
	list *V;
	element *b;
	FILE *ifp;
	int m, n, from, to, w;

	ifp = fopen("data8.in", "r");

	fscanf(ifp, "%d %d\n", &m, &n);

	V = (list *)calloc(m, sizeof(list));

	for (i = 0; i < m; i++) {
		listInit(V + i);
		(V + i)->nodeID = i;
		(V + i)->color = WHITE;
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

	DFS_stack(V, V);
	return 0;



}