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
[EditorCurveBinding](EditorCurveBinding.html).SerializeReferenceCurve(string,Type,string)

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

### Parameters

inPath | The transform path to the object to animate.  
---|---  
inType | The type of the MonoBehaviour managing the [SerializeReference](SerializeReference.html) instance to animate.  
refID | The reference id of the SerializeReference instance to animate. Additional resources: [ManagedReferenceUtility.GetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html)  
inPropertyName | The name of the property to animate on the object.  
  
### Description

Creates a preconfigured binding for a curve that points to a
[SerializeReference](SerializeReference.html) instance field.

Fields on objects referenced with SerializeReference can be animated when the
host object is derived from [MonoBehaviour](MonoBehaviour.html). The animation
binding to the referenced object will be based on the reference id instead of
the property path, which makes it possible to correctly resolve the animation
even when there are changes in the path leading to the referenced object. For
example, if the object is referenced from within an array, the animation is
retained even if the position of the object within the array changes.

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

