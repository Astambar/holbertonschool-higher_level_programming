#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/*
 * is_palindrome - fonctio à un seul argument
 * @head: pointer to linked list
 * Return: 1 si c'est vrais sinon 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *phead;
	int count = 0, count2 = 0, calcul;
	int *buffer = NULL;

	if (!head)
	      return (0);
	if (!*head)
		return (1);
	phead = *head;
	if (phead)
		for (;phead->next; phead = phead->next, count++)
		;
	buffer = malloc(sizeof(int) * count);
	if (!buffer)
		return (0);

	phead = *head;
	count = 0;
	while (phead)
	{
		buffer[count] = (*phead).n;
		count++;
		phead = (*phead).next;
	}
	calcul = count / 2;

	while (calcul)
	{
		if (buffer[count2] != buffer[count - 1])
			return (0);
		calcul--, count2++, count--;
	}
	free(buffer);
	return (1);
}