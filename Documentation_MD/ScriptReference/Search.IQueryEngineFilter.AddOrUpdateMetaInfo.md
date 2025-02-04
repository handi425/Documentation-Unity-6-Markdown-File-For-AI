[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [IQueryEngineFilter](Search.IQueryEngineFilter.html).AddOrUpdateMetaInfo

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public [Search.IQueryEngineFilter](Search.IQueryEngineFilter.html)
AddOrUpdateMetaInfo(string key, string value);

### Parameters

key | The key of the information.  
---|---  
value | The value of the information.  
  
### Returns

**IQueryEngineFilter** The current filter.

### Description

Add or update additional information specific to the filter.

You can use this function to add additional information on the filter.

    
    
    // Add a description to the filter
    var descriptionKey = "desc";
    var descriptionValue = "This filters the objects based on their id.";
    var exampleKey = "example";
    var exampleValue = "id>10 or id=2";
    queryEngine.TryGetFilter("id", out var filter);
    filter.AddOrUpdateMetaInfo(descriptionKey, descriptionValue)
        .AddOrUpdateMetaInfo(exampleKey, exampleValue);
    

You can then retrieve that information by accessing the
[metaInfo](Search.IQueryEngineFilter-metaInfo.html) property directly.

    
    
    var descriptionKey = "desc";
    var allFilters = queryEngine.GetAllFilters();
    var filtersWithDescription = allFilters.Where(f => f.metaInfo.ContainsKey(descriptionKey));
    

See [metaInfo](Search.IQueryEngineFilter-metaInfo.html) for a complete
example.

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

