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
[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html).SetManagedReferenceIdForObject

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

public static bool SetManagedReferenceIdForObject([Object](Object.html) obj,
object scriptObj, long refId);

### Parameters

hostObj | The "host" object that supports [SerializeReference](SerializeReference.html). For example, [MonoBehaviour](MonoBehaviour.html) or [ScriptableObject](ScriptableObject.html).  
---|---  
refObj | The C# object, to which the reference Id will be assigned.  
refId | A positive number between 0 and Int64.MaxValue. This managed reference Id cannot be used by another object on the same host object. You can reuse the same managed reference Id on separate hosts.  
  
### Returns

**bool** Returns true if the Id was successfully set false otherwise.

### Description

Assigns a managed reference Id to an object that is referenced using
[SerializeReference](SerializeReference.html) on a specified host.

In normal usage, it is not necessary to use this method. By default, the Unity
Editor automatically generates a unique id for the object when it is first
serialized.  
  
If you use this method, it should be called after the referenced object is
created and before the next serialization of the host object that references
it. If the object is not referenced when the host object is serialized, Unity
prunes the object and discards its assigned Id. An object is "referenced" if
it is directly assigned to at least one field of the host object, or is
referenced indirectly via fields on other referenced objects.  
  
After being assigned, the managed reference id persists as a permanent local
identifier for the object provided the object is referenced by the host. This
identifier is retained even when the host object is unloaded and reloaded.  
  
Additional resources:
[GetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html),
[GetManagedReference](Serialization.ManagedReferenceUtility.GetManagedReference.html),
[SerializeReference](SerializeReference.html),
[SerializedProperty.managedReferenceId](SerializedProperty-
managedReferenceId.html).

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

