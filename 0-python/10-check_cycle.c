#include "lists.h"
/**
 * check_cycle - check cycle.
 * @list: firest value.
 *
 * Return: value
 */
int check_cycle(listint_t *list)
{
	listint_t *new;

	new = list;
	while (new)
	{
		new = new->next;

		if (new == list)
		return (1);
	}
	return (0);
}
