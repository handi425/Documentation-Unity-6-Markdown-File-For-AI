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

#  [SearchUtils](Search.SearchUtils.html).GetTransformPath

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

public static string GetTransformPath([Transform](Transform.html) tform);

### Parameters

tform | Transform to extract name from.  
---|---  
  
### Returns

**string** Returns a transform name using "/" as hierarchy separator.

### Description

Format the pretty name of a Transform component by appending all the parent
hierarchy names.

    
    
    static string FetchLabel([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
    {
        if (item.label != null)
            return item.label;
    
        var go = ObjectFromItem(item);
        if (!go)
            return item.id;
    
        var transformPath = [SearchUtils.GetTransformPath](Search.SearchUtils.GetTransformPath.html)(go.transform);
        var components = go.GetComponents<[Component](Component.html)>();
        if (components.Length > 2 && components[1] && components[components.Length - 1])
            item.label = $"{transformPath} ({components[1].GetType().Name}..{components[components.Length - 1].GetType().Name})";
        else if (components.Length > 1 && components[1])
            item.label = $"{transformPath} ({components[1].GetType().Name})";
        else
            item.label = $"{transformPath} ({item.id})";
    
        return item.label;
    }
    

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

