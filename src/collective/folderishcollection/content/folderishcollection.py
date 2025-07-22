from plone.app.contenttypes import _
from plone.app.contenttypes.behaviors.collection import ICollection
from plone.dexterity.content import Container
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory


class IFolderishCollection(Interface):
    """Marker interface"""

@implementer(IFolderishCollection, ICollection)
class FolderishCollection(Container):

    def results(
        self,
        batch=True,
        b_start=0,
        b_size=None,
        sort_on=None,
        limit=None,
        brains=False,
        custom_query=None,
    ):
        if custom_query is None:
            custom_query = {}
        querybuilder = getMultiAdapter(
            (self, getRequest()), name="querybuilderresults"
        )
        sort_order = "reverse" if self.sort_reversed else "ascending"
        if not b_size:
            b_size = self.item_count
        if not sort_on:
            sort_on = self.sort_on
        if not limit:
            limit = self.limit
        return querybuilder(
            query=self.query,
            batch=batch,
            b_start=b_start,
            b_size=b_size,
            sort_on=sort_on,
            sort_order=sort_order,
            limit=limit,
            brains=brains,
            custom_query=custom_query,
        )

    def selectedViewFields(self):
        """Returns a list of all metadata fields from the catalog that were
           selected.

        The template expects a tuple/list of (id, title) of the field.

        """
        _mapping = {}
        vocab = getUtility(
            IVocabularyFactory, name="plone.app.vocabularies.MetadataFields"
        )
        for field in vocab(self):
            _mapping[field.value] = (field.value, field.title)
        ret = [_mapping[field] for field in self.customViewFields]
        return ret

