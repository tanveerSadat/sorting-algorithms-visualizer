"""
Unit tests for sorting algorithms (bubble sort and selection sort)
Tests both the basic sorting functions and the step-by-step visualization
"""

import sys
import os

# python backend/tests/algos_test.py
# pytest tests/algos_test.py -v --cov=. --cov-report=html

# Add parent directory to path to import sorting modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bubblesort
import selectionsort

# Bubble Sort Tests
class TestBubbleSort:
    """Test cases for bubble sort implementation"""

    def test_empty_array(self):
        """Test sorting an empty array"""
        arr = []
        bubblesort.bubbleSort(arr)
        assert arr == []

    def test_single_element(self):
        """Test sorting a single element array"""
        arr = [5]
        bubblesort.bubbleSort(arr)
        assert arr == [5]

    def test_already_sorted(self):
        """Test sorting an already sorted array"""
        arr = [1, 2, 3, 4, 5]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array (worst case)"""
        arr = [5, 4, 3, 2, 1]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_unsorted_array(self):
        """Test sorting a random unsorted array"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements"""
        arr = [3, 3, 1, 1, 2, 2]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 1, 2, 2, 3, 3]

    def test_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        arr = [-3, -1, -4, 0, 2, 1]
        bubblesort.bubbleSort(arr)
        assert arr == [-4, -3, -1, 0, 1, 2]

    def test_large_array(self):
        """Test sorting a larger array"""
        arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_two_elements_sorted(self):
        """Test sorting two elements already in order"""
        arr = [1, 2]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 2]

    def test_two_elements_unsorted(self):
        """Test sorting two elements not in order"""
        arr = [2, 1]
        bubblesort.bubbleSort(arr)
        assert arr == [1, 2]

class TestBubbleSortWithSteps:
    """Test cases for bubble sort with visualization steps"""

    def test_steps_empty_array(self):
        """Test that steps are generated for empty array"""
        arr = []
        steps = bubblesort.bubbleSortWithSteps(arr)
        assert isinstance(steps, list)

    def test_steps_structure(self):
        """Test that each step has the correct structure"""
        arr = [3, 1, 2]
        steps = bubblesort.bubbleSortWithSteps(arr)
        
        # Each step should be: [array, i, j, swapped]
        for step in steps:
            assert isinstance(step, list)
            assert len(step) == 4
            assert isinstance(step[0], list)  # array
            assert isinstance(step[1], int)   # i index
            assert isinstance(step[2], int)   # j index
            assert isinstance(step[3], bool)  # swapped flag

    def test_steps_final_array_sorted(self):
        """Test that the final array in steps is sorted"""
        arr = [5, 2, 8, 1]
        steps = bubblesort.bubbleSortWithSteps(arr)
        
        if len(steps) > 0:
            final_array = steps[-1][0]
            assert final_array == sorted([5, 2, 8, 1])

    def test_steps_contains_swaps(self):
        """Test that steps contain swap operations when needed"""
        arr = [2, 1]
        steps = bubblesort.bubbleSortWithSteps(arr)
        
        # Should have at least one step with swapped=True
        has_swap = any(step[3] == True for step in steps)
        assert has_swap

    def test_steps_no_swaps_when_sorted(self):
        """Test that no swaps occur for already sorted array"""
        arr = [1, 2, 3]
        steps = bubblesort.bubbleSortWithSteps(arr)
        
        # Count swap operations
        swap_count = sum(1 for step in steps if step[3] == True)
        assert swap_count == 0

    def test_steps_indices_valid(self):
        """Test that all indices in steps are valid"""
        arr = [5, 2, 8, 1]
        steps = bubblesort.bubbleSortWithSteps(arr)
        
        n = len(arr)
        for step in steps:
            i_index = step[1]
            j_index = step[2]
            
            # Indices should be within array bounds
            assert 0 <= i_index < n
            assert 0 <= j_index < n

# Selection sort tests
class TestSelectionSort:
    """Test cases for selection sort implementation"""

    def test_empty_array(self):
        """Test sorting an empty array"""
        arr = []
        selectionsort.selectionSort(arr)
        assert arr == []

    def test_single_element(self):
        """Test sorting a single element array"""
        arr = [5]
        selectionsort.selectionSort(arr)
        assert arr == [5]

    def test_already_sorted(self):
        """Test sorting an already sorted array"""
        arr = [1, 2, 3, 4, 5]
        selectionsort.selectionSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        selectionsort.selectionSort(arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_unsorted_array(self):
        """Test sorting a random unsorted array"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        selectionsort.selectionSort(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements"""
        arr = [3, 3, 1, 1, 2, 2]
        selectionsort.selectionSort(arr)
        assert arr == [1, 1, 2, 2, 3, 3]

    def test_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        arr = [-3, -1, -4, 0, 2, 1]
        selectionsort.selectionSort(arr)
        assert arr == [-4, -3, -1, 0, 1, 2]

    def test_large_array(self):
        """Test sorting a larger array"""
        arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]
        selectionsort.selectionSort(arr)
        assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_two_elements_sorted(self):
        """Test sorting two elements already in order"""
        arr = [1, 2]
        selectionsort.selectionSort(arr)
        assert arr == [1, 2]

    def test_two_elements_unsorted(self):
        """Test sorting two elements not in order"""
        arr = [2, 1]
        selectionsort.selectionSort(arr)
        assert arr == [1, 2]


class TestSelectionSortWithSteps:
    """Test cases for selection sort with visualization steps"""

    def test_steps_empty_array(self):
        """Test that steps are generated for empty array"""
        arr = []
        steps = selectionsort.selectionSortWithSteps(arr)
        assert isinstance(steps, list)

    def test_steps_structure(self):
        """Test that each step has the correct structure"""
        arr = [3, 1, 2]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        # Each step should be: [array, i, j, min index, swapped]
        for step in steps:
            assert isinstance(step, list)
            assert len(step) == 5
            assert isinstance(step[0], list)  # array
            assert isinstance(step[1], int)   # i index
            assert isinstance(step[2], int)   # j index
            assert isinstance(step[3], int)   # min index
            assert isinstance(step[4], bool)  # swapped flag

    def test_steps_final_array_sorted(self):
        """Test that the final array in steps is sorted"""
        arr = [5, 2, 8, 1]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        if len(steps) > 0:
            final_array = steps[-1][0]
            assert final_array == sorted([5, 2, 8, 1])

    def test_steps_contains_swaps(self):
        """Test that steps contain swap operations when needed"""
        arr = [3, 1, 2]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        # Should have at least one step with swapped=True
        has_swap = any(step[4] == True for step in steps)
        assert has_swap

    def test_steps_min_index_valid(self):
        """Test that minIndex in steps is always valid"""
        arr = [5, 2, 8, 1]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        n = len(arr)
        for step in steps:
            min_index = step[3]
            
            # min index should be within array bounds
            assert 0 <= min_index < n

    def test_steps_indices_valid(self):
        """Test that all indices in steps are valid"""
        arr = [5, 2, 8, 1]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        n = len(arr)
        for step in steps:
            i_index = step[1]
            j_index = step[2]
            min_index = step[3]
            
            # All indices should be within array bounds
            assert 0 <= i_index < n
            assert 0 <= j_index < n
            assert 0 <= min_index < n

    def test_min_index_in_unsorted_portion(self):
        """Test that minIndex is always in the unsorted portion"""
        arr = [5, 2, 8, 1]
        steps = selectionsort.selectionSortWithSteps(arr)
        
        for step in steps:
            i = step[1]
            min_index = step[3]
            
            # min index should be >= i (within unsorted portion)
            assert min_index >= i


# Comparison Tests (verify both algorithms sort the same)
class TestAlgorithmEquivalence:
    """Test that both sorting algorithms produce the same results"""

    def test_same_result_random_array(self):
        """Test that both algorithms sort the same array identically"""
        arr1 = [3, 7, 1, 9, 2, 5]
        arr2 = arr1.copy()
        
        bubblesort.bubbleSort(arr1)
        selectionsort.selectionSort(arr2)
        
        assert arr1 == arr2

    def test_same_result_reverse_sorted(self):
        """Test both algorithms on reverse sorted array"""
        arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr2 = arr1.copy()
        
        bubblesort.bubbleSort(arr1)
        selectionsort.selectionSort(arr2)
        
        assert arr1 == arr2

    def test_same_result_with_duplicates(self):
        """Test both algorithms on array with duplicates"""
        arr1 = [5, 2, 5, 1, 2, 5, 1]
        arr2 = arr1.copy()
        
        bubblesort.bubbleSort(arr1)
        selectionsort.selectionSort(arr2)
        
        assert arr1 == arr2


if __name__ == "__main__":
    # Run tests if executed directly
    import pytest
    pytest.main([__file__, "-v"])
