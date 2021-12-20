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
	listint_t *simple_node, *double_node;

	simple_node = list, double_node = list;

	for (; simple_node && double_node && double_node->next; simple_node = simple_node->next)
	{
		double_node = double_node->next->next

		if (simple_node == double_node)
			return (1);
	}

	return (0);
}
