from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from dgcn.theme.interfaces import ICustomTheme


class HomePage(BrowserView):

    implements(ICustomTheme)
    # TODO: Hard-coded Catalog Path Setting Might Need Refactoring.

    def getDress(self, lang='en', limit=9):
        """Get Photos on Dress
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('dress'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getBuilding(self, lang='en', limit=9):
        """Get Photos on Building
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('building'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getClothes(self, lang='en', limit=9):
        """Get Photos on Clothes
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('clothes'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getShip(self, lang='en', limit=9):
        """Get Photos on Ship
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('ship'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getRiver(self, lang='en', limit=9):
        """Get Photos on River
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
        return catalog(portal_type='Photo',
                       Subject=('river'),
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getLighthouse(self, lang='en'):
        """Get Photos on LightHouse
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/dgcn/' + lang + '/photos'
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

