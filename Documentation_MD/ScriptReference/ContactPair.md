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

# ContactPair

struct in UnityEngine

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

A pair of Colliders that belong to the bodies in the parent
[ContactPairHeader](ContactPairHeader.html) struct.

Contains an array of [ContactPairPoint](ContactPairPoint.html)s that can be
retrieved using the [GetContactPoint](ContactPair.GetContactPoint.html)
method.

### Properties

[collider](ContactPair-collider.html)| The first Collider component of the
ContactPair.  
---|---  
[colliderInstanceID](ContactPair-colliderInstanceID.html)| Instance ID of the
first Collider in the ContactPair.  
[contactCount](ContactPair-contactCount.html)| The number of ContactPairPoints
that this pair contains.  
[impulseSum](ContactPair-impulseSum.html)| Total impulse sum of the pair.  
[isCollisionEnter](ContactPair-isCollisionEnter.html)| Whether or not this
pair is equivalent to a pair reported in MonoBehaviour.OnCollisionEnter
events.  
[isCollisionExit](ContactPair-isCollisionExit.html)| Whether or not this pair
is equivalent to a pair reported in MonoBehaviour.OnCollisionExit events.  
[isCollisionStay](ContactPair-isCollisionStay.html)| Whether or not this pair
is equivalent to a pair reported in MonoBehaviour.OnCollisionStay events.  
[otherCollider](ContactPair-otherCollider.html)| The second Collider component
of the ContactPair.  
[otherColliderInstanceID](ContactPair-otherColliderInstanceID.html)| Instance
ID of the second Collider in the ContactPair.  
  
### Public Methods

[CopyToNativeArray](ContactPair.CopyToNativeArray.html)| Copies the internal
ContactPairPoint buffer to the provided buffer.  
---|---  
[GetContactPoint](ContactPair.GetContactPoint.html)| Gets the ContactPairPoint
at the provided index of this pair.  
[GetContactPointFaceIndex](ContactPair.GetContactPointFaceIndex.html)| Get the
index of a face that a particular contact point belongs to in this
ContactPairPoint.  
  
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

