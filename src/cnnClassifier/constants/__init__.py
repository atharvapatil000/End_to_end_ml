# The 'constants' folder is used in the project to centralize and manage all constant values. This promotes a clean and maintainable code structure.

from pathlib import Path

# CONFIG_FILE_PATH stores the path to the primary configuration file. Centralizing file paths here prevents hardcoding throughout the codebase.
CONFIG_FILE_PATH = Path("config/config.yaml")

# PARAMS_FILE_PATH stores the path to the parameter settings file, allowing easy access and modification of model parameters.
PARAMS_FILE_PATH = Path("params.yaml")

# Benefits of using a 'constants' folder:
# 1. Centralization: Simplifies the management of constant values, making them easy to find and modify.
# 2. Maintainability: Enhances code clarity and reduces maintenance overhead by isolating constants in a single directory.
# 3. Separation of Concerns: Keeps configuration data separate from business logic, improving code organization.
# 4. Scalability: Facilitates easy updates and modifications as project requirements grow or change.
# 5. Error Reduction: Reduces risks of inconsistencies and errors by ensuring all parts of the application reference the same constants.