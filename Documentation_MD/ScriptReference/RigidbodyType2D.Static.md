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

#  [RigidbodyType2D](RigidbodyType2D.html).Static

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

Sets the [Rigidbody2D](Rigidbody2D.html) to have static behaviour.

Static behaviour stops the [Rigidbody2D](Rigidbody2D.html) from reacting to
gravity or applied forces including contacts with any other
[Rigidbody2D](Rigidbody2D.html).  
  
This type of [Rigidbody2D](Rigidbody2D.html) should never repositioned
explicitly. It is designed to never move.  
  
A static [Rigidbody2D](Rigidbody2D.html) will only collide with a dynamic
[Rigidbody2D](Rigidbody2D.html) body type. The exception to this is if
[Rigidbody2D.useFullKinematicContacts](Rigidbody2D-useFullKinematicContacts.html)
is set to true in which case it will also collide with any
[[[Kinematic](RigidbodyType2D.Kinematic.html)]] body types.  
  
When an attached [Collider2D](Collider2D.html) is set to trigger, it will
always produce a trigger for any [Collider2D](Collider2D.html) attached to
[[[Dynamic](RigidbodyType2D.Dynamic.html)]] or
[[[Kinematic](RigidbodyType2D.Kinematic.html)]] body types.  
  
Additional resources: [Rigidbody2D.bodyType](Rigidbody2D-bodyType.html),
[Rigidbody2D.useFullKinematicContacts](Rigidbody2D-useFullKinematicContacts.html).

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

