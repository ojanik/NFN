from jax.tree_util import tree_map
import jax.numpy as jnp

## A collection of functions acting on pytrees

def add_pytrees(pytree1, pytree2):
  return tree_map(lambda pt1, pt2: pt1 + pt2, pytree1, pytree2)

def substract_pytrees(pytree1, pytree2):
  return tree_map(lambda pt1, pt2: pt1 - pt2, pytree1, pytree2)

def multiply_pytrees(pytree1, pytree2):
  return tree_map(lambda pt1, pt2: pt1 * pt2, pytree1, pytree2)

def divide_pytrees(pytree1, pytree2):
  return tree_map(lambda pt1, pt2: pt1 / pt2, pytree1, pytree2)

def scale_pytrees(scalar, pytree):
  return tree_map(lambda pt: scalar * pt, pytree)

def median_pytree(*pytree):
  def elem_median(*leaves):
    stacked = jnp.stack(leaves)
    return jnp.median(stacked, axis=0)
  return tree_map(elem_median, *pytree)

def apply_mask(grads, mask):
    # Recursively apply mask to each parameter
    return tree_map(lambda g, m: g * m, grads, mask)

def rearrange_matrix(matrix, indices):
    n = matrix.shape[0]
    
    # Create a new order of indices: specified ones first, then the rest
    new_order = indices + [i for i in range(n) if i not in indices]
    
    # Rearrange the rows and columns
    matrix_rearranged = matrix[new_order, :][:, new_order]
    return matrix_rearranged