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

#  [VisualElement](UIElements.VisualElement.html).style

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

public [UIElements.IStyle](UIElements.IStyle.html) style;

### Description

Sets the style values on a [VisualElement](UIElements.VisualElement.html).

The returned style data, computed from USS files or inline styles written to
this object in C#, doesn't represent the fully resolved styles, such as the
final height and width of a VisualElement. To access these fully resolved
styles, use resolvedStyle.  
  
For information about how to use this property and all the supported USS
properties, refer to the [Apply styles in C# scripts](../Manual/UIE-apply-
styles-with-csharp.html) and [USS properties reference](../Manual/UIE-USS-
Properties-Reference.html) manual pages.  
  
Additional resources: [VisualElement.resolvedStyle](UIElements.VisualElement-
resolvedStyle.html), [VisualElement.customStyle](UIElements.VisualElement-
customStyle.html), [StyleSheet](UIElements.StyleSheet.html)  
  

    
    
     // Set the background color of the element to red.
     element.style.backgroundColor = [Color.red](Color-red.html);
    

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

