import pytest

from test_api.base import ApiBase


class TopicBase(ApiBase):
    """
    Базовый класс для тестов на топики. Содержит необходимые методы релевантных только для тестов на топики.
    """

    publish = False

    def create_topic(self, title, text, publish=True):
        res = self.api_client.post_topic_create(blog_id=350, title=title, text=text, publish=publish)
        assert res['success'] is True
        assert res.get('redirect_url')
        return int(res['redirect_url'].split('/')[-2])

    def check_topic_feed(self, topic_id, title, text, feed_type='all'):
        all_topics = self.api_client.get_topic_feed(feed_type=feed_type)

        topics = [t for t in all_topics['items'] if t['object']['id'] == topic_id]

        assert len(topics) == 1, f'Topic id {topic_id} does not present in feed "{feed_type}"'
        topic = topics[0]

        assert topic['object']['title'] == title
        assert topic['object']['text'] == text

    @pytest.fixture(scope='function')
    def topic(self):
        topic_data = self.builder.create_topic()
        topic_id = self.create_topic(title=topic_data.title, text=topic_data.text, publish=self.publish)

        topic_data.id = topic_id

        yield topic_data

        self.api_client.post_topic_delete(topic_data.id)
        self.api_client.get_topic(topic_data.id, expected_status=404)


class TestTopicDraft(TopicBase):
    """
    Родительский класс для тестов на создание топика.
    """

    publish = False

    def test_draft_topic_creation(self, topic):
        self.api_client.get_topic(topic.id, expected_status=200)


class TestTopicPublish(TestTopicDraft):
    """
    Дочерний класс для тестов на создание топика.
    Переопределяет тестовый метод test_draft_topic_creation
    Вызывает test_draft_topic_creation родителя через super, чтобы выполнить все действия родителя
    Используется тогда, когда нужно дополнить логику теста отдельной проверкой, которой не должно быть в родителе
    """

    publish = True

    def test_topic_creation(self, topic):
        super(TestTopicPublish, self).test_draft_topic_creation(topic)
        self.check_topic_feed(topic.id, topic.title, topic.text)


########################################
########################################


class TestTopicDraftVar2(TopicBase):
    """
    Родительский класс для тестов на создание топика (ВАРИАНТ 2).
    Создает топик и вызывает общий метод check().
    Всем наследникам, которым нужны альтренативные проверки, достаточно переопределить только сам метод проверки.
    """

    publish = False

    def check(self):
        print(self.topic_id)

    def test_draft_topic_creation(self):
        self.title = '#@^#^@#^@&*^#*!'
        self.text = 'fdsjkfsdkfhkjsd'

        self.topic_id = self.create_topic(title=self.title, text=self.text, publish=self.publish)

        self.check()


class TestTopicPublishVar2(TestTopicDraftVar2):
    """
    Дочерний класс для тестов на создание топика (ВАРИАНТ 2).
    Полностью автоматически выполняет тест родителя, но переопределяет метод проверки.
    Используется тогда, когда нужны разные реализации проверок во всех тестах. Каждый тест выполнит свою проверку.
    """

    publish = True

    def check(self):
        self.check_topic_feed(self.topic_id, self.title, self.text)


class TestTopicVote(TopicBase):
    """
    Баг. нельзя удалить топик, который лайкнули. Пользуемся вторым пользователем.
    """

    publish = True

    def test_delete_topic_after_vote(self, topic, second_user):
        self.api_client.get_topic(topic.id)
        self.check_topic_feed(topic.id, topic.title, topic.text)

        second_user.post_topic_vote(topic.id)
