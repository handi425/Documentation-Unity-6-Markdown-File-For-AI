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

#  [GameObjectUtility](GameObjectUtility.html).GetUniqueNameForSibling

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

public static string GetUniqueNameForSibling([Transform](Transform.html)
parent, string name);

### Parameters

parent | Target parent for a new [GameObject](GameObject.html). Null means root level.  
---|---  
name | Requested name for a new [GameObject](GameObject.html).  
  
### Returns

**string** Unique name for a new [GameObject](GameObject.html).

### Description

You can use this method before instantiating a new sibling, or before
parenting one GameObject to another, to ensure the new child GameObject has a
unique name compared to its siblings in the hierarchy.

To use this method, you must provide a "target parent", and a "requested
name". The method uses an incremental numeric suffix appended to the name to
avoid duplicate names.  
  
If the target parent that you specify does _not_ already have a child with the
requested name that you specify, the method will return the requested name. If
the target parent _does_ have a child object matching the requested name, the
method will add an incremental number after the requested name until it finds
one that is unique. This is useful when trying to avoid duplicate naming.  
  
Note: You should use this method _before_ the GameObject becomes a child of
the target parent. If you use this method _after_ the GameObject is already a
child of the target parent, it will detect its own name among the siblings as
a conflict! If you want to perform the check after the GameObject is a child
of the target parent, you can use
[GameObjectUtility.EnsureUniqueNameForSibling](GameObjectUtility.EnsureUniqueNameForSibling.html)
instead.  
  
Additional resources:
[GameObjectUtility.EnsureUniqueNameForSibling](GameObjectUtility.EnsureUniqueNameForSibling.html),
[ObjectNames.GetUniqueName](ObjectNames.GetUniqueName.html).

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

