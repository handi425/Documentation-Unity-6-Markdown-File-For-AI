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

#  [Collider2D](Collider2D.html).forceReceiveLayers

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

public [LayerMask](LayerMask.html) forceReceiveLayers;

### Description

The Layers that this [Collider2D](Collider2D.html) can receive forces from
during a Collision contact with another [Collider2D](Collider2D.html).

When a collision occurs between two [Collider2D](Collider2D.html), both
Colliders would normally receive a force from each other that separates them.
Both Colliders have a Layer assigned to them respectively, which can be the
same or different Layer(s). For the forces to apply, each Collider must send a
force to the Layer that is assigned to the other Collider, while also
receiving a force on their own Layer from the other Collider. Thus, both
Colliders must mutually agree on which Layers the forces are being sent and
received.  
  
The [forceReceiveLayers](Collider2D-forceReceiveLayers.html) property allows
you to select which Layers that the Collider receives force from, while
[forceSendLayers](Collider2D-forceSendLayers.html) allows you to select which
Layers the Collider sends a force to.  
  
**NOTES** :

  * Because forces only relate to a Collision contact, this features does not apply when either [Collider2D](Collider2D.html) is set to be a trigger via [Collider2D.isTrigger](Collider2D-isTrigger.html) and does not affect mutual forces applied by a [Joint2D](Joint2D.html).
  * Any [Rigidbody2D.bodyType](Rigidbody2D-bodyType.html) can send forces; however, only a [Dynamic Body Type](RigidbodyType2D.Dynamic.html) can receive forces. Neither [Kinematic Body Type](RigidbodyType2D.Kinematic.html) nor [Static Body Type](RigidbodyType2D.Static.html) can receive forces.
  * Forces being sent and received do not affect Collision callbacks which are still called even if no forces are applied.
  * During a Collision callback, any impulses reported by [ContactPoint2D.normalImpulse](ContactPoint2D-normalImpulse.html) or [ContactPoint2D.tangentImpulse](ContactPoint2D-tangentImpulse.html) will be the impulses that would have been applied if [forceSendLayers](Collider2D-forceSendLayers.html) and [forceReceiveLayers](Collider2D-forceReceiveLayers.html) were not used.

Additional resources:
[Collider2D.forceSendLayers](Collider2D-forceSendLayers.html).

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

