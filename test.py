#!/usr/bin/env python3
"""
Test script for SEC Championship Simulator
Run this to verify your Clingo installation and basic functionality
"""

import sys

def test_clingo_import():
    """Test if Clingo can be imported"""
    print("Testing Clingo import...")
    try:
        import clingo
        print("✓ Clingo imported successfully")
        print(f"  Version: {clingo.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Failed to import Clingo: {e}")
        print("  Install with: pip install clingo")
        return False

def test_flask_import():
    """Test if Flask can be imported"""
    print("\nTesting Flask import...")
    try:
        import flask
        print("✓ Flask imported successfully")
        print(f"  Version: {flask.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Failed to import Flask: {e}")
        print("  Install with: pip install flask")
        return False

def test_basic_clingo():
    """Test basic Clingo functionality"""
    print("\nTesting basic Clingo functionality...")
    try:
        import clingo
        
        ctl = clingo.Control()
        
        # Simple test program
        program = """
        team(a).
        team(b).
        { winner(T) : team(T) } = 1.
        #show winner/1.
        """
        
        ctl.add("base", [], program)
        ctl.ground([("base", [])])
        
        solutions = []
        def on_model(model):
            solutions.append([str(atom) for atom in model.symbols(shown=True)])
        
        ctl.solve(on_model=on_model)
        
        if solutions:
            print("✓ Clingo solving works correctly")
            print(f"  Found {len(solutions)} solution(s)")
            return True
        else:
            print("✗ Clingo didn't find solutions")
            return False
            
    except Exception as e:
        print(f"✗ Clingo test failed: {e}")
        return False

def test_app_structure():
    """Test if required files exist"""
    print("\nTesting project structure...")
    import os
    
    required_files = [
        'app.py',
        'templates/index.html',
        'static/style.css',
        'static/script.js',
        'requirements.txt'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 60)
    print("SEC Championship Simulator - Test Suite")
    print("=" * 60)
    
    tests = [
        test_clingo_import(),
        test_flask_import(),
        test_basic_clingo(),
        test_app_structure()
    ]
    
    print("\n" + "=" * 60)
    passed = sum(tests)
    total = len(tests)
    
    if passed == total:
        print(f"✓ All tests passed ({passed}/{total})")
        print("\nYou're ready to run the simulator!")
        print("Start with: python app.py")
        return 0
    else:
        print(f"✗ Some tests failed ({passed}/{total} passed)")
        print("\nPlease fix the issues above before running the simulator.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
