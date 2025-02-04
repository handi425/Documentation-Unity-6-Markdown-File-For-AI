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

#
[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html).GetManagedReferenceIdForObject

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

public static long GetManagedReferenceIdForObject([Object](Object.html) obj,
object scriptObj);

### Parameters

hostObj | The host object that supports [SerializeReference](SerializeReference.html). For example, [MonoBehaviour](MonoBehaviour.html) or [ScriptableObject](ScriptableObject.html).  
---|---  
refObj | The C# object, to which the reference Id is associated.  
  
### Returns

**long** Returns the managed reference Id. Returns
[ManagedReferenceUtility.RefIdUnknown](Serialization.ManagedReferenceUtility.RefIdUnknown.html)
if the managed reference Id has not been assigned yet.

### Description

Retrieves the managed reference Id for an object that is referenced using
[SerializeReference](SerializeReference.html).

Unity assigns an Id for an object when the Unity Object referencing the object
has been serialized, or when
[SetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html)
is called.  
  
Additional resources:
[SetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html),
[GetManagedReference](Serialization.ManagedReferenceUtility.GetManagedReference.html),
[SerializeReference](SerializeReference.html).

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

