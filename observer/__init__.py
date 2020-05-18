"""
Publisher
issues events (upon state change)
subscribers stored as list
subscribers get added/removed
pass contextual info to notification method to handle update appropriately
can pass self as arg so sub fetches data directly

Concrete Publisher
contains real business logic that's interesting for some subscribers

Subscriber
declares notification method on interface, usually update()
notified in random order, use extra logic to notify in specific order

Concrete Subscriber
performs actions in response to notifications issued by pub
implement same interface so publisher not coupled to concrete classes
concrete business logic

Client
creates publisher/subscriber
registers sub for pub updates

main
at runtime, configure pubs and subs
if applying pattern to existing class hierarchy, use composition to
make real publishers use subscription logic encapsulated in another object

applicability
when changes to the state of one obj requires changing other objs
& the set of objects is unknown beforehand or changes dynamically
observation is for ltd time in specific cases

eg custom button class, clients hook custom code fired onClick.
observer lets objs that implement subscriber interface subscribe 
to event notifications on publisher objects. add sub mechanism to buttons
to let client hook up custom code via custom subscriber classes

pseudocode
blog subscription
1. core functionality (publisher) - creating/publishing blog post 
2. subscriber classes with update()
Publisher:
  submit()
"""
from abc import ABC, abstractmethod
from collections import OrderedDict
import datetime


class Publisher(ABC):

  def __init__(self, subscribers):
    self.subscribers = subscribers  # list of tuples

  @abstractmethod    
  def subscribe(self, event_type: str, sub):
    self.subscribers.append((event_type, sub))
  
  @abstractmethod
  def unsubscribe(self, event_type: str, sub):
    self.subscribers.remove((event_type, sub))

  def notify(self, event_type, data):
    for sub in self.subscribers:
      if self.subscribers[0] == event_type:
        sub.update(event_type, data)
  

class BlogPublisher(Publisher):

  def __init__(self, subscribers):
    self.articles = []
    self.products = []
    super().__init__(subscribers)

  def subscribe(self, event_type: str, sub: str):
    return super().subscribe(sub)

  def unsubscribe(self, event_type: str, sub: str):
    return super().unsubscribe(sub)

  def publish(self, article):
    self.articles.append(article)
    self.notify('publication', article)

  def create(self, title: str, text: str):
    article = {
      'title': title,
      'text': text,
      'date': datetime.now(),
    }
    self.publish(article)

  def new_product(self, item: str):
    self.products.append(item)
    self.notify('product', item)


class Subscriber(ABC):

  def __init__(self):
    self.log = []
  
  @abstractmethod
  def update(self, event_type: str, data):
    print(event_type, data)
    self.log.append({event_type: data})


class EmailAlert(Subscriber):
  def __init__(self):
    super().__init__()

  def update(self, event_type, data):
    print('Ping about ' + event_type + '. Check it: ', data)
    super.update(event_type, data)




