class IntentRouter:
    """
    Routes a user's request to the correct AI agent.
    """

    def route(self, question: str):

        text = question.lower()

        if any(word in text for word in [
            "resume",
            "cv",
            "profile"
        ]):
            return "resume"

        elif any(word in text for word in [
            "ats",
            "job description",
            "keywords"
        ]):
            return "ats"

        elif any(word in text for word in [
            "career",
            "roadmap",
            "goal",
            "learning"
        ]):
            return "career"

        elif any(word in text for word in [
            "interview",
            "question",
            "hr",
            "technical"
        ]):
            return "interview"

        else:
            return "chat"