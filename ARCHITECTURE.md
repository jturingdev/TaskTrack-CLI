# TaskTracker Architecture

1. System overview
   1. CLILayer: Entrypoint
   2. CommandParser: commands logic functions
   3. TaskManager: bussiness logic management state to tasks
   4. StorageLayer: infra camada read and writing to path

2. Components
- Domain Model: Task and states
- Controller: operations model and repository count ids
- Repository: abstract complexity manipulation to path json
- CLI App: commands subparser and comunicate with user

3. Data Flow
   1. Input: argparse
   2. Processing: TaskManager intance new object Task
      generating uuid and timestamps
   3. Transformation: object task converted dict vars(new_task) to serializabel
   4. Persistence: json_repo gain updated list to dicts and replaced to path tasks.json atomic

4. Complexity considerations
   - WritingOperations:
    load list tasks in memory add/modify item and rewriting complete path.
   - TemporalComplexity:
     - List: O(1)
     - Search/Update:O(n)
     - Remove:O(n)