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
[AnimatorJobExtensions](Animations.AnimatorJobExtensions.html).BindCustomStreamProperty

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

public static
[Animations.PropertyStreamHandle](Animations.PropertyStreamHandle.html)
BindCustomStreamProperty([Animator](Animator.html) animator, string property,
[Animations.CustomStreamPropertyType](Animations.CustomStreamPropertyType.html)
type);

### Parameters

animator | The [Animator](Animator.html) instance that calls this method.  
---|---  
name | The name of the property.  
type | The type of property to create (float, integer or boolean).  
  
### Returns

**PropertyStreamHandle** Returns the PropertyStreamHandle that represents the
new binding.

### Description

Create a custom property in the
[AnimationStream](Animations.AnimationStream.html) to pass extra data to
downstream animation jobs in your graph. Custom properties created in the
[AnimationStream](Animations.AnimationStream.html) do not exist in the scene.

You can create custom properties in the
[AnimationStream](Animations.AnimationStream.html) that do not exist in the
scene. This can be useful when you want to communicate extra data to
downstream animation jobs in your graph.

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

