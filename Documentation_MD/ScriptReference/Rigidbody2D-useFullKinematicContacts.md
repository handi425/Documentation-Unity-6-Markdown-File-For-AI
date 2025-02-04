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

#  [Rigidbody2D](Rigidbody2D.html).useFullKinematicContacts

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

public bool useFullKinematicContacts;

### Description

Should kinematic/kinematic and kinematic/static collisions be allowed?

By default, colliders attached to a pair of [Rigidbody2D](Rigidbody2D.html)
that are either both set to be kinematic or kinematic and static will not
collide with each other. Only [Rigidbody2D](Rigidbody2D.html) where one is
kinematic and the other is dynamic will collide by default.  
  
This default behaviour happens when this property is set to false however,
when set to true then kinematic [Rigidbody2D](Rigidbody2D.html) are allowed to
collide with other kinematic or static [Rigidbody2D](Rigidbody2D.html). When
this happens, collision callbacks will be produced when kinematic/kinematic or
kinematic/static pairs collide although no actual collision response will
happen. In other words, callbacks will happen but the
[Rigidbody2D](Rigidbody2D.html) will allow colliders to overlap similar to the
situation when a [Collider2D](Collider2D.html) is set to be a trigger.  
  
This can be a useful feature if detecting collisions is required with details
of the contact points and collision normal but without the automatic collision
response.  
  
This is only used when the [bodyType](Rigidbody2D-bodyType.html) is set to
[[[RigidbodyType2D.Kinematic](RigidbodyType2D.Kinematic.html)]].  
  
Additional resources: [bodyType](Rigidbody2D-bodyType.html).

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

