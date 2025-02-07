import codegen
from codegen import Codebase


@codegen.function('add-docstrings')
def run(codebase: Codebase):
    for function in codebase.functions:
        # Check if the function already has a docstring
        if not function.docstring:
            # Generate a new docstring
            param_list = '\n    '.join(f'{param.name} ({param.type.source if param.is_typed else "Any"}): Description of {param.name}' for param in function.parameters)
            return_type = function.return_type.source if function.return_type else "None"
        
            docstring_template = f'''
    """Function {function.name}.

    Description: This function does something.

    Args:
        {param_list}

    Returns:
        {return_type}: Description of return value.
    """
            '''
            # Set the generated docstring
            function.set_docstring(docstring_template)

    # After modifying the codebase, ensure changes are committed
    codebase.commit()


if __name__ == "__main__":
    print('Parsing codebase...')
    codebase = Codebase("./")

    print('Running function...')
    codegen.run(run)
