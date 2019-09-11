#include "lists.h"
#include <stdlib.h>
/**
* insert_node - Adds a node on a sorted list.
* @head: Pointer to the current first element of the list.
* @number: Number to initialize the new element.
* Return: Pointer to the new first element or 0 if it fails.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *iterator = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (iterator->next)
		{
			if (number <= iterator->next->n)
			{
				new->next = iterator->next;
				iterator->next = new;
				return (new);
			}
			iterator = iterator->next;
		}
	}
	new->next = NULL;
	iterator->next = new;
	return (new);
}
