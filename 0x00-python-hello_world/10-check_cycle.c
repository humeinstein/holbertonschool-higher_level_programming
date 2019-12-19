#include "lists.h"
/**
 * check_cycle - check if linked list contains cycle
 * @list: list of ls
 * Return: 0 if no cucle 1 if true
 */
int check_cycle(listint *list)
{
  listint_t *up, *down;

  if (list == NULL || list->next == NULL)
    return (0);

  up = list;
  down = list->next;
  
  while (up != NULL && down->next != NULL)
    {
      while (down->next->next != NULL)
	{
	  if (up == down)
	    return (1);
	  down = down->next->next;
	  up = up->next;
	}
    }
  return (0);
}
