#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of a list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = c = list;
	while (a && b && b->next)
	{
		c = b->next->next;
		a = a->next;
		if (a == b)
		return (1);
	}
	return (0);
}
