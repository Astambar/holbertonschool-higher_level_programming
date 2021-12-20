#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - detecte si une list est un cycle
 * @list: list chaîner tester
 * Return: 1 si c'est un cycle et 0 si ce n'est pas le cas
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
