#include <stdio.h>
#include "DBLinkedList.h"

void ListPrint(List* plist) {
	Node* cur = plist->head;

	if (cur->next == NULL) {
		printf("There is no data");
	}

	while (cur->next != NULL) {
		printf("%d ", cur->data);
		cur = cur->next;
	}
}

int ListSum(List* plist) {

}

int main(void)
{
	// ����� ���� ����Ʈ�� ���� �� �ʱ�ȭ  ///////
	List list;
	int data;
	ListInit(&list);

	// 8���� ������ ����  ///////
	LInsert(&list, 1);  LInsert(&list, 2);
	LInsert(&list, 3);  LInsert(&list, 4);
	LInsert(&list, 5);  LInsert(&list, 6);
	LInsert(&list, 7);  LInsert(&list, 8);

	// ����� �������� ��ȸ  ///////
	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		while(LNext(&list, &data)) 
			printf("%d ", data);
		
		while(LPrevious(&list, &data))
			printf("%d ", data);
		
		printf("\n\n");
	}

	ListPrint(&list);

	return 0;
}