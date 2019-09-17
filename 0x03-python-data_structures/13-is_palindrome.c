#include "lists.h"
/**
* is_palindrome - Checks if a linked list is a palindrome.
* @head: Double pointer to the first element on the list.
* Return: 1 if list is palindrome, 0 if not.
*/
int is_palindrome(listint_t **head)
{
	listint_t *beg = *head, *end = NULL, *it = *head;

	if (!head || !*head)
		return (1);
	while (1)
	{
		while (it && it->next != end)
			it = it->next;
		if (!it)
			return (1);
		end = it;
		if (beg->n != end->n)
			return (0);
		beg = beg->next;
		it = beg;
	}
	return (1);
}
