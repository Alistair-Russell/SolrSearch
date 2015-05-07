from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete



class Snippet(models.Model):
    # importing the models package and extending the basic Model
    class Meta:
        app_label = "codekeeper"

    title = models.CharField(max_length=256, blank=True, null=True)
    # here blank is for Django and null is for the database
    snippet = models.TextField()

    tags = models. ManyToManyField("codekeeper.Tag")
    creator = models.ForeignKey("codekeeper.Person")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # self ALWAYS refers to that particular instance
        # the __ __ deal makes it so that calling methods on instances of snippet will do method.__str__(foo)
        return "{0}".format(self.title)
        # here 0 is replaced by title, and if we had {1} then the next param in format would be subbed in for that

# here we say that Snippet is the sender so that this class underneath ignores our other models, only listens to snippet
@receiver(post_save, sender=Snippet)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
    records = solrconn.query(type="snippet", item_id="{0}".format(instance.pk)).execute()
    if records:
        solrconn.delete_by_ids([x['id'] for x in records])

    d = {
        "id": str(uuid.uuid4()),
        "type": "snippet",
        "item_id": instance.pk,
        "snippet": instance.snippet,
        "title": instance.title
    }

    solrconn.add(d)
    solrconn.commit()

@receiver(post_delete, sender=Snippet)
def solr_del_index(sender, instance, **kwargs):
    from django.conf import settings
    import scorched

    solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
    records = solrconn.query(type="snippet", item_id="{0}".format(instance.pk)).execute()

    if records:
        solrconn.delete_by_ids([x['id'] for x in records])

    solrconn.commit()
