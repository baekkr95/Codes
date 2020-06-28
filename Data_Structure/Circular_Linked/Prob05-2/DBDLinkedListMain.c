#include <stdio.h>
#include "DBDLinkedList.h"

void ListPrint(List* plist) {
	Node* cur = plist->head->next;

	if (cur->next == NULL) {
		printf("There is no data");
	}

	while (cur->next != NULL) {
		printf("%d ", cur->data);
		cur = cur->next;
	}
	printf("\n");
}

int ListSum(List* plist) {
	Node* cur = plist->head->next;
	int sumdata = 0;

	if (cur->next == NULL) {
		printf("There is no data");
	}

	while (cur->next != NULL) {
		sumdata += cur->data;
		cur = cur->next;
	}
	return sumdata;
}

void AddNodeFront(List* plist, int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = plist->head->next;
	newNode->prev = plist->head;
	plist->head->next->prev = newNode;
	plist->head->next = newNode;

	(plist->numOfData)++;
}

void AddNodeLast(List* plist, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->prev = plist->tail->prev;
	plist->tail->prev->next = newNode;

	newNode->next = plist->tail;
	plist->tail->prev = newNode;

	(plist->numOfData)++;
}


int main(void)
{
	List list;
	int data;
	ListInit(&list);

	// 8개의 데이터 저장 ///////
	LInsert(&list, 1);  LInsert(&list, 2);
	LInsert(&list, 3);  LInsert(&list, 4);
	LInsert(&list, 5);  LInsert(&list, 6);
	LInsert(&list, 7);  LInsert(&list, 8);

	// 저장된 데이터의 조회 ///////
	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		while(LNext(&list, &data)) 
			printf("%d ", data);
		
		printf("\n");
	}
	printf("\n");
	printf("ListPrint: ");
	ListPrint(&list);

	printf("\n");

	printf("Sum of List: %d\n", ListSum(&list));

	AddNodeFront(&list, 10);
	AddNodeLast(&list, 20);

	printf("\n");

	ListPrint(&list);

	return 0;
}