{
  'targets': [
    {
      'target_name': 'libgdata',
      'type': 'static_library',
      'dependencies': [
        'json.gyp:libjson',
      ],
      'sources': [
        'gdata/ACL/GDataACLKeyedRole.m',
        'gdata/ACL/GDataACLRole.m',
        'gdata/ACL/GDataACLScope.m',
        'gdata/ACL/GDataEntryACL.m',
        'gdata/ACL/GDataFeedACL.m',
        'gdata/ACL/GDataServiceACL.m',
        'gdata/BaseClasses/GDataEntryBase.m',
        'gdata/BaseClasses/GDataFeedBase.m',
        'gdata/BaseClasses/GDataObject.m',
        'gdata/BaseClasses/GDataQuery.m',
        'gdata/BaseClasses/GDataServiceBase.m',
        'gdata/BaseClasses/GDataServiceGoogle.m',
        'gdata/Clients/Contacts/GDataContactConstants.m',
        'gdata/Clients/Contacts/GDataContactElements.m',
        'gdata/Clients/Contacts/GDataContactEvent.m',
        'gdata/Clients/Contacts/GDataContactExternalID.m',
        'gdata/Clients/Contacts/GDataContactJot.m',
        'gdata/Clients/Contacts/GDataContactLanguage.m',
        'gdata/Clients/Contacts/GDataContactLink.m',
        'gdata/Clients/Contacts/GDataContactPriority.m',
        'gdata/Clients/Contacts/GDataContactRelation.m',
        'gdata/Clients/Contacts/GDataContactSensitivity.m',
        'gdata/Clients/Contacts/GDataContactUserDefinedField.m',
        'gdata/Clients/Contacts/GDataEntryContact.m',
        'gdata/Clients/Contacts/GDataEntryContactBase.m',
        'gdata/Clients/Contacts/GDataEntryContactGroup.m',
        'gdata/Clients/Contacts/GDataEntryContactProfile.m',
        'gdata/Clients/Contacts/GDataFeedContact.m',
        'gdata/Clients/Contacts/GDataFeedContactGroup.m',
        'gdata/Clients/Contacts/GDataFeedContactProfile.m',
        'gdata/Clients/Contacts/GDataGroupMembershipInfo.m',
        'gdata/Clients/Contacts/GDataQueryContact.m',
        'gdata/Clients/Contacts/GDataServiceGoogleContact.m',
        'gdata/Elements/GDataAtomPubControl.m',
        'gdata/Elements/GDataBaseElements.m',
        'gdata/Elements/GDataBatchID.m',
        'gdata/Elements/GDataBatchInterrupted.m',
        'gdata/Elements/GDataBatchOperation.m',
        'gdata/Elements/GDataBatchStatus.m',
        'gdata/Elements/GDataCategory.m',
        'gdata/Elements/GDataComment.m',
        'gdata/Elements/GDataCustomProperty.m',
        'gdata/Elements/GDataDateTime.m',
        'gdata/Elements/GDataDeleted.m',
        'gdata/Elements/GDataEmail.m',
        'gdata/Elements/GDataEntryContent.m',
        'gdata/Elements/GDataEntryLink.m',
        'gdata/Elements/GDataExtendedProperty.m',
        'gdata/Elements/GDataFeedLink.m',
        'gdata/Elements/GDataGenerator.m',
        'gdata/Elements/GDataGeoPt.m',
        'gdata/Elements/GDataIM.m',
        'gdata/Elements/GDataLink.m',
        'gdata/Elements/GDataMoney.m',
        'gdata/Elements/GDataName.m',
        'gdata/Elements/GDataOrganization.m',
        'gdata/Elements/GDataOrganizationName.m',
        'gdata/Elements/GDataPerson.m',
        'gdata/Elements/GDataPhoneNumber.m',
        'gdata/Elements/GDataPostalAddress.m',
        'gdata/Elements/GDataRating.m',
        'gdata/Elements/GDataStructuredPostalAddress.m',
        'gdata/Elements/GDataTextConstruct.m',
        'gdata/Elements/GDataValueConstruct.m',
        'gdata/Elements/GDataWhen.m',
        'gdata/Elements/GDataWhere.m',
        'gdata/Elements/GDataWho.m',
        'gdata/GDataFramework.m',
        'gdata/GDataUtilities.m',
        'gdata/Geo/GDataGeo.m',
        'gdata/HTTPFetcher/GTMGatherInputStream.m',
        'gdata/HTTPFetcher/GTMHTTPFetcher.m',
        'gdata/HTTPFetcher/GTMHTTPFetcherLogging.m',
        'gdata/HTTPFetcher/GTMHTTPFetcherService.m',
        'gdata/HTTPFetcher/GTMHTTPFetchHistory.m',
        'gdata/HTTPFetcher/GTMHTTPUploadFetcher.m',
        'gdata/HTTPFetcher/GTMMIMEDocument.m',
        'gdata/HTTPFetcher/GTMReadMonitorInputStream.m',
        'gdata/Introspection/GDataAtomCategoryGroup.m',
        'gdata/Introspection/GDataAtomCollection.m',
        'gdata/Introspection/GDataAtomServiceDocument.m',
        'gdata/Introspection/GDataAtomWorkspace.m',
        'gdata/Media/GDataMediaCategory.m',
        'gdata/Media/GDataMediaContent.m',
        'gdata/Media/GDataMediaCredit.m',
        'gdata/Media/GDataMediaGroup.m',
        'gdata/Media/GDataMediaKeywords.m',
        'gdata/Media/GDataMediaPlayer.m',
        'gdata/Media/GDataMediaRating.m',
        'gdata/Media/GDataMediaRestriction.m',
        'gdata/Media/GDataMediaThumbnail.m',
        'gdata/Media/GDataNormalPlayTime.m',
        'gdata/Networking/GDataAuthenticationFetcher.m',
        'gdata/Networking/GDataProgressMonitorInputStream.m',
        'gdata/Networking/GDataServerError.m',
        'gdata/OAuth2/GTMOAuth2Authentication.m',
        'gdata/OAuth2/GTMOAuth2SignIn.m',
        #'gdata/OAuth2/Mac/GTMOAuth2WindowController.m',
        'gdata/OAuth2/Touch/GTMOAuth2ViewControllerTouch.m',
        'gdata/XMLSupport/GDataXMLNode.m',
      ],
      'include_dirs': [
        '${SDKROOT}/usr/include/libxml2',
      ],
      'link_settings': {
        'libraries': [
          '${SDKROOT}/usr/lib/libxml2.dylib',
        ],
      },
      'direct_dependent_settings': {
        'include_dirs': [
          'gdata/Clients/Contacts',
          'gdata/BaseClasses',
          'gdata/HTTPFetcher',
          'gdata/Elements',
          'gdata/',
          'gdata/XMLSupport',
          'gdata/OAuth2/Touch',
          'gdata/OAuth2',
        ],
        'mac_bundle_resources': [
          'gdata/OAuth2/Touch/GTMOAuth2ViewTouch.xib',
        ],
      },
      # This code generates the following warnings with the current version of xcode.
      # Some of them may be real issues, but just silence them for now since we're not paying any attention.
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-Wno-incompatible-pointer-types',
          '-Wno-cast-of-sel-type',
          '-Wno-format-extra-args',
          '-Wno-format',
          '-Wno-objc-protocol-method-implementation',
          '-Wno-deprecated',
        ],
        'SKIP_INSTALL': 'YES',
      },
    },
  ],
}