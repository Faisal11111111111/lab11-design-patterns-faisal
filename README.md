## Lab 11 – Factory & Strategy Debugging Notes

1. **How many if/elif branches does the factory use to select the operator?**  
   The factory does not use a chain of if/elif statements. Instead, it relies on a single dictionary lookup based on the operator type and the operator name.

2. **What Python data structure is used to select operators?**  
   A `dict` is used to map operator names (like `"redact"`, `"replace"`, `"initial"`) to their operator classes. The line `operator = operators_by_type.get(operator_name)` looks up the class in that dictionary.

3. **How does this demonstrate the Strategy design pattern?**  
   The AnonymizerEngine never hard-codes a specific operator implementation. It asks the factory for an operator by name and type, the factory looks up the matching class in a dictionary and instantiates it, and then the engine calls `operate` on that object. Because all operators share the same interface (`operate`, `operator_name`, etc.), the engine can swap different behaviors (strategies) at runtime simply by changing the operator name in the configuration.

4. **Call stack screenshot**  
   The screenshot `call-stack.png` in the repository root shows the full call stack when the factory selects the operator at `operator = operators_by_type.get(operator_name)`.
