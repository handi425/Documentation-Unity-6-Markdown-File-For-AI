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

#  [ArticulationBody](ArticulationBody.html).collisionDetectionMode

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

[Switch to Manual](../Manual/class-ArticulationBody.html "Go to
ArticulationBody Component in the Manual")

public [CollisionDetectionMode](CollisionDetectionMode.html)
collisionDetectionMode;

### Description

The ArticulationBody's collision detection mode.

Use this property to set up an ArticulationBody for continuous collision
detection, in order to prevent fast moving objects from passing through other
objects without detecting collisions. For best results, set this property to
[CollisionDetectionMode.ContinuousDynamic](CollisionDetectionMode.ContinuousDynamic.html)
for fast moving objects, and set it to
[CollisionDetectionMode.Continuous](CollisionDetectionMode.Continuous.html)
for other objects these fast moving objects need to collide with.  
  
Note: These two options have a big impact on the physics engine processing
resources. To consume fewer processing resources, you can alternatively use
[CollisionDetectionMode.ContinuousSpeculative](CollisionDetectionMode.ContinuousSpeculative.html)
(which you can also use on kinematic objects). However, if you don't have
issues with collisions of fast objects, you should leave this property set to
the default value
[CollisionDetectionMode.Discrete](CollisionDetectionMode.Discrete.html).  
  
Restriction: You can use Continuous Collision Detection only for
ArticulationBodies with Sphere-, Capsule- or BoxColliders.  
  
Additional resources: [CollisionDetectionMode](CollisionDetectionMode.html).

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

