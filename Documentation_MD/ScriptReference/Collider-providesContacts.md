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

#  [Collider](Collider.html).providesContacts

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

public bool providesContacts;

### Description

Whether or not this Collider generates contacts for
[Physics.ContactEvent](Physics.ContactEvent.html).

If this property is set to `true`, all contacts produced by this collider will
appear in the buffer. If this property is set to false, contact generation
will depend on these factors:

  * If the Collider or its Rigidbody have a script with a [MonoBehaviour.OnCollisionStay](MonoBehaviour.OnCollisionStay.html) method, all contacts will be generated for [Physics.ContactEvent](Physics.ContactEvent.html).
  * If the Collider or its Rigidbody has a script with either [MonoBehaviour.OnCollisionEnter](MonoBehaviour.OnCollisionEnter.html) or [MonoBehaviour.OnCollisionExit](MonoBehaviour.OnCollisionExit.html) but not [MonoBehaviour.OnCollisionStay](MonoBehaviour.OnCollisionStay.html), enter and exit contacts will be generated for [Physics.ContactEvent](Physics.ContactEvent.html), but not stay contacts.
  * If the [PhysicsVisualizationSettings.showAllContacts](PhysicsVisualizationSettings-showAllContacts.html) property is set to true, all Colliders will generate all contacts for visualisation purposes!

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

