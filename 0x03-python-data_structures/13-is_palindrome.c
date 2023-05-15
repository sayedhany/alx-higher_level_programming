#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of the list
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return *head;
}

/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: double pointer to head of the list
  * Return: 1 if the list is a palindrome, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half = NULL;
	listint_t *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return is_palindrome;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_of_slow_ptr = slow_ptr;
	slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		midnode = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	second_half = slow_ptr;
	prev_of_slow_ptr->next = NULL;
	reverse_list(&second_half);

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
	*head = (*head)->next;
	second_half = second_half->next;
	}

	reverse_list(&second_half);
	if (midnode != NULL)
	{
		prev_of_slow_ptr->next = midnode;
		midnode->next = second_half;
	}
	else
		prev_of_slow_ptr->next = second_half;
	return is_palindrome;
}

