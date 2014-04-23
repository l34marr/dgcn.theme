from zope.interface import implements
from zope.component import getMultiAdapter
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from dgcn.theme.interfaces import ICustomTheme


class HomePage(BrowserView):

    implements(ICustomTheme)

    def getPeople(self):
        """Get Photos on People
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='ascending',
                       sort_limit=9)[:9]

    def fixed_items(self):
        """Get Items for Fixed-Position Tiles
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='ascending',
                       sort_limit=9)[:9]

