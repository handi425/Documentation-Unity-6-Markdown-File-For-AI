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

#  [VisualElement](UIElements.VisualElement.html).resolvedStyle

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

public [UIElements.IResolvedStyle](UIElements.IResolvedStyle.html)
resolvedStyle;

### Description

The final rendered style values of a visual element, as it's rendered in the
current frame.(Read Only)

Use `resolvedStyle` to find the actual rendered styling of a
[VisualElement](UIElements.VisualElement.html) in the current frame, such as
style values for width, height, and colors. You can get the resolved style
value of an element to make layout decisions, troubleshoot styling issues, or
ensure visual consistency across different platforms.  
  
The final rendered style is computed from applied classes, inherited styles
from ancestors, and inline styles defined in UXML or C# code. Therefore, the
resolved style might be different from what you set through the
[VisualElement.style](UIElements.VisualElement-style.html) property, depending
on the other styles applied to the element.  
  
To get the resolved style when the geometry changes, register a callback to
the [GeometryChangedEvent](UIElements.GeometryChangedEvent.html) event. If the
element's geometry remains unchanged, consider adding a
[scheduler](UIElements.IVisualElementScheduler.html) to periodically check the
element's resolved style. You can also poll the value during the
[MonoBehaviour.LateUpdate](MonoBehaviour.LateUpdate.html) phase at runtime if
you have access to MonoBehaviours.  
  
For a list of all the style properties supported by UI Toolkit, refer to [USS
properties reference](../Manual/UIE-USS-Properties-Reference.html).  
  
For more information about how to use this property and an example of how
style changes when layout updates, refer to [Apply styles in C#
scripts](../Manual/UIE-apply-styles-with-csharp.html).  
  
Additional resources: [VisualElement.style](UIElements.VisualElement-
style.html), [VisualElement.customStyle](UIElements.VisualElement-
customStyle.html)  
  

    
    
     // Get the resolved width of the element.
     float width = element.resolvedStyle.width;
    

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

