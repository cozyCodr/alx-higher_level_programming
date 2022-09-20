#include <stdio.h>
#include <lists.h>
/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to head of list
 * Return: 1 if cycle is found and 0 if no cyle is found
 */
int check_cycle(listint_t *list){

	listint_t *fast;
	listint_t *slow;

	fast = list->next;
	slow = list;

	while (slow != null)
	{
		if (slow == fast && fast != null)
			return (1);
		if (fast->next->next != null)
			fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
