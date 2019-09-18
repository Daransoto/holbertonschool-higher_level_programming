#include "lists.h"
/**
* is_palindrome - Checks if a linked list is a palindrome.
* @head: Double pointer to the first element on the list.
* Return: 1 if list is palindrome, 0 if not.
*/
int is_palindrome(listint_t **head)
{
	int data[1000];
	short count, i;

	if (!head || !*head)
		return (1);
	for (count = 0; *head; *head = (*head)->next)
		data[count++] = (*head)->n;
	count--;
	for (i = 0; i < count; i++, count--)
		if (data[i] != data[count])
			return (0);
	return (1);
}
