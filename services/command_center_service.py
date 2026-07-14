from orchestrator.agent_orchestrator import AgentOrchestrator


class CommandCenterService:

    """
    Single entry point
    for every AI request.
    """

    def __init__(self):

        self.orchestrator = AgentOrchestrator()

    def process(

        self,

        question,

        resume=None,

        job_description=None,

        interview=None,

        analytics=None

    ):

        return self.orchestrator.execute(

            question,

            resume,

            job_description,

            interview,

            analytics

        )