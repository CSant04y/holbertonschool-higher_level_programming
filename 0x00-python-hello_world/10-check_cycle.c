#include "lists.h"
/**
 * check_cycle - This checks to see if a linked list is a cycle
 * @list: this is the head of the linked list
 * Return: 0 if not a cycle 1 if a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *a = list;

	while (head && a && a->next)
	{
		a = a->next->next;
		head = head->next;
		if (a == head)
			return (1);
	}

	return (0);
}
