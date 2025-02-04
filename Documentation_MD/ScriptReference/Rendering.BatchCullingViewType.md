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

# BatchCullingViewType

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

The type of an object that is requesting culling.

### Properties

[Unknown](Rendering.BatchCullingViewType.Unknown.html)| The type of the object
that is requesting culling is unknown.  
---|---  
[Camera](Rendering.BatchCullingViewType.Camera.html)| A Camera is requesting
culling.  
[Light](Rendering.BatchCullingViewType.Light.html)| A shadow-casting Light is
requesting culling.  
[Picking](Rendering.BatchCullingViewType.Picking.html)| The Scene view is
requesting culling so that it can render object picking data. Unity calls the
OnPerformCulling() with this enum value when a user clicks in the Scene view.  
[SelectionOutline](Rendering.BatchCullingViewType.SelectionOutline.html)| The
Scene view is requesting culling so that it can render the selection outline
of the objects currently picked. Unity calls the OnPerformCulling() with this
enum value when rendering the selection outline.  
[Filtering](Rendering.BatchCullingViewType.Filtering.html)| The Scene view is
requesting culling so that it can render filtered objects. Unity calls the
OnPerformCulling() with this enum value when a user writes a search query in
the Hierarchy window.  
  
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

