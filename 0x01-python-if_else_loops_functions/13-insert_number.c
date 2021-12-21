#include "lists.h"

/**
 * insert_node - Insert un nouveaux noeud triée par ordre croissant
 *
 * @head: Pointer vers le début de la liste chaînée
 * @number: Nombre de nouveau noeud
 *
 * Return: L'adresse du nouveau noeud, ou NULL en cas d'échec.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *numbercurrent;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	(*new_node).n = number;

	numbercurrent = *head;
	if (numbercurrent)
		if ((*numbercurrent).n > number)
			(*new_node).next = numbercurrent, *head = new_node;
		else
		{
			while (numbercurrent && (*numbercurrent).next)
				if ((*(*numbercurrent).next).n < number)
					numbercurrent = (*numbercurrent).next;
				else
					break;
			(*new_node).next = (*numbercurrent).next;
			(*numbercurrent).next = new_node;
		}
	else
		*head = new_node, (*new_node).next = NULL;

	return (new_node);
}
