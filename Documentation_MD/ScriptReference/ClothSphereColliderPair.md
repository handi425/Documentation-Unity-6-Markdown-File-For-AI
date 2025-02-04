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

# ClothSphereColliderPair

struct in UnityEngine

/

Implemented in:[UnityEngine.ClothModule](UnityEngine.ClothModule.html)

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

A pair of SphereColliders used to define shapes for Cloth objects to collide
against.

A ClothSphereColliderPair can contain either a single valid SphereCollider
instance (with the second one being null), or a pair of two SphereColliders.
In the former cases the ClothSphereColliderPair just represents a single
SphereCollider for the cloth to collide against. In the latter case, it
represents a conic capsule shape defined by the two spheres, and the cone
connecting the two. Conic capsule shapes are useful for modelling limbs of a
character.  
  
Select the cloth object to see a visualization of Cloth colliders shapes in
the Scene view.

### Properties

[first](ClothSphereColliderPair-first.html)| The first SphereCollider of a
ClothSphereColliderPair.  
---|---  
[second](ClothSphereColliderPair-second.html)| The second SphereCollider of a
ClothSphereColliderPair.  
  
### Constructors

[ClothSphereColliderPair](ClothSphereColliderPair-ctor.html)| Creates a
ClothSphereColliderPair. If only one SphereCollider is given, the
ClothSphereColliderPair will define a simple sphere. If two SphereColliders
are given, the ClothSphereColliderPair defines a conic capsule shape, composed
of the two spheres and the cone connecting the two.  
---|---  
  
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

