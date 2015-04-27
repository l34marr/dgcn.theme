from zope.interface import implements
from zope.component import getMultiAdapter
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from dgcn.theme.interfaces import ICustomTheme


class HomePage(BrowserView):

    implements(ICustomTheme)

    def getDress(self):
        """Get Photos on Dress
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('dress'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=9)[:9]

    def getBuilding(self):
        """Get Photos on Building
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('building'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=9)[:9]

    def getClothes(self):
        """Get Photos on Clothes
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('clothes'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=9)[:9]

    def getShip(self):
        """Get Photos on Ship
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('ship'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=9)[:9]

    def getRiver(self):
        """Get Photos on River
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('river'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=9)[:9]

    def getLighthouse(self):
        """Get Photos on LightHouse
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/photos'
        brain = catalog(portal_type='Photo',
                        Subject=('lighthouse'),
                        review_state='published',
                        path=path,
                        sort_on='getObjPositionInParent',
                        sort_order='descending')
        import random
        n = random.randint(0,104)
        if n < 105 - 20:
            return brain[n:n+20]
        else:
            return brain[n:] + brain[:n-20]

