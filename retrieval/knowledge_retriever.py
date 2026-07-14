class KnowledgeRetriever:

    """
    Retrieves structured knowledge
    from CareerNova AI.
    """

    def retrieve(

        self,

        resume=None,

        ats=None,

        interview=None,

        analytics=None

    ):

        knowledge = {}

        if resume:

            knowledge["resume"] = resume

        if ats:

            knowledge["ats"] = ats

        if interview:

            knowledge["interview"] = interview

        if analytics:

            knowledge["analytics"] = analytics

        return knowledge