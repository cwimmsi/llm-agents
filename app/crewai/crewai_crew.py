from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class ClassifierCrew:

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def ticket_classifier(self) -> Agent:
        return Agent(config=self.agents_config["ticket_classifier"], verbose=True)

    @task
    def classify_ticket_type_task(self) -> Task:
        return Task(config=self.tasks_config["classify_ticket_type_task"])

    @task
    def classify_ticket_priority_task(self) -> Task:
        return Task(config=self.tasks_config["classify_ticket_priority_task"])

    @task
    def classify_ticket_sentiment_task(self) -> Task:
        return Task(config=self.tasks_config["classify_ticket_sentiment_task"])

    @task
    def classify_ticket_tags_task(self) -> Task:
        return Task(config=self.tasks_config["classify_ticket_tags_task"])

    @task
    def classify_responsible_team_task(self) -> Task:
        return Task(
            config=self.tasks_config["classify_responsible_team_task"],
            context=[self.classify_ticket_tags_task()],
        )

    @task
    def key_words_extraction_task(self) -> Task:
        return Task(config=self.tasks_config["key_words_extraction_task"])

    @task
    def initial_action_suggestion_task(self) -> Task:
        return Task(config=self.tasks_config["initial_action_suggestion_task"])

    @task
    def confidence_score_task(self) -> Task:
        return Task(config=self.tasks_config["confidence_score_task"])

    @task
    def reasoning_task(self) -> Task:
        return Task(
            config=self.tasks_config["reasoning_task"],
            context=[
                self.classify_ticket_type_task(),
                self.classify_ticket_priority_task(),
                self.classify_ticket_sentiment_task(),
                self.classify_ticket_tags_task(),
                self.classify_responsible_team_task(),
            ],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.SEQUENTIAL,
            verbose=True,
        )
