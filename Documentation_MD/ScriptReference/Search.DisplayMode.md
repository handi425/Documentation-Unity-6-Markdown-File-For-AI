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

# DisplayMode

enumeration

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

### Description

Options for setting the display mode to use for a search view.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    
    static class Example_ISearchView_displayMode
    {
        [[MenuItem](MenuItem.html)("Examples/[ISearchView](Search.ISearchView.html)/displayMode")]
        public static void Run()
        {
            // [SearchService](Search.SearchService.html) can open a SearchView.
            var view = [SearchService.ShowContextual](Search.SearchService.ShowContextual.html)("asset");
    
            // You can assign [DisplayMode](Search.DisplayMode.html) as iconSizeValue...
            view.itemIconSize = (float)[DisplayMode.List](Search.DisplayMode.List.html);
    
            // ... and this will update displayMode
            [Debug.Assert](Debug.Assert.html)(view.displayMode == [DisplayMode.List](Search.DisplayMode.List.html));
        }
    }
    

### Properties

[None](Search.DisplayMode.None.html)| Unspecified ISearchView display mode.  
---|---  
[Compact](Search.DisplayMode.Compact.html)| Display as a compact list view.  
[List](Search.DisplayMode.List.html)| Display as a list view.  
[Grid](Search.DisplayMode.Grid.html)| Display as a grid of icons of various
sizes.  
[Table](Search.DisplayMode.Table.html)| Display search results in a table.  
  
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

