from behave import *
from LinkedList.LinkedListNode import *
use_step_matcher("re")


@when("I Create Node")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.node = LinkedListNode(5)
	pass


@then("The Node Contains data and a pointer with None")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	assert(context.node.data is not None)
	assert(context.node.next is None)


@when("I Create head node")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.head = LinkedListNode(5)
	pass


@step("Add a second node to the first one")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	context.head.next = LinkedListNode(13)
	pass


@then("The head node contains data and a pointer to the second node")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	assert (context.head.data == 5)
	assert (context.head.next is not None)


@step("Second node contains data and an empty pointer")
def step_impl(context):
	"""
	:type context: behave.runner.Context
	"""
	assert(context.head.next.data == 13)
	assert(context.head.next.next is not None)