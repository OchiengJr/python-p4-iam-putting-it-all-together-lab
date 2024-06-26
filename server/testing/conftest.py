#!/usr/bin/env python3

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par and par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node and node.__doc__ else node.__name__
    
    # Ensure pref and suf are not empty
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
        logger.debug(f"Custom node ID set for item {item}: {item._nodeid}")
    else:
        logger.warning(f"Empty pref or suf for item {item}. Using default node ID.")
        item._nodeid = repr(item)

# Example usage
if __name__ == '__main__':
    # Simulate item for testing
    class ParentTestClass:
        pass
    
    class TestNode:
        def test_example(self):
            """Example test method"""
            assert 1 == 1
    
    item = TestNode().test_example
    
    # Call pytest_itemcollected with the simulated item
    pytest_itemcollected(item)
