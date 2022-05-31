#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linkes list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse throigh nodes as long as linked list node exists*/
		if (fast->next != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
